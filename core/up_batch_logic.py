from core.up_image_upscale_logic import ImageUpscaleLogic


class BatchLogic:
    @staticmethod
    def run(paths: list[str], output_dir: str, scale: int, progress=None) -> list[str]:
        errors = []
        total = len(paths)
        for index, path in enumerate(paths, 1):
            if progress is not None:
                progress(index, total, path)
            try:
                ImageUpscaleLogic.process_single_image(path, output_dir, scale)
            except Exception as exc:
                errors.append(f'{path}: {exc}')
        return errors
