from crewai import Agent
from config import get_llm


def create_summarizer_agent():
    """Creates and returns a CrewAI Summarizer Agent"""
    return Agent(
        role="Technical Writer & Summarizer",
        goal="Summarize conversations and extract key information including code blocks",
        backstory=(
            "You are an expert technical writer who excels at distilling complex conversations "
            "into concise, actionable summaries. You have a keen eye for identifying important "
            "details, decisions made, and code snippets. You present information in a clear, "
            "structured format that makes it easy to understand what happened in a conversation."
        ),
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )


def run_summary(chat_text : str):
     summarizer_agent = create_summarizer_agent()
     result = summarizer_agent.run(task=f"Summarize this chat:\n{chat_text}")

     return result 
