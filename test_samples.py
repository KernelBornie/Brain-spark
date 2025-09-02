from app import BrainSparkAI

def test_answer():
    ai = BrainSparkAI()
    question = "What is 2 + 2?"
    answer = ai.get_answer(question)
    assert "2 + 2" in answer

test_answer()
print("Test passed!")
