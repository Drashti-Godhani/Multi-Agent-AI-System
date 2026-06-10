from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")
class SynthesizerAgent:

    def __init__(self):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY")
        )

    def synthesize(self, user_query: str, history: list[dict]) -> str:
        """
        history: list of { task, agent, result } dicts from MemoryStore
        """

        # Saari findings compile karo
        compiled = ""
        for i, entry in enumerate(history, start=1):
            compiled += f"\n--- Task {i} (handled by {entry['agent']}) ---\n"
            compiled += f"Task: {entry['task']}\n"
            compiled += f"Result:\n{entry['result']}\n"

        prompt = f"""
You are a Synthesizer Agent.

The user asked: "{user_query}"

Multiple agents worked on different parts of this request and produced the following findings:

{compiled}

Your job:
- Combine all findings into one clear, well-structured final answer.
- Remove repetition.
- Use these emojis for formatting:
  📌 for main section headings
  🔍 for research findings
  📊 for data and calculations
  ✅ for conclusions
  💡 for recommendations or insights
- Do NOT mention agents or tasks internally — just present the answer.
- IMPORTANT: For calculations, show results in plain text only.
  ❌ Never use LaTeX format like \[ \frac{{}} \] or \text{{}}
  ✅ Always write like: Growth Percentage = ((1.8 - 1.2) / 1.2) x 100 = 50.00%
"""

        response = self.client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content
