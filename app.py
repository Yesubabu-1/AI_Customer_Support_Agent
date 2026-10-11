from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from orchestrator import AIOrchestrator

app = FastAPI(
    title="Multi-Agent Customer Support AI",
    version="2.0.0",
    description="Customer Support AI using Multi-Agent Architecture, RAG and Gemini"
)

orchestrator = AIOrchestrator()



class QuestionRequest(BaseModel):
    customer_name: str = "Anonymous"
    question: str


class FeedbackRequest(BaseModel):
    rating: int
    comment: str


class TicketStatusRequest(BaseModel):
    status: str




@app.get("/")
def home():

    return {
        "message": "Multi-Agent Customer Support AI Running"
    }




@app.get("/health")
def health():

    return {
        "status": "UP",
        "application": "Customer Support AI",
        "version": "2.0.0"
    }




@app.post("/ask")
def ask(request: QuestionRequest):

    try:

        return orchestrator.process_query(
            question=request.question,
            customer_name=request.customer_name
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )




@app.get("/tickets")
def get_tickets():

    return orchestrator.get_all_tickets()


@app.get("/ticket/{ticket_id}")
def get_ticket(ticket_id: str):

    ticket = orchestrator.get_ticket(ticket_id)

    if ticket is None:

        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return ticket


@app.patch("/ticket/{ticket_id}")
def update_ticket(
        ticket_id: str,
        request: TicketStatusRequest
):

    ticket = orchestrator.update_ticket_status(
        ticket_id,
        request.status
    )

    if ticket is None:

        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return ticket



@app.post("/feedback")
def submit_feedback(
        request: FeedbackRequest
):

    return orchestrator.submit_feedback(
        request.rating,
        request.comment
    )


@app.get("/feedback")
def feedback_stats():

    return orchestrator.get_feedback_statistics()




@app.get("/memory")
def memory():

    return orchestrator.memory_agent.load_memory()


@app.delete("/memory")
def clear_memory():

    orchestrator.memory_agent.clear_memory()

    return {
        "message": "Conversation memory cleared."
    }