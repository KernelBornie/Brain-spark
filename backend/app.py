from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="BrainSpark Q&A")

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample question-answer function
def get_answer(question: str) -> str:
    qa_dict = {
        "Hello!": "Hello! I’m really happy to help you with your questions.",
        "What is Python?": "Python is a high-level programming language.",
        "Tell me a fun fact about space.": "Did you know that space is silent because there is no atmosphere to carry sound?",
    }
    return qa_dict.get(question, "Sorry, I don't know the answer to that.")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("frontend/index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@app.post("/ask")
async def ask_question(data: dict):
    question = data.get("query", "")
    answer = get_answer(question)
    return JSONResponse(content={"question": question, "answer": answer})
