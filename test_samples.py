# test_samples.py
import requests

url = "http://127.0.0.1:8000/ask"
data = {"query": "Hello BrainSpark!"}

response = requests.post(url, json=data)
print(response.json())
