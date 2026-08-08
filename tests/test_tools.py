import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.tools.registry import ToolRegistry


def test_calculator_tool():
    registry = ToolRegistry()
    result = registry.call("calculator", "2 + 2")
    assert result == "4"


def test_tool_selection_routes_math_to_calculator():
    registry = ToolRegistry()
    selected = registry.select_tool("What is 10 * 5?")
    assert selected == "calculator"


def test_tool_selection_routes_general_to_wikipedia():
    registry = ToolRegistry()
    selected = registry.select_tool("What are coral reefs?")
    assert selected == "wikipedia_search"


def test_unknown_tool_returns_error_message():
    registry = ToolRegistry()
    result = registry.call("nonexistent_tool", "test")
    assert "not found" in result.lower()