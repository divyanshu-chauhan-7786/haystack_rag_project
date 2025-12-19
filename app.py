from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv

# Import your RAG function
from QASystem.retrievalgeneration import get_response

load_dotenv()

app = FastAPI(title="RAG Application")

# ✅ Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


# -------------------------
# Home Page (UI)
# -------------------------
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


# -------------------------
# API Schema
# -------------------------
class QuestionRequest(BaseModel):
    question: str


# -------------------------
# RAG API Endpoint
# -------------------------
@app.post("/ask")
async def ask_question(payload: QuestionRequest):
    try:
        answer = get_response(payload.question)
        return JSONResponse(
            content={"answer": answer}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )
