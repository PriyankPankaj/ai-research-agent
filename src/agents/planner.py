from src.agents.base import BaseAgent
from src.state import ResearchState

class PlannerAgent(BaseAgent):
    name = "planner"

    def run(self, state: ResearchState) -> ResearchState:
        state.subtasks = []  # TODO: break query into subtasks
        return state