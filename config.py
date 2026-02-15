import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env
load_dotenv()

APP_NAME = os.getenv("APP_NAME", "CrossAgenticHub")
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8000))
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

# API Keys - Google Gemini only
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# LLM Configuration for CrewAI
LLM_MODEL = os.getenv("LLM_MODEL", "gemini-2.5-flash-lite")
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.7"))

# Database configuration
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://neondb_owner:npg_7gtqkuHF4LXb@ep-patient-rice-ai7k18a9-pooler.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
)

# Initialize LLM for CrewAI agents (using Gemini)
def get_llm():
    """Returns configured LLM instance using Google Gemini"""
    if not GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY is not set. Please check your .env file.")
        
    return ChatGoogleGenerativeAI(
        model=LLM_MODEL,
        google_api_key=GOOGLE_API_KEY,
        temperature=LLM_TEMPERATURE,
        convert_system_message_to_human=True
    )
