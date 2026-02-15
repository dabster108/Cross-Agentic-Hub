from crewai import Agent
from config import get_llm


def create_planner_agent():
    """Creates and returns a CrewAI Planner Agent"""
    return Agent(
        role="Task Planner",
        goal="Break down complex goals into clear, actionable steps",
        backstory=(
            "You are an expert project planner with years of experience in software development. "
            "You excel at analyzing requirements and creating detailed execution plans that are "
            "easy to follow and implement. You always consider edge cases and best practices."
        ),
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )
