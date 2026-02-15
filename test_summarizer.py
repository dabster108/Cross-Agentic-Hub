# test_summarizer.py
"""
Test file to verify the Summarizer Agent (CrewAI + Mistral)
"""

from agents.summarizer import run_summary

# Example chat input
chat_text = """
User: How do I create a FastAPI endpoint?
Assistant: You need FastAPI, define app = FastAPI(), and create @app.get routes...
User: Can you also show database integration?
Assistant: Sure! Use SQLAlchemy to define models and connect them to your endpoints.
User: And how do I organize multiple agents?
Assistant: Use CrewAI to orchestrate planner, coder, validator, summarizer agents in a pipeline.
"""

# Run summarizer agent
summary = run_summary(chat_text)

# Print the structured summary
print("----- SUMMARY OUTPUT -----")
print(summary)
