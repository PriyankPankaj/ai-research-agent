from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel
from src.memory.session_store import init_db, create_session, get_session
from src.orchestrator import Orchestrator

app = FastAPI(title="AutoLab AI")
orchestrator = Orchestrator()


@app.on_event("startup")
def startup():
    init_db()


class ResearchRequest(BaseModel):
    query: str


@app.post("/research")
def start_research(request: ResearchRequest, background_tasks: BackgroundTasks):
    session_id = create_session(request.query)
    background_tasks.add_task(orchestrator.run_and_persist, session_id, request.query)
    return {"session_id": session_id, "status": "pending"}


@app.get("/research/{session_id}")
def get_research(session_id: str):
    session = get_session(session_id)
    if session is None:
        raise HTTPException(status_code=404, detail="Session not found")
    return session