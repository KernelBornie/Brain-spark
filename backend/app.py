# backend/app.py
from fastapi import FastAPI
from pydantic import BaseModel

class Question(BaseModel):
    query: str

app = FastAPI(title="BrainSpark AI")

@app.post("/ask")
async def ask_question(question: Question):
    # Simple mock AI response
    return {"query": question.query, "answer": f"BrainSpark thinks: {question.query[::-1]}"}
