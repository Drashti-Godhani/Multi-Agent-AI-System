import os


class FileReaderTool:
    """
    Local files read karta hai — PDF, TXT, DOCX, CSV support.
    """

    SUPPORTED_EXTENSIONS = [".txt", ".pdf", ".docx", ".csv", ".md"]

    def read(self, file_path: str) -> str:

        file_path = file_path.strip()

        if not os.path.exists(file_path):
            return f"[FileReader] Error: File not found -> '{file_path}'"

        ext = os.path.splitext(file_path)[1].lower()

        if ext not in self.SUPPORTED_EXTENSIONS:
            return f"[FileReader] Error: Unsupported file type '{ext}'. Supported: {self.SUPPORTED_EXTENSIONS}"

        try:
            if ext in (".txt", ".md"):
                return self._read_text(file_path)
            elif ext == ".pdf":
                return self._read_pdf(file_path)
            elif ext == ".docx":
                return self._read_docx(file_path)
            elif ext == ".csv":
                return self._read_csv(file_path)
        except Exception as e:
            return f"[FileReader] Error reading file: {str(e)}"

    def _read_text(self, path: str) -> str:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        return f"[File: {os.path.basename(path)}]\n\n{content}"

    def _read_pdf(self, path: str) -> str:
        try:
            import PyPDF2
            text = ""
            with open(path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                for i, page in enumerate(reader.pages):
                    text += f"\n--- Page {i+1} ---\n"
                    text += page.extract_text() or ""
            return f"[File: {os.path.basename(path)}]\n{text}"
        except ImportError:
            return "[FileReader] Error: PyPDF2 not installed. Run: pip install PyPDF2"

    def _read_docx(self, path: str) -> str:
        try:
            from docx import Document
            doc = Document(path)
            text = "\n".join([para.text for para in doc.paragraphs if para.text.strip()])
            return f"[File: {os.path.basename(path)}]\n\n{text}"
        except ImportError:
            return "[FileReader] Error: python-docx not installed. Run: pip install python-docx"

    def _read_csv(self, path: str) -> str:
        import csv
        rows = []
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                rows.append(", ".join(row))
        preview = rows[:100]
        result = "\n".join(preview)
        if len(rows) > 100:
            result += f"\n\n... ({len(rows) - 100} more rows not shown)"
        return f"[File: {os.path.basename(path)}]\n\n{result}"