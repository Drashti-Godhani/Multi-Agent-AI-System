# 🤖 Multi-Agent AI Research Assistant

<img width="1448" height="1086" alt="Image" src="https://github.com/user-attachments/assets/d19727d0-3453-457b-8e84-cb009e35922a" />

A modular, multi-agent AI system built with Python and OpenRouter API that breaks down complex user queries into tasks, routes them to specialized agents, and synthesizes a final structured answer.

---

## ✨ Features

- 🧠 **Planner Agent** — breaks any complex query into 4–8 executable tasks
- 🔀 **Router Agent** — intelligently routes each task to the right agent
- 🔍 **Research Agent** — deep analysis and research using GPT-4o-mini
- 🛠️ **Tool Agent** — handles calculations, web search, and file reading
- 💾 **Memory Store** — stores intermediate results across all agents
- 📝 **Synthesizer Agent** — combines everything into one clean final answer

---

## 🗂️ Project Structure

```
multi_agent/
│
├── main.py                        # Entry point
│
├── agents/
│   ├── planner_agent.py           # Breaks query into tasks
│   ├── router_agent.py            # Routes tasks to agents
│   ├── research_agent.py          # Research & analysis
│   ├── tool_agent.py              # Calculator, search, file reader
│   └── synthesizer_agent.py       # Combines all results
│
├── tools/
│   ├── calculator.py              # Math expression evaluator
│   ├── web_search.py              # Web search (mock / extendable)
│   ├── file_reader.py             # Reads PDF, TXT, DOCX, CSV
│   └── document_retriever.py      # Smart query-based doc retrieval
│
├── memory/
│   └── memory_store.py            # Stores intermediate task results
│
├── workflows/
│   └── execution_flow.py          # Orchestrates the full pipeline
│
├── requirements.txt
└── README.md
```

---

## 🔁 How It Works

```
User Query
    ↓
🧠 Planner Agent   →  Breaks into tasks
    ↓
🔀 Router Agent    →  Decides: Research or Tool?
    ↓
🔍 Research Agent  →  Deep analysis tasks
🛠️ Tool Agent      →  Calculate / Search / Read file
    ↓
💾 Memory Store    →  Saves every result
    ↓
📝 Synthesizer     →  Final clean answer
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/multi-agent-ai-assistant.git
cd multi-agent-ai-assistant
```

### 2. Create virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API key

In `agents/planner_agent.py`, `research_agent.py`, `synthesizer_agent.py`, and `tools/document_retriever.py`, replace:

```python
api_key="your-openrouter-api-key"
```

> Get your free API key at [openrouter.ai](https://openrouter.ai)

### 5. Run

```bash
python main.py
```

---

## 🧪 Example Queries

```
# Research + Calculation
Research electric vehicles in India. Search the latest EV sales data.
Calculate the growth percentage if sales increased from 1.2 million to 1.8 million.

# File Reading
read file sample_report.txt

# Smart Document Retrieval
retrieve from sample_report.txt what are the key findings and conclusion

# Mixed Query
retrieve from sample_report.txt the conclusion, also calculate 250 * 4, and search for AI trends
```

---

## 🛠️ Tools Overview

| Tool | What it does |
|---|---|
| `CalculatorTool` | Evaluates math expressions, growth %, percentages |
| `WebSearchTool` | Searches for information (mock — replaceable with Tavily/SerpAPI) |
| `FileReaderTool` | Reads `.txt`, `.pdf`, `.docx`, `.csv`, `.md` files |
| `DocumentRetrieverTool` | Reads a file + extracts query-specific info using LLM |

---

## 📦 Requirements

```
openai
pypdf
python-docx
```

---

## 👩‍💻 Author

**Drashti** — built with 💙 using Python & OpenRouter API
