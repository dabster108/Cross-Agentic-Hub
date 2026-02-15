from crewai import Task


def create_planning_task(agent, goal: str):
    """Creates a planning task for the Planner Agent"""
    return Task(
        description=(
            f"Analyze the following goal and break it down into clear, actionable steps:\n\n"
            f"Goal: {goal}\n\n"
            f"Provide a detailed step-by-step plan that covers:\n"
            f"1. Understanding the requirements\n"
            f"2. Identifying necessary components\n"
            f"3. Defining the implementation sequence\n"
            f"4. Considering edge cases and error handling\n\n"
            f"Format your plan as a numbered list with clear descriptions."
        ),
        agent=agent,
        expected_output="A detailed numbered list of actionable steps to achieve the goal"
    )


def create_coding_task(agent, goal: str, plan_context: str = ""):
    """Creates a coding task for the Coder Agent"""
    context_section = f"\n\nPlan to follow:\n{plan_context}" if plan_context else ""
    
    return Task(
        description=(
            f"Generate clean, production-ready Python code for the following goal:\n\n"
            f"Goal: {goal}{context_section}\n\n"
            f"Requirements:\n"
            f"- Write clean, well-documented code with docstrings\n"
            f"- Follow PEP 8 style guidelines\n"
            f"- Include proper error handling\n"
            f"- Add comments for complex logic\n"
            f"- Make the code modular and reusable\n\n"
            f"Provide the complete Python code."
        ),
        agent=agent,
        expected_output="Complete, well-documented Python code that implements the goal"
    )


def create_validation_task(agent, code_context: str):
    """Creates a validation task for the Validator Agent"""
    return Task(
        description=(
            f"Review the following Python code for correctness, security, and best practices:\n\n"
            f"```python\n{code_context}\n```\n\n"
            f"Check for:\n"
            f"1. Syntax errors and logical bugs\n"
            f"2. Security vulnerabilities\n"
            f"3. Performance issues\n"
            f"4. Code style and best practices\n"
            f"5. Error handling completeness\n"
            f"6. Edge cases coverage\n\n"
            f"If issues are found, provide:\n"
            f"- List of identified issues\n"
            f"- Severity of each issue (Critical/High/Medium/Low)\n"
            f"- Fixed version of the code\n\n"
            f"If the code is good, confirm its quality and highlight strengths."
        ),
        agent=agent,
        expected_output="Detailed code review with identified issues and fixes, or confirmation of code quality"
    )


def create_summarization_task(agent, chat_history: list):
    """Creates a summarization task for the Summarizer Agent"""
    chat_text = "\n".join(chat_history) if isinstance(chat_history, list) else str(chat_history)
    
    return Task(
        description=(
            f"Summarize the following conversation or chat history:\n\n"
            f"{chat_text}\n\n"
            f"Provide:\n"
            f"1. A concise summary in bullet points\n"
            f"2. Key decisions or conclusions\n"
            f"3. Extract and list any code snippets mentioned\n"
            f"4. Highlight any action items or next steps\n"
        ),
        agent=agent,
        expected_output="Structured summary with bullets, key points, code snippets, and action items"
    )
