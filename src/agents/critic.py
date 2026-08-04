from src.agents.base import BaseAgent
from src.state import ResearchState

class CriticAgent(BaseAgent):
    name = "critic"

    def run(self, state: ResearchState) -> ResearchState:
        state.critique = ""  # TODO: review draft, flag gaps
        state.is_complete = True
        return state