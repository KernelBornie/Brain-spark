from fastapi import FastAPI
from app import BrainSparkAI

app = FastAPI()
brain_ai = BrainSparkAI()

@app.get("/")
def read_root():
    return {"message": "BrainSpark API is running!"}

@app.post("/ask")
def ask_question(question: str):
    answer = brain_ai.get_answer(question)
    return {"question": question, "answer": answer}
