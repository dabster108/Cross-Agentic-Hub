from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from config import APP_NAME
from crew.orchestrator import run_crew, run_summarizer_crew


app = FastAPI(title=APP_NAME)


# Request models
class TaskRequest(BaseModel):
    goal: str
    workflow: str = "full"  # Options: "full", "plan_only", "code_only"


class SummaryRequest(BaseModel):
    session_id: str
    chat_history: list = None  # Optional: provide directly instead of loading


@app.get("/")
def root():
    return {
        "message": f"Welcome to {APP_NAME}!",
        "endpoints": {
            "POST /task": "Execute CrewAI workflow for a given goal",
            "POST /get_summary": "Get AI-generated summary of chat history",
            "GET /health": "Health check"
        }
    }


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": APP_NAME}


@app.post("/task")
def create_task(request: TaskRequest):
    """
    Execute CrewAI agents to complete a task
    
    - **goal**: The task or goal description
    - **workflow**: Type of workflow (full, plan_only, code_only)
    """
    try:
        result = run_crew(goal=request.goal, workflow=request.workflow)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error executing task: {str(e)}")


@app.post("/get_summary")
def get_summary(request: SummaryRequest):
    """
    Get AI-generated summary of chat history
    
    - **session_id**: Session identifier for loading chat history
    - **chat_history**: Optional - provide chat history directly
    """
    try:
        chat_history = request.chat_history
        
        # If no chat_history provided, try to load from session_id
        if not chat_history:
            from utils.helpers import load_chat
            chat_history = load_chat(request.session_id)
            
            if not chat_history:
                raise HTTPException(
                    status_code=404, 
                    detail=f"No chat history found for session: {request.session_id}"
                )
        
        summary_result = run_summarizer_crew(chat_history)
        return {
            "session_id": request.session_id,
            **summary_result
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating summary: {str(e)}")

