from src.agents.base import BaseAgent
from src.state import ResearchState


class WriterAgent(BaseAgent):
    name = "writer"

    def run(self, state: ResearchState) -> ResearchState:
        parts = [f"Research Report: {state.query}\n"]

        if state.memory_context:
            parts.append("Related past findings:")
            for mem in state.memory_context:
                parts.append(f"- (from prior query '{mem['original_query']}'): {mem['content'][:150]}...")
            parts.append("")

        parts.append("Findings from current sources:")
        for src in state.sources:
            content = src.get("content", "")
            parts.append(f"- {content[:200]}")

        state.draft_report = "\n".join(parts)
        return state