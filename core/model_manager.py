from pathlib import Path
import shutil

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


def install_model_from_path(source: Path) -> None:
    """
    Kopiuje pliki modelu do katalogu aplikacji.
    source może być:
    - katalogiem
    - pojedynczym plikiem
    """
    if source.is_dir():
        # Walidacja: sprawdzamy czy w katalogu jest plik wykonywalny
        has_exe = any(
            f.is_file() and "ncnn-vulkan" in f.name
            for f in source.iterdir()
        )
        if not has_exe:
            raise ValueError("Wybrany katalog nie zawiera pliku wykonywalnego upscalera (ncnn-vulkan).")

        # Czyszczenie starej wersji przed instalacją nowej
        if ENGINE_DIR.exists():
            shutil.rmtree(ENGINE_DIR)
        ensure_model_dirs()

        for item in source.iterdir():
            target = ENGINE_DIR / item.name
            if item.is_dir():
                shutil.copytree(item, target, dirs_exist_ok=True)
            else:
                shutil.copy2(item, target)

    elif source.is_file():
        ensure_model_dirs()
        shutil.copy2(source, ENGINE_DIR / source.name)

    else:
        raise ValueError("Nieprawidłowa ścieżka modelu")
