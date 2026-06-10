import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

class PlannerAgent:

    def __init__(self):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY")
        )

    def plan(self, user_query: str) -> list[str]:
        prompt = f"""
You are a Planner Agent.

Break the user request into 4-8 high-level executable tasks.

Rules:
- Keep tasks concise.
- Do not create very detailed implementation steps.
- Tasks should be suitable for routing to worker agents.
- IMPORTANT: If the task involves reading or retrieving from a file,
  keep it as ONE single task. Do not split file operations.
- Return ONLY a valid Python list of strings. No explanation, no markdown.

User Request:
{user_query}
"""

        response = self.client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        raw = response.choices[0].message.content
        return raw