from src.agents.base import BaseAgent
from src.state import ResearchState

class ResearchAgent(BaseAgent):
    name = "researcher"

    def run(self, state: ResearchState) -> ResearchState:
        state.sources = []  # TODO: retrieve sources via RAG
        return state