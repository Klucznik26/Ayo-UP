from pathlib import Path
import shutil
import zipfile

from config.settings import load_settings, save_settings


MODELS_DIR = Path.home() / '.local' / 'share' / 'ayo-up' / 'models'
KNOWN_ENGINE_NAMES = {
    'waifu2x-ncnn-vulkan',
    'realesrgan-ncnn-vulkan',
    'realcugan-ncnn-vulkan',
}


def ensure_model_dirs() -> None:
    MODELS_DIR.mkdir(parents=True, exist_ok=True)


def find_engine_binary(model_dir: Path) -> Path | None:
    for path in sorted(model_dir.rglob('*')):
        if path.is_file() and path.name in KNOWN_ENGINE_NAMES and path.stat().st_mode & 0o111:
            return path
    return None


def find_model_directories(model_dir: Path) -> list[Path]:
    return sorted(
        path for path in model_dir.rglob('*')
        if path.is_dir() and path.name.startswith('models')
    )


def is_runnable_model(model_dir: Path) -> bool:
    return find_engine_binary(model_dir) is not None and bool(find_model_directories(model_dir))


def get_model_directories() -> list[Path]:
    ensure_model_dirs()
    return [path for path in sorted(MODELS_DIR.iterdir()) if path.is_dir() and is_runnable_model(path)]


def get_model_names() -> list[str]:
    return [path.name for path in get_model_directories()]


def get_active_model_name() -> str:
    names = get_model_names()
    if not names:
        return ''
    settings = load_settings()
    active = settings.get('active_model', '')
    if active in names:
        return active
    active = names[0]
    settings['active_model'] = active
    save_settings(settings)
    return active


def set_active_model_name(name: str) -> None:
    if name not in get_model_names():
        return
    settings = load_settings()
    settings['active_model'] = name
    save_settings(settings)


def get_active_model_config() -> tuple[str, Path, Path]:
    active_name = get_active_model_name()
    if not active_name:
        raise RuntimeError('No runnable models installed')
    model_dir = MODELS_DIR / active_name
    engine_bin = find_engine_binary(model_dir)
    model_dirs = find_model_directories(model_dir)
    if engine_bin is None or not model_dirs:
        raise RuntimeError(f'Active model {active_name} is not runnable')
    return active_name, engine_bin, model_dirs[0]


def install_model_archive(zip_path: Path) -> str:
    ensure_model_dirs()
    model_name = zip_path.stem
    target_dir = MODELS_DIR / model_name
    if target_dir.exists():
        shutil.rmtree(target_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    try:
        with zipfile.ZipFile(zip_path, 'r') as archive:
            archive.extractall(target_dir)
    except Exception:
        shutil.rmtree(target_dir, ignore_errors=True)
        raise
    if not is_runnable_model(target_dir):
        shutil.rmtree(target_dir, ignore_errors=True)
        raise ValueError(
            'The ZIP does not contain a runnable NCNN/Vulkan upscaler with an executable binary and model directory.'
        )
    set_active_model_name(model_name)
    return model_name
