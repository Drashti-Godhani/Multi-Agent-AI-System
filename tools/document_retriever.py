import os
from openai import OpenAI
from tools.file_reader import FileReaderTool
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

class DocumentRetrieverTool:
    """
    File read karta hai + LLM se relevant content extract karta hai.
    Ye sirf file content dump nahi karta — task ke according answer deta hai.
    """

    def __init__(self):
        self.file_reader = FileReaderTool()
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY")
        )

    def retrieve(self, file_path: str, query: str) -> str:
        """
        File padho aur query ke basis pe relevant info extract karo.
        """

        # Step 1: File content padho
        file_content = self.file_reader.read(file_path)

        if file_content.startswith("[FileReader] Error"):
            return file_content

        # Step 2: LLM se relevant part extract karo
        prompt = f"""
You are a Document Retrieval Agent.

The user wants to extract specific information from a document.

Query: {query}

Document Content:
{file_content[:8000]}  

Instructions:
- Answer the query using ONLY information from the document.
- If the answer is not in the document, say "Information not found in document."
- Be concise and direct.
- Do NOT add external knowledge.
"""

        response = self.client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content
