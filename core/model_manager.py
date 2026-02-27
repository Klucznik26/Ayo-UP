from pathlib import Path
import shutil
import zipfile

from core.paths import MODELS_DIR


ENGINE_NAME = "waifu2x"
ENGINE_DIR = MODELS_DIR / ENGINE_NAME


def ensure_model_dirs():
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    ENGINE_DIR.mkdir(parents=True, exist_ok=True)


def is_model_available() -> bool:
    if not ENGINE_DIR.exists():
        return False
    return any(ENGINE_DIR.iterdir())


def get_model_names() -> list[str]:
    """
    Zwraca listę nazw dostępnych modeli (nazwy podkatalogów).
    """
    ensure_model_dirs()
    return [d.name for d in MODELS_DIR.iterdir() if d.is_dir()]


def set_active_model(name: str) -> None:
    """
    Ustawia aktywny model poprzez aktualizację globalnych zmiennych.
    """
    global ENGINE_NAME, ENGINE_DIR
    ENGINE_NAME = name
    ENGINE_DIR = MODELS_DIR / name


def install_model_from_zip(zip_path: Path) -> None:
    """
    Rozpakowuje archiwum ZIP do nowego katalogu w folderze modeli.
    Nazwa katalogu będzie taka sama jak nazwa pliku ZIP (bez rozszerzenia).
    """
    model_name = zip_path.stem
    target_dir = MODELS_DIR / model_name

    # Jeśli katalog już istnieje, czyścimy go
    if target_dir.exists():
        shutil.rmtree(target_dir)
    target_dir.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(target_dir)
