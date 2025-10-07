import os
from pathlib import Path
from dotenv import load_dotenv
from config.utils import load_yaml

load_dotenv()

# Chemin racine du projet
BASE_DIR = Path(__file__).resolve().parents[1]

# Secrets
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Models config
MODELS_CONFIG = load_yaml(BASE_DIR / "config" / "models.yaml")

# Prompts files 
PROMPTS_DIR = BASE_DIR / "prompts"
PROMPTS = load_yaml(BASE_DIR / "config" / "prompts.yaml")
