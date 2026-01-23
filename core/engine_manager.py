import subprocess
from pathlib import Path

BASE_DIR = Path.home() / ".local" / "share" / "ayo-up" / "models" / "waifu2x"
ENGINE_BIN = BASE_DIR / "waifu2x-ncnn-vulkan"
MODEL_DIR = BASE_DIR / "models-cunet"


def is_engine_available() -> bool:
    return ENGINE_BIN.exists() and MODEL_DIR.exists()


def run_waifu2x(
    input_image: Path,
    output_image: Path,
    scale: int,
):
    if not is_engine_available():
        raise RuntimeError("Waifu2x engine or model not found")

    # waifu2x OBSŁUGUJE TYLKO x1 lub x2
    if scale not in (1, 2, 4):
        raise RuntimeError(f"Unsupported scale: {scale}")

    # cunet → tylko x2, x1
    if scale == 4:
        raise RuntimeError("Scale x4 requires two-pass upscaling (not implemented yet)")

    cmd = [
        str(ENGINE_BIN),
        "-i", str(input_image),
        "-o", str(output_image),
        "-s", "2",
        "-m", str(MODEL_DIR),
    ]

    subprocess.run(cmd, check=True)

