# Cross-Agentic Hub

A multi-agent system that uses AI agents to break down tasks, generate code, and validate solutions.

## Agents

- **Planner Agent**: Breaks down goals into actionable steps
- **Coder Agent**: Generates Python code based on the plan
- **Validator Agent**: Checks and validates generated code
- **Summarizer Agent**: Summarizes conversations and extracts code blocks

## Tech Stack

- FastAPI backend
- Mistral AI for agent intelligence
- PostgreSQL database for storage

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn main:app --reload
```
