from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from rag_chat import get_answer

app = FastAPI()

# Allow your website (running on a different address) to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {"status": "College Assistant API is running"}

@app.post("/chat")
def chat(request: ChatRequest):
    answer = get_answer(request.question)
    return {"answer": answer}