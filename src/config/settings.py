from pathlib import Path
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# LLM Configuration
LLM_CONFIG = {
    "model_name": "meta-llama/Llama-3.3-70B-Instruct",
    "api_key": os.getenv("HUGGINGFACE_API_KEY"),
    "max_new_tokens": 500,
    "temperature": 0.7,
    "context_length": 2048,
}

# Game Configuration
GAME_CONFIG = {
    "max_history_length": 10,
    "default_character_stats": {
        "health": 100,
        "mana": 100,
        "strength": 10,
        "intelligence": 10,
    }
}

# API Configuration
API_CONFIG = {
    "host": "0.0.0.0",
    "port": 8000,
    "debug": True,
}