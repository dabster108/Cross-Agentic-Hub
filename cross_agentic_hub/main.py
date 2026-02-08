from fastapi import FastAPI
from config import APP_NAME
from agents.planner import PlannerAgent
from agents.coder import CoderAgent
from agents.validator import ValidatorAgent

# Create FastAPI app
app = FastAPI(title=APP_NAME)

# Initialize agents
planner_agent = PlannerAgent()
coder_agent = CoderAgent()
validator_agent = ValidatorAgent()

# Root endpoint
@app.get("/")
def root():
    return {"message": f"Welcome to {APP_NAME}!"}

# Task endpoint
@app.post("/task")
def create_task(task: dict):
    """
    Receives a task like:
    {"goal": "Build a todo app with FastAPI"}
    """
    goal = task.get("goal")
    plan = planner_agent.plan(goal)
    code = coder_agent.generate_code(plan)
    validation = validator_agent.validate(code)

    return {
        "goal": goal,
        "plan": plan,
        "generated_code": code,
        "validation": validation
    }
