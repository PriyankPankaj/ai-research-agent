from src.state import ResearchState
from src.agents.planner import PlannerAgent
from src.agents.researcher import ResearchAgent
from src.agents.reader import ReaderAgent
from src.agents.writer import WriterAgent
from src.agents.critic import CriticAgent
from src.memory.session_store import update_session


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

    def run_and_persist(self, session_id: str, query: str) -> ResearchState:
        state = ResearchState(query=query)
        update_session(session_id, state, status="running")

        for agent in self.pipeline:
            print(f"Running: {agent.name}")
            state = agent.run(state)
            update_session(session_id, state, status="running")

        update_session(session_id, state, status="completed")
        return state


if __name__ == "__main__":
    orchestrator = Orchestrator()
    final_state = orchestrator.run("How does ocean warming affect coral bleaching?")
    print(final_state)