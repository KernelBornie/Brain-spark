from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load Q&A data
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.json")

with open(DATA_FILE, "r", encoding="utf-8") as f:
    qa_data = json.load(f)

questions = [item["question"] for item in qa_data]
answers = [item["answer"] for item in qa_data]

# Setup TF-IDF vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

# Create FastAPI app
app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    user_question = data.get("question", "").lower()

    if not user_question:
        return {"answer": "Please enter a question."}

    # Transform user question
    user_vec = vectorizer.transform([user_question])
    similarities = cosine_similarity(user_vec, X).flatten()

    best_idx = similarities.argmax()
    best_score = similarities[best_idx]

    # Adjusted threshold for better matching
    if best_score > 0.45:
        return {"answer": answers[best_idx]}
    else:
        return {"answer": "Sorry, I don’t know the answer to that yet."}
