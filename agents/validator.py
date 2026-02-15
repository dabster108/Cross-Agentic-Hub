from crewai import Agent
from config import get_llm


def create_validator_agent():
    """Creates and returns a CrewAI Validator Agent"""
    return Agent(
        role="Code Quality Reviewer",
        goal="Review code for correctness, security, and best practices, providing fixes when needed",
        backstory=(
            "You are a meticulous code reviewer with deep expertise in Python and software security. "
            "You have an eye for catching bugs, security vulnerabilities, and code smells. "
            "You provide constructive feedback and suggest improvements that make code more "
            "maintainable, efficient, and secure. You always test edge cases mentally."
        ),
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )
