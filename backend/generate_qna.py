import json

# Generate 10,000 sample questions and answers
sample_qna = [
    {"question": f"sample question {i}", "answer": f"sample answer {i}"}
    for i in range(1, 10001)
]

# Save to backend/data/sample_questions.json
with open("backend/data/sample_questions.json", "w") as f:
    json.dump(sample_qna, f, indent=4)

print("Generated 10,000 Q&A pairs successfully!")
