class ToolRegistry:
    """Stores and manages JARVIS tools."""

    def __init__(self):
        self.tools = {}

    def register(self, name, function):
        self.tools[name] = function

    def execute(self, name, *args, **kwargs):
        if name not in self.tools:
            return f"Tool '{name}' is not available."

        return self.tools[name](*args, **kwargs)

    def list_tools(self):
        return list(self.tools.keys())