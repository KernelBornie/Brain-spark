import requests
import json

URL = "http://127.0.0.1:8000/ask"

# Load sample questions
with open("sample_questions.json", "r") as f:
    questions = json.load(f)

# Send each question and print the answer
for q in questions:
    response = requests.post(URL, json=q)
    if response.status_code == 200:
        print("Q:", q["query"])
        print("A:", response.json()["answer"])
        print("-" * 50)
    else:
        print("Failed for question:", q["query"])
        print("Status code:", response.status_code)
