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

MODELS_CONFIG = load_yaml(BASE_DIR / "config" / "models.yaml")

PROMPTS_DIR = BASE_DIR / "prompts"

# COR_PROMPT = PROMPTS_DIR / f"correction_prompt_{VERSION['PROMPT_VERSION']}.txt"
# COM_PROMPT = PROMPTS_DIR / f"completion_prompt_{VERSION['PROMPT_VERSION']}.txt"
# OT_PROMPT = PROMPTS_DIR / f"off_topic_prompt_{VERSION['PROMPT_VERSION']}.txt"
# REF_PROMPT = PROMPTS_DIR / f"reformulation_prompt_{VERSION['PROMPT_VERSION']}.txt"