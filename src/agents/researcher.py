from src.agents.base import BaseAgent
from src.state import ResearchState
from src.rag.retriever import Retriever
from src.tools.registry import ToolRegistry


class ResearchAgent(BaseAgent):
    name = "researcher"

    def __init__(self):
        self.retriever = Retriever()
        self.tools = ToolRegistry()

    def run(self, state: ResearchState) -> ResearchState:
        local_sources = self.retriever.query(state.query, n_results=3)

        selected_tool = self.tools.select_tool(state.query)
        tool_result = self.tools.call(selected_tool, state.query)
        tool_source = {
            "id": f"tool_{selected_tool}",
            "content": tool_result,
            "relevance_score": None,
            "source_type": "tool_call",
            "tool_used": selected_tool,
        }

        state.sources = local_sources + [tool_source]
        return state