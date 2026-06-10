class MemoryStore:
    """
    Intermediate results store karta hai - task se result tak ka mapping.
    """

    def __init__(self):
        self._store = {}  # { task: result }
        self._history = []  # [ {task, agent, result} ]

    def save(self, task: str, agent: str, result: str):
        self._store[task] = result
        self._history.append({
            "task": task,
            "agent": agent,
            "result": result
        })

    def get(self, task: str):
        return self._store.get(task, None)

    def get_all_results(self):
        return [entry["result"] for entry in self._history]

    def get_history(self):
        return self._history

    def clear(self):
        self._store.clear()
        self._history.clear()
