# FastAPI & Python Fundamentals Guide

This repository serves as a practical learning journey transitioning into modern Python and FastAPI development. Below are the foundational concepts translated into practical Python backend code.

---

## 1. Syntax Basics & Whitespace

Unlike languages that rely on `{}` braces or `;` line endings, Python uses **strict 4-space indentation** to define scope blocks.

```python
# Correct Indentation
def read_root():
    return {"message": "Hello World"}

# Incorrect (Will throw an IndentationError)
def read_root():
return {"message": "Hello World"}
```

---

## 2. Conditional Statements & Loops

Python uses `elif` for "else if" logic and iterates over collections cleanly without needing explicit index counters.

```python
# Conditional Logic
role = "admin"

if role == "admin":
    access_level = 3
elif role == "moderator":
    access_level = 2
else:
    access_level = 1

# Loops (Iterating over API endpoints)
endpoints = ["/users", "/agents", "/logs"]

for endpoint in endpoints:
    print(f"Registering route: {endpoint}")
```

---

## 3. Arrays (Lists) & Multi-Dimensional Arrays

Python represents dynamic arrays using **Lists** (`[]`). Multi-dimensional arrays are created by nesting lists inside lists.

```python
# Standard List
active_user_ids = [101, 102, 103, 104]

# Multi-Dimensional List (Row x Column Matrix)
embedding_matrix = [
    [0.12, 0.45, 0.89],
    [0.99, 0.33, 0.11],
    [0.55, 0.66, 0.77]
]

# Accessing Row 1, Column 2 (Zero-indexed)
print(embedding_matrix[1][2])  # Output: 0.11
```

---

## 4. Array Management & List Comprehensions

List management includes built-in methods like `append()` and `pop()`. **List Comprehensions** provide a concise syntax for mapping and filtering arrays.

```python
token_counts = [120, 450, 80, 950, 310]

# Standard array operations
token_counts.append(500)             # Append to end
first_item = token_counts.pop(0)     # Remove and return item at index 0

# List Comprehension (Filter > 300 and multiply by 2)
high_tokens = [t * 2 for t in token_counts if t > 300]
print(high_tokens)  # Output: [900, 1900, 620, 1000]
```

---

## 5. Object-Oriented Programming: Inheritance & Subclasses

Inheritance is achieved by passing the parent class into the child class definition. The `super()` function calls methods from the parent class.

```python
class BaseModel:
    def __init__(self, record_id: int):
        self.record_id = record_id

    def save(self):
        print(f"Saving record {self.record_id} to database...")

class AgentModel(BaseModel):
    def __init__(self, record_id: int, name: str):
        super().__init__(record_id)  # Pass ID to parent constructor
        self.name = name

    def save(self):
        # Method Overriding
        print(f"Saving Agent '{self.name}' (ID: {self.record_id}) to vector database...")

agent = AgentModel(record_id=42, name="CodeReviewer")
agent.save()
```

---

## 6. Polymorphism

Python utilizes **Duck Typing** ("If it walks like a duck and quacks like a duck, it's a duck"). Polymorphic functions do not require explicit interface types as long as the objects share expected methods.

```python
class OpenAITool:
    def execute(self, task: str):
        return f"OpenAI performing: {task}"

class LocalLLMTool:
    def execute(self, task: str):
        return f"Local Llama performing: {task}"

def run_agent_task(tool, task: str):
    print(tool.execute(task))

run_agent_task(OpenAITool(), "Code analysis")
run_agent_task(LocalLLMTool(), "Code analysis")
```

---

## 7. Interfaces (Abstract Base Classes)

To enforce strict structural contracts across classes, Python uses the built-in `abc` (Abstract Base Class) module.

```python
from abc import ABC, abstractmethod

class ToolInterface(ABC):
    @abstractmethod
    def run_tool(self, payload: dict) -> str:
        """Subclasses must implement this method"""
        pass

class DatabaseSearchTool(ToolInterface):
    def run_tool(self, payload: dict) -> str:
        return f"Executing search for query: {payload.get('query')}"

# Note: Instantiating ToolInterface directly or an incomplete subclass will raise a TypeError.
```