import re
class RouterAgent:

    def route(self, task: str) -> str:
        task_lower = task.lower()

        tool_keywords = [
            # Calculator
            "calculate", "compute", "math", "how much is", "convert",
            # Web Search
            "search", "retrieve", "fetch", "lookup", "find",
            "what is the price", "current", "latest news", "how much",
            # File operations
            "read file", "open file", "load file",
            "read the file", "retrieve from", "extract from",
            "find in", "from file", "in the document", "in the file",
            ".pdf", ".txt", ".docx", ".csv", ".md",
            "growth percentage", "percentage", "% growth", 
        ]

        research_keywords = [
    "research", "compare", "analyze", "analyse",
    "study", "evaluate", "explain", "describe",
    "what is", "why", "how does", "difference between",
    "summarize", "overview", "history",
    "electric vehicle", "ev "          
]
# Tool agent ko pehle check karo (specific actions)
        for word in tool_keywords:
            if word in task_lower:
                return "tool_agent"
            
        if re.search(r'\.(pdf|txt|docx|csv|md)\b', task_lower):
            return "tool_agent"

        # Phir research agent
        for word in research_keywords:
            if word in task_lower:
                return "research_agent"

        # Default: research agent
        return "research_agent"