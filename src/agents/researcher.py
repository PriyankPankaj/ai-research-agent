from src.agents.base import BaseAgent
from src.state import ResearchState
from src.rag.retriever import Retriever


class ResearchAgent(BaseAgent):
    name = "researcher"

    def __init__(self):
        self.retriever = Retriever()

    def run(self, state: ResearchState) -> ResearchState:
        sources = self.retriever.query(state.query, n_results=3)
        state.sources = sources
        return state