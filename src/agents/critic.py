from src.agents.base import BaseAgent
from src.state import ResearchState
from src.memory.memory_manager import MemoryManager


class CriticAgent(BaseAgent):
    name = "critic"

    def __init__(self):
        self.memory = MemoryManager()

    def run(self, state: ResearchState) -> ResearchState:
        issues = []

        real_sources = [
            s for s in state.sources
            if "error" not in s.get("content", "").lower()
            and "unavailable" not in s.get("content", "").lower()
        ]

        if len(real_sources) < 2:
            issues.append("Fewer than 2 reliable sources were found; report may lack depth.")

        if not state.draft_report or len(state.draft_report) < 100:
            issues.append("Draft report is unusually short.")

        if issues:
            state.critique = "Issues found: " + "; ".join(issues)
        else:
            state.critique = "Draft reviewed. No major gaps identified."

        state.is_complete = True

        findings_only = "\n".join(state.extracted_notes) if state.extracted_notes else ""
        finding = findings_only
        if finding:
            self.memory.store_finding(
                session_id=state.query,
                query=state.query,
                content=finding,
            )
        return state