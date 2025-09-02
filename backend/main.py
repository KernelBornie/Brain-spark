from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Model path (put your model files here)
model_name = "models"

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    question = data.get("query", "")
    return {
        "question": question,
        "answer": f"🤖 BrainSpark says: I understood your question '{question}'! (This is a sample answer.)"
    }
