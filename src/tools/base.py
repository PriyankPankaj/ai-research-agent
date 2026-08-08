from abc import ABC, abstractmethod


class BaseTool(ABC):
    name: str = "base_tool"
    description: str = "Base tool interface"

    @abstractmethod
    def run(self, input_text: str) -> str:
        """Execute the tool with the given input, return a text result."""
        pass

    def describe(self) -> dict:
        """Metadata used for tool selection (keyword-based today, LLM
        function-calling schema-compatible later)."""
        return {
            "name": self.name,
            "description": self.description,
        }