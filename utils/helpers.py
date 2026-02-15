import os
import requests
from config import MISTRAL_API_KEY

MISTRAL_URL = "https://api.mistral.ai/v1/generate"


def call_mistral(prompt: str, max_tokens=500):
    """Legacy function for calling Mistral API directly"""
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


def load_chat(session_id: str):
    """
    Load chat history from database or storage based on session_id
    
    Args:
        session_id: Unique session identifier
    
    Returns:
        List of chat messages or None if not found
    """
    # TODO: Implement actual database retrieval
    # For now, return mock data or empty list
    from database.models import get_session_history
    
    try:
        history = get_session_history(session_id)
        return history
    except Exception as e:
        print(f"Error loading chat history: {e}")
        return None

