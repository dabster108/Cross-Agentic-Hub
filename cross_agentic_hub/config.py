import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

APP_NAME = os.getenv("APP_NAME", "AgenticApp")
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8000))
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
