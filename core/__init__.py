from pathlib import Path

APP_NAME = "ayo-up"

CONFIG_DIR = Path.home() / ".config" / APP_NAME
DATA_DIR   = Path.home() / ".local" / "share" / APP_NAME
MODELS_DIR = DATA_DIR / "models"
