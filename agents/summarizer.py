from crewai import Agent, Task, Crew
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


def run_summary(chat_text: str):
    """
    Runs the summarizer agent on the provided chat text
    
    Args:
        chat_text: The conversation text to summarize
    
    Returns:
        Summary output from the agent
    """
    summarizer_agent = create_summarizer_agent()
    
    # Create a task for summarization
    summary_task = Task(
        description=(
            f"Summarize the following conversation:\n\n{chat_text}\n\n"
            f"Provide:\n"
            f"1. A concise summary in bullet points\n"
            f"2. Key topics discussed\n"
            f"3. Any code snippets or technical details mentioned\n"
            f"4. Action items or next steps if any\n"
        ),
        agent=summarizer_agent,
        expected_output="Structured summary with bullets, key topics, and code snippets"
    )
    
    # Create and run the crew
    crew = Crew(
        agents=[summarizer_agent],
        tasks=[summary_task],
        verbose=True
    )
    
    result = crew.kickoff()
    
    return result 
