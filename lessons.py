# Conditional Statements
role = "admin"

if role == "admin":
    access_level = 3
elif role == "moderator":
    access_level = 2
else:
    access_level = 1

# Loops (Iterating over a list of API routes)
routes = ["/api/v1/users", "/api/v1/agents", "/api/v1/chat"]

for route in routes:
    print(f"Registering route: {route}")

# ==========================================================================

# Standard Array (List) of active user IDs
active_users = [101, 102, 103, 104]

# Multi-Dimensional Array (List of Lists)
# Imagine a grid representing an agent's memory matrix or coordinates
memory_matrix = [
    [0.12, 0.45, 0.89],
    [0.99, 0.33, 0.11],
    [0.55, 0.66, 0.77]
]

# Accessing a multi-dimensional item (Row 1, Column 2)
print(memory_matrix[1][2])  # Output: 0.11

# ==========================================================================

tokens = [120, 450, 80, 950, 310]

# Array Management: Adding and removing items
tokens.append(500)       # Adds to the end
removed_token = tokens.pop(0)  # Removes and returns item at index 0

# List Comprehension: Filter tokens greater than 300 and double them
# Equivalent to array_map + array_filter in other languages
expensive_tokens = [t * 2 for t in tokens if t > 300]
print(expensive_tokens)  # Output: [900, 1900, 620, 1000]

# ==========================================================================

# Parent Class
class BaseModel:
    def __init__(self, id: int):
        self.id = id

    def save(self):
        print(f"Saving record {self.id} to database...")

# Subclass (Inherits from BaseModel)
class AgentModel(BaseModel):
    def __init__(self, id: int, name: str):
        super().__init__(id)  # Call parent constructor
        self.name = name

    # Overriding a method
    def save(self):
        print(f"Saving AI Agent '{self.name}' with ID {self.id}...")

# Usage
agent = AgentModel(id=42, name="DataAnalyzer")
agent.save()  # Output: Saving AI Agent 'DataAnalyzer' with ID 42...

# ==========================================================================

class OpenAITool:
    def execute(self, query: str):
        return f"Executing query via OpenAI: {query}"

class LocalLLMTool:
    def execute(self, query: str):
        return f"Executing query via Local Llama 3: {query}"

# Polymorphic function: doesn't care what tool it is, as long as it has .execute()
def run_agent_workflow(tool, query: str):
    print(tool.execute(query))

# Usage
run_agent_workflow(OpenAITool(), "Analyze sales data")
run_agent_workflow(LocalLLMTool(), "Analyze sales data")

# ==========================================================================

from abc import ABC, abstractmethod

# Defining an Interface using ABC
class ToolInterface(ABC):
    @abstractmethod
    def run_tool(self, payload: dict) -> str:
        pass

# Implementing the Interface
class DatabaseSearchTool(ToolInterface):
    def run_tool(self, payload: dict) -> str:
        # Must implement run_tool or Python throws a TypeError on instantiation
        return "Searching database..."