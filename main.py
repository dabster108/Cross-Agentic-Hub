from fastapi import FastAPI
from config import APP_NAME
from agents.planner import PlannerAgent
from agents.coder import CoderAgent
from agents.validator import ValidatorAgent


app = FastAPI(title=APP_NAME)


planner_agent = PlannerAgent()
coder_agent = CoderAgent()
validator_agent = ValidatorAgent()


@app.get("/")
def root():
    return {"message": f"Welcome to {APP_NAME}!"}



@app.post("/task")
def create_task(task: dict):
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


@app.get("/get_summary")
def get_summary(session_id: str):
    from utils.helpers import load_chat  
    chat_history = load_chat(session_id)
    
    summary = summarizer_agent.summarize(chat_history)
    return {"summary": summary}
