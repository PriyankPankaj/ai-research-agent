from src.tools.base import BaseTool
from duckduckgo_search import DDGS

class WebSearchTool(BaseTool):
    name = "web_search"
    description = "Searches the web and returns top result snippets for a query."

    def run(self, input_text: str) -> str:
        try:
            with DDGS() as ddgs:
                results = list(ddgs.text(input_text, max_results=3))
            if not results:
                return "No web results found."
            formatted = []
            for r in results:
                formatted.append(f"- {r.get('title', '')}: {r.get('body', '')}")
            return "\n".join(formatted)
        except Exception as e:
            return f"Web search error: {str(e)}"