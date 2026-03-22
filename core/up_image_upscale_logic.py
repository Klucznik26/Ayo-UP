import os
from pathlib import Path

from core.up_image_upscale_models import (
    get_active_model_name,
    get_model_names,
    install_model_archive,
    set_active_model_name,
)
from core.up_image_upscale_pipeline import is_engine_available, run_upscale_pipeline
from core.up_settings_logic import SettingsLogic


class ImageUpscaleLogic:
    IMG_EXTS = ('.png', '.jpg', '.jpeg', '.webp')

    @staticmethod
    def is_model_ready() -> bool:
        return is_engine_available()

    @staticmethod
    def get_model_names() -> list[str]:
        return get_model_names()

    @staticmethod
    def get_active_model_name() -> str:
        return get_active_model_name()

    @staticmethod
    def set_active_model(name: str) -> None:
        set_active_model_name(name)

    @staticmethod
    def install_model(zip_path: Path) -> str:
        return install_model_archive(zip_path)

    @staticmethod
    def filter_valid_images(paths: list[str]) -> list[str]:
        valid_images = []
        for path in paths:
            if os.path.isdir(path):
                for root, _, files in os.walk(path):
                    for file_name in files:
                        if file_name.lower().endswith(ImageUpscaleLogic.IMG_EXTS):
                            valid_images.append(os.path.join(root, file_name))
            elif path.lower().endswith(ImageUpscaleLogic.IMG_EXTS):
                valid_images.append(path)
        return sorted(set(valid_images))

    @staticmethod
    def build_output_path(input_path: str, output_dir: str, scale: int) -> str:
        input_resolved = Path(input_path).resolve()
        output_name = f'{input_resolved.stem}_AUPx{scale}{input_resolved.suffix}'
        return str((Path(output_dir) / output_name).resolve())

    @staticmethod
    def processing_message(current: int, total: int) -> str:
        return SettingsLogic.tr('processing').format(current, total)

    @staticmethod
    def process_single_image(input_path: str, output_dir: str, scale: int) -> str:
        output_path = ImageUpscaleLogic.build_output_path(input_path, output_dir, scale)
        run_upscale_pipeline(input_path, output_path, scale)
        return output_path
