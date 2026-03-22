from PySide6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QWidget

from core.up_batch_logic import BatchLogic
from core.up_image_upscale_logic import ImageUpscaleLogic
from gui.up_file_drop_ui import FileDropUI
from gui.up_image_upscale_ui import ImageUpscaleUI
from gui.up_preview_ui import PreviewUI
from gui.up_settings_ui import SettingsUI


class MainUI(QMainWindow):
    VERSION = '1.7.0'

    def __init__(self):
        super().__init__()
        self.input_files = []
        self.setMinimumSize(1050, 700)
        self.resize(1050, 700)
        central = QWidget(); self.setCentralWidget(central)
        layout = QHBoxLayout(central); layout.setContentsMargins(10, 10, 10, 10); layout.setSpacing(10)
        self.settings_ui = SettingsUI(self)
        self.image_upscale_ui = ImageUpscaleUI(self)
        self.file_drop_ui = FileDropUI(self)
        self.preview_ui = PreviewUI(self)
        layout.addWidget(self.settings_ui); layout.addWidget(self.image_upscale_ui); layout.addWidget(self.file_drop_ui); layout.addWidget(self.preview_ui)
        self.settings_ui.close_requested.connect(self.close)
        self.settings_ui.language_changed.connect(self.retranslate_ui)
        self.file_drop_ui.files_dropped.connect(self._load)
        self.image_upscale_ui.files_requested.connect(self._load)
        self.image_upscale_ui.run_requested.connect(self._run)
        self.preview_ui.file_list.currentRowChanged.connect(self._on_file_selected)
        self.retranslate_ui()

    def retranslate_ui(self):
        self.setWindowTitle(f'AyoUP {self.VERSION}')
        self.settings_ui.retranslate_ui(); self.image_upscale_ui.retranslate_ui(); self.file_drop_ui.retranslate_ui(); self.preview_ui.retranslate_ui()

    def _load(self, paths):
        valid = ImageUpscaleLogic.filter_valid_images(paths)
        if not valid:
            return
        self.input_files = valid
        self.preview_ui.update_files(valid)
        self.image_upscale_ui.set_ready_state(bool(valid) and ImageUpscaleLogic.is_model_ready())
        self.image_upscale_ui.clear_status()

    def _run(self, scale, output_dir):
        if not self.input_files:
            return
        total = len(self.input_files)
        self.image_upscale_ui.set_ready_state(False)
        self.image_upscale_ui.btn_run.set_progress(0, total)
        self.settings_ui.setDisabled(True)
        errors = BatchLogic.run(self.input_files, output_dir, scale, self._progress)
        self.image_upscale_ui.btn_run.reset_progress()
        self.settings_ui.setDisabled(False)
        self.file_drop_ui.reset_preview(); self.preview_ui.clear_files(completed=True)
        self.input_files = []
        if errors:
            self.image_upscale_ui.show_status('\n'.join(errors[:3]))
        else:
            self.image_upscale_ui.clear_status()

    def _progress(self, index, total, _path):
        self.image_upscale_ui.btn_run.set_progress(index, total)
        self.image_upscale_ui.show_status(ImageUpscaleLogic.processing_message(index, total))
        QApplication.processEvents()
        if index < len(self.input_files):
            self.file_drop_ui.preview_label.set_next_pixmap(self.file_drop_ui.preview_label.pixmap())
        self.file_drop_ui.preview_label.apply_next_image()

    def _on_file_selected(self, index):
        if 0 <= index < len(self.input_files):
            self.file_drop_ui.show_preview(self.input_files[index])
