import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

class ResearchAgent:
    
    def __init__(self):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY")
        )


    
    def execute(self, task: str) -> str:

        prompt = f"""
You are a Research Agent.

Your job is to EXECUTE the given task and provide detailed findings.

Rules:
- Do NOT create a plan or subtasks.
- Do NOT return a Python list or code.
- Give actual, factual, useful information.
- Format your response with these emojis for sections:
  📌 for main topic heading
  🔍 for key findings or details  
  📊 for data, numbers, statistics
  ✅ for conclusions or recommendations
  💡 for insights or tips

Task:
{task}
"""
        response = self.client.chat.completions.create(
                model="openai/gpt-4o-mini",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

        return response.choices[0].message.content