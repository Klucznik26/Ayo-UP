import subprocess
import tempfile
from pathlib import Path

from core.up_image_upscale_models import get_active_model_config


def is_engine_available() -> bool:
    try:
        _name, engine_bin, model_dir = get_active_model_config()
    except RuntimeError:
        return False
    return engine_bin.exists() and model_dir.exists()


def run_single_pass(engine_bin: Path, model_dir: Path, input_image: Path, output_image: Path) -> None:
    cmd = [
        str(engine_bin), '-i', str(input_image), '-o', str(output_image), '-s', '2', '-m', str(model_dir),
    ]
    subprocess.run(cmd, check=True)


def run_upscale_pipeline(input_image: str | Path, output_image: str | Path, scale: int) -> None:
    if scale not in (2, 4):
        raise RuntimeError(f'Unsupported scale: {scale}')
    _name, engine_bin, model_dir = get_active_model_config()
    input_path = Path(input_image).resolve()
    output_path = Path(output_image).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if scale == 2:
        run_single_pass(engine_bin, model_dir, input_path, output_path)
        return
    with tempfile.TemporaryDirectory(prefix='ayoup-x4-') as temp_dir:
        temp_output = Path(temp_dir) / f'{input_path.stem}_x2{input_path.suffix}'
        run_single_pass(engine_bin, model_dir, input_path, temp_output)
        run_single_pass(engine_bin, model_dir, temp_output, output_path)
