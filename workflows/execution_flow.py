from ast import literal_eval

from agents.planner_agent import PlannerAgent
from agents.router_agent import RouterAgent
from agents.research_agent import ResearchAgent
from agents.tool_agent import ToolAgent
from agents.synthesizer_agent import SynthesizerAgent
from memory.memory_store import MemoryStore


def run_workflow(user_query: str) -> str:
    """
    Full multi-agent workflow:
    1. Planner  -> query ko tasks mein todta hai
    2. Router   -> har task ke liye sahi agent choose karta hai
    3. Research/Tool Agent -> task execute karta hai
    4. Memory   -> intermediate results store karta hai
    5. Synthesizer -> sabhi results combine karke final answer deta hai
    """

    print("\n[Workflow] Starting...")

    # --- Agents & Memory initialize karo ---
    planner = PlannerAgent()
    router = RouterAgent()
    research_agent = ResearchAgent()
    tool_agent = ToolAgent()
    synthesizer = SynthesizerAgent()
    memory = MemoryStore()

    # --- Step 1: Plan ---
    print("[Planner] Breaking query into tasks...")
    raw_tasks = planner.plan(user_query)

    # LLM string -> Python list
    if isinstance(raw_tasks, str):
        cleaned = raw_tasks.replace("```python", "").replace("```", "").strip()
        try:
            tasks = literal_eval(cleaned)
            if not isinstance(tasks, list):
                tasks = [cleaned]
        except Exception:
            tasks = [cleaned]
    else:
        tasks = raw_tasks

    print(f"[Planner] {len(tasks)} tasks created:")
    for i, t in enumerate(tasks, 1):
        print(f"  {i}. {t}")

    # --- Steps 2 & 3 & 4: Route -> Execute -> Store ---
    for task in tasks:
        selected_agent = router.route(task)
        print(f"\n[Router] '{task[:60]}...' -> {selected_agent}" if len(task) > 60 else f"\n[Router] '{task}' -> {selected_agent}")

        if selected_agent == "research_agent":
            print("[ResearchAgent] Executing...")
            result = research_agent.execute(task)
        else:
            print("[ToolAgent] Executing...")
            result = tool_agent.execute(task)

        # Memory mein save karo
        memory.save(task=task, agent=selected_agent, result=result)
        print("[Memory] Saved result for task.")

    # --- Step 5: Synthesize ---
    print("\n[Synthesizer] Combining all results...")
    final_answer = synthesizer.synthesize(
        user_query=user_query,
        history=memory.get_history()
    )

    return final_answer
