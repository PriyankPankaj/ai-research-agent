from src.tools.registry import ToolRegistry

registry = ToolRegistry()
print(registry.call("calculator", "12 * (4 + 3)"))
print(registry.select_tool("What is 25 * 4?"))
print(registry.select_tool("latest news on AI"))
print(registry.select_tool("What are coral reefs?"))