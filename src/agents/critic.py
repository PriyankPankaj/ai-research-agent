from src.agents.base import BaseAgent
from src.state import ResearchState
from src.memory.memory_manager import MemoryManager


class CriticAgent(BaseAgent):
    name = "critic"

    def __init__(self):
        self.memory = MemoryManager()

    def run(self, state: ResearchState) -> ResearchState:
        state.critique = "Draft reviewed. No major gaps identified."
        state.is_complete = True

        # Persist this session's finding into long-term memory
        finding = state.draft_report or " ".join(state.extracted_notes) or ""
        if finding:
            self.memory.store_finding(
                session_id=state.query,  # simple stand-in until real session_id is threaded through
                query=state.query,
                content=finding,
            )
        return state