import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

APP_NAME = os.getenv("APP_NAME", "AgenticApp")
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8000))
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Database configuration
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://neondb_owner:npg_7gtqkuHF4LXb@ep-patient-rice-ai7k18a9-pooler.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
)
