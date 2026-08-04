from src.agents.base import BaseAgent
from src.state import ResearchState

class WriterAgent(BaseAgent):
    name = "writer"

    def run(self, state: ResearchState) -> ResearchState:
        state.draft_report = ""  # TODO: draft report from notes
        return state