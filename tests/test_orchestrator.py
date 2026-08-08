import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.orchestrator import Orchestrator
from src.state import ResearchState


def test_orchestrator_runs_end_to_end():
    orchestrator = Orchestrator()
    result = orchestrator.run("What is coral bleaching?")

    assert isinstance(result, ResearchState)
    assert result.is_complete is True
    assert result.draft_report is not None
    assert len(result.draft_report) > 0


def test_orchestrator_populates_sources():
    orchestrator = Orchestrator()
    result = orchestrator.run("What is coral bleaching?")

    assert len(result.sources) > 0