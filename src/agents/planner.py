from src.agents.base import BaseAgent
from src.state import ResearchState
from src.memory.memory_manager import MemoryManager


class PlannerAgent(BaseAgent):
    name = "planner"

    def __init__(self):
        self.memory = MemoryManager()

    def run(self, state: ResearchState) -> ResearchState:
        # Recall relevant past findings before planning new subtasks
        state.memory_context = self.memory.recall(state.query, n_results=3)

        # TODO: use an LLM to break query into subtasks; for now, single subtask
        state.subtasks = [state.query]
        return state