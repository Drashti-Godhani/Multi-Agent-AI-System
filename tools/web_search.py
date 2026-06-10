class WebSearchTool:
    """
    Mock web search tool.
    Real implementation ke liye: SerpAPI, Tavily, or DuckDuckGo API use karo.
    """

    def search(self, query: str) -> str:

        mock_results = {
            "python": "Python is a versatile, high-level language widely used for backend, data science, and AI.",
            "java": "Java is a robust, object-oriented language popular in enterprise systems.",
            "ai": "Artificial Intelligence is transforming industries through automation, NLP, and machine learning.",
            "machine learning": "Machine Learning allows systems to learn from data without being explicitly programmed.",
            "javascript": "JavaScript is the primary language for web frontend development, also used in backend via Node.js.",
            "react": "React is a popular JavaScript library by Meta for building user interfaces.",
            "llm": "Large Language Models (LLMs) like GPT and Claude can understand and generate human-like text.",
        }

        query_lower = query.lower()

        for key, result in mock_results.items():
            if key in query_lower:
                return f"Search result for '{query}':\n{result}"

        return f"Search result for '{query}':\nNo specific results found. Please refine your search query."