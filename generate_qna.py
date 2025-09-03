import json

data = {}

# Generate 10,000 Q&A pairs
for i in range(1, 10001):
    question = f"question {i}"
    answer = f"This is the answer for question {i}."
    data[question] = answer

# Save to backend/data/sample_questions.json
with open("backend/data/sample_questions.json", "w") as f:
    json.dump(data, f, indent=2)

print("✅ 10,000 Q&A file generated at backend/data/sample_questions.json")
