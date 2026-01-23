import json
from pathlib import Path
from .defaults import DEFAULT_SETTINGS

CONFIG_DIR = Path.home() / ".config" / "ayo-up"
CONFIG_FILE = CONFIG_DIR / "settings.json"


def load_settings() -> dict:
    if not CONFIG_FILE.exists():
        return DEFAULT_SETTINGS.copy()

    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return DEFAULT_SETTINGS.copy()

    return {**DEFAULT_SETTINGS, **data}


def save_settings(settings: dict) -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=2, ensure_ascii=False)
