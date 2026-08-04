from src.agents.base import BaseAgent
from src.state import ResearchState

class ReaderAgent(BaseAgent):
    name = "reader"

    def run(self, state: ResearchState) -> ResearchState:
        state.extracted_notes = []  # TODO: extract content from sources
        return state