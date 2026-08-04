from src.state import ResearchState
from src.agents.planner import PlannerAgent
from src.agents.researcher import ResearchAgent
from src.agents.reader import ReaderAgent
from src.agents.writer import WriterAgent
from src.agents.critic import CriticAgent

class Orchestrator:
    def __init__(self):
        self.pipeline = [
            PlannerAgent(),
            ResearchAgent(),
            ReaderAgent(),
            WriterAgent(),
            CriticAgent(),
        ]

    def run(self, query: str) -> ResearchState:
        state = ResearchState(query=query)
        for agent in self.pipeline:
            print(f"Running: {agent.name}")
            state = agent.run(state)
        return state


if __name__ == "__main__":
    orchestrator = Orchestrator()
    final_state = orchestrator.run("What are the effects of climate change on coral reefs?")
    print(final_state)