from src.agents.base import BaseAgent
from src.state import ResearchState


class WriterAgent(BaseAgent):
    name = "writer"

    def run(self, state: ResearchState) -> ResearchState:
        report_lines = []
        report_lines.append(f"# Research Report: {state.query}\n")

        # --- Related past findings (from memory) ---
        if state.memory_context:
            report_lines.append("## Related Prior Research\n")
            for mem in state.memory_context:
                report_lines.append(
                    f"- From a previous session on *\"{mem['original_query']}\"* "
                    f"(relevance: {mem['relevance_score']:.2f}): "
                    f"{mem['content'][:150]}..."
                )
            report_lines.append("")

        # --- Main findings with numbered citations ---
        report_lines.append("## Findings\n")
        citations = []

        for i, src in enumerate(state.sources, start=1):
            content = src.get("content", "")
            source_type = src.get("source_type", "vector_store")
            report_lines.append(f"{content} [{i}]")
            report_lines.append("")

            citations.append({
                "index": i,
                "id": src.get("id", "unknown"),
                "type": source_type,
                "preview": content[:100],
            })

        # --- Citations section ---
        report_lines.append("## Sources\n")
        for c in citations:
            report_lines.append(f"[{c['index']}] ({c['type']}) {c['id']}: {c['preview']}...")

        state.draft_report = "\n".join(report_lines)
        state.extracted_notes = [c["preview"] for c in citations]  # simple traceability
        return state