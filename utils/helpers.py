import os
import requests
from config import MISTRAL_API_KEY

MISTRAL_URL = "https://api.mistral.ai/v1/generate"

def call_mistral(prompt: str, max_tokens=500):
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "max_tokens": max_tokens
    }
    response = requests.post(MISTRAL_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["text"]
    else:
        return f"Error: {response.text}"
