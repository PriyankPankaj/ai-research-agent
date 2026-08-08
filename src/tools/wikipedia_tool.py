import wikipedia
from src.tools.base import BaseTool


class WikipediaSearchTool(BaseTool):
    name = "wikipedia_search"
    description = "Looks up a topic on Wikipedia and returns a summary."

    def _extract_search_term(self, query: str) -> str:
        try:
            results = wikipedia.search(query, results=1)
            if results:
                return results[0]
        except Exception:
            pass
        return query

    def run(self, input_text: str) -> str:
        search_term = self._extract_search_term(input_text)
        try:
            summary = wikipedia.summary(search_term, sentences=3, auto_suggest=False)
            return summary
        except wikipedia.exceptions.DisambiguationError as e:
            try:
                summary = wikipedia.summary(e.options[0], sentences=3, auto_suggest=False)
                return summary
            except Exception:
                return f"Ambiguous topic. Options included: {', '.join(e.options[:5])}"
        except wikipedia.exceptions.PageError:
            return f"No Wikipedia page found for '{search_term}'."
        except Exception as e:
            # Wikipedia API is occasionally unreliable (network/rate-limit issues).
            # Fail gracefully instead of crashing the pipeline.
            return f"Wikipedia lookup temporarily unavailable — continuing without this source."