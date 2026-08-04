from abc import ABC, abstractmethod
from src.state import ResearchState

class BaseAgent(ABC):
    name: str = "base_agent"

    @abstractmethod
    def run(self, state: ResearchState) -> ResearchState:
        """Takes the current state, does its job, returns updated state."""
        pass