import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

APP_NAME = os.getenv("APP_NAME", "CrossAgenticHub")
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8000))
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# LLM Configuration for CrewAI
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4")
LLM_BASE_URL = os.getenv("LLM_BASE_URL", None)  # For OpenAI-compatible endpoints
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.7"))

# Database configuration
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://neondb_owner:npg_7gtqkuHF4LXb@ep-patient-rice-ai7k18a9-pooler.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
)

# Initialize LLM for CrewAI agents
def get_llm():
    """Returns configured LLM instance for CrewAI agents"""
    if LLM_BASE_URL:
        return ChatOpenAI(
            model=LLM_MODEL,
            base_url=LLM_BASE_URL,
            api_key=OPENAI_API_KEY or MISTRAL_API_KEY,
            temperature=LLM_TEMPERATURE
        )
    return ChatOpenAI(
        model=LLM_MODEL,
        api_key=MISTRAL_API_KEY or OPENAI_API_KEY,
        temperature=LLM_TEMPERATURE
    )
