import re
from tools.calculator import CalculatorTool
from tools.web_search import WebSearchTool
from tools.file_reader import FileReaderTool
from tools.document_retriever import DocumentRetrieverTool


class ToolAgent:

    def __init__(self):
        self.calculator = CalculatorTool()
        self.search_tool = WebSearchTool()
        self.file_reader = FileReaderTool()
        self.doc_retriever = DocumentRetrieverTool()

    def execute(self, task: str) -> str:

        task_lower = task.lower()

        # --- 1. File Read (raw) ---
        file_read_keywords = [
            "read file", "open file", "load file",
            "read the file", "contents of"
        ]
        for keyword in file_read_keywords:
            if keyword in task_lower:
                file_path = self._extract_file_path(task)
                if file_path:
                    print(f"[ToolAgent] Reading file: {file_path}")
                    return self.file_reader.read(file_path)

        # --- 2. Document Retrieval (smart query on file) ---
        doc_keywords = [
            "retrieve from", "extract from", "find in",
            "from file", "in the document", "in the file"
        ]
        for keyword in doc_keywords:
            if keyword in task_lower:
                file_path = self._extract_file_path(task)
                if file_path:
                    print(f"[ToolAgent] Document retrieval from: {file_path}")
                    return self.doc_retriever.retrieve(file_path, task)

        # --- 3. Calculator ---
        calc_keywords = [
            "calculate", "compute", "math", "how much is", "convert",
            "growth percentage", "percentage", "% growth", "increase by"
        ]
        for keyword in calc_keywords:
            if keyword in task_lower:
                numbers = re.findall(r"\d+\.?\d*", task)
                if len(numbers) >= 2:
                    # Growth % formula
                    if any(w in task_lower for w in ["growth", "increase", "percent"]):
                        old_val = float(numbers[0])
                        new_val = float(numbers[1])
                        growth = ((new_val - old_val) / old_val) * 100
                        return (
                            f"Growth Percentage = "
                            f"(({new_val} - {old_val}) / {old_val}) x 100 = {growth:.2f}%"
                        )
                # Normal expression
                expression = task_lower
                for kw in calc_keywords:
                    expression = expression.replace(kw, "")
                expression = expression.strip()
                result = self.calculator.calculate(expression)
                if result != "Invalid Expression":
                    return f"Calculation result: {result}"

        # --- 4. Default: Web Search ---
        return self.search_tool.search(task)

    def _extract_file_path(self, task: str) -> str | None:
        # Quoted path: "report.pdf" ya 'notes.txt'
        quoted = re.findall(r'["\']([^"\']+\.[a-zA-Z]{2,5})["\']', task)
        if quoted:
            return quoted[0]

        # Extension-based match
        ext_match = re.findall(
            r"[\w/\\.\-]+\.(?:pdf|txt|docx|csv|md)", task, re.IGNORECASE
        )
        if ext_match:
            return ext_match[0]

        return None