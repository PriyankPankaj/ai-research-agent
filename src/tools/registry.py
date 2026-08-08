from src.tools.wikipedia_tool import WikipediaSearchTool
from src.tools.calculator_tool import CalculatorTool
from src.tools.web_search_tool import WebSearchTool


class ToolRegistry:
    def __init__(self):
        self._tools = {}
        self.register(WikipediaSearchTool())
        self.register(CalculatorTool())
        self.register(WebSearchTool())

    def register(self, tool):
        self._tools[tool.name] = tool

    def get(self, tool_name: str):
        return self._tools.get(tool_name)

    def list_tools(self) -> list[dict]:
        return [tool.describe() for tool in self._tools.values()]

    def call(self, tool_name: str, input_text: str) -> str:
        tool = self.get(tool_name)
        if tool is None:
            return f"Tool '{tool_name}' not found."
        return tool.run(input_text)

    def select_tool(self, query: str) -> str:
        """Simple keyword-based tool selection.
        NOTE: this is an interim heuristic. Once an LLM is wired in (post-v1
        roadmap item), this should be replaced with real function-calling
        where the model picks the tool based on `describe()` metadata."""
        lowered = query.lower()
        if any(ch.isdigit() for ch in query) and any(op in query for op in ["+", "-", "*", "/", "^"]):
            return "calculator"
        if any(word in lowered for word in ["latest", "news", "current", "recent", "today"]):
            return "web_search"
        return "wikipedia_search"