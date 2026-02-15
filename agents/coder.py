from crewai import Agent
from config import get_llm


def create_coder_agent():
    """Creates and returns a CrewAI Coder Agent"""
    return Agent(
        role="Senior Python Developer",
        goal="Generate clean, efficient, and well-documented Python code",
        backstory=(
            "You are a senior Python developer with expertise in writing production-ready code. "
            "You follow PEP 8 guidelines, write comprehensive docstrings, handle errors gracefully, "
            "and always consider performance and maintainability. You excel at translating plans "
            "into working code that is both elegant and robust."
        ),
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )
