from crewai import Crew, Process
from agents.planner import create_planner_agent
from agents.coder import create_coder_agent
from agents.validator import create_validator_agent
from agents.summarizer import create_summarizer_agent
from crew.tasks import (
    create_planning_task,
    create_coding_task,
    create_validation_task,
    create_summarization_task
)


def run_crew(goal: str, workflow: str = "full"):
    """
    Orchestrates the CrewAI agents to complete a goal
    
    Args:
        goal: The user's goal or task description
        workflow: Type of workflow - "full" (plan->code->validate), "plan_only", "code_only"
    
    Returns:
        Dictionary with results from each agent
    """
    
    # Initialize agents
    planner = create_planner_agent()
    coder = create_coder_agent()
    validator = create_validator_agent()
    
    # Create tasks based on workflow type
    tasks = []
    agents = []
    
    if workflow == "full":
        # Full workflow: Planning -> Coding -> Validation
        planning_task = create_planning_task(planner, goal)
        tasks.append(planning_task)
        agents.append(planner)
        
        coding_task = create_coding_task(coder, goal)
        coding_task.context = [planning_task]  # Coding task uses planning output
        tasks.append(coding_task)
        agents.append(coder)
        
        # Create validation task that uses coding output
        validation_task = Task(
            description=(
                f"Review the generated code for the goal: {goal}\n\n"
                f"Check for correctness, security, and best practices.\n"
                f"Provide detailed feedback and fixes if needed."
            ),
            agent=validator,
            context=[coding_task],
            expected_output="Code review with issues identified and fixes provided"
        )
        tasks.append(validation_task)
        agents.append(validator)
        
    elif workflow == "plan_only":
        planning_task = create_planning_task(planner, goal)
        tasks.append(planning_task)
        agents.append(planner)
        
    elif workflow == "code_only":
        coding_task = create_coding_task(coder, goal)
        tasks.append(coding_task)
        agents.append(coder)
    
    # Create and run the crew
    crew = Crew(
        agents=agents,
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )
    
    # Execute the crew
    result = crew.kickoff()
    
    return {
        "goal": goal,
        "workflow": workflow,
        "result": result,
        "tasks_completed": len(tasks)
    }


def run_summarizer_crew(chat_history: list):
    """
    Runs the summarizer agent on chat history
    
    Args:
        chat_history: List of chat messages or conversation text
    
    Returns:
        Summary of the conversation
    """
    
    # Initialize summarizer agent
    summarizer = create_summarizer_agent()
    
    # Create summarization task
    summary_task = create_summarization_task(summarizer, chat_history)
    
    # Create and run the crew
    crew = Crew(
        agents=[summarizer],
        tasks=[summary_task],
        process=Process.sequential,
        verbose=True
    )
    
    result = crew.kickoff()
    
    return {
        "summary": result,
        "messages_processed": len(chat_history) if isinstance(chat_history, list) else 1
    }


# Import Task here to avoid circular import
from crewai import Task
