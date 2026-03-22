from pathlib import Path

from PySide6.QtCore import Signal
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QComboBox, QFileDialog, QFrame, QGraphicsDropShadowEffect, QHBoxLayout, QLabel, QMenu, QMessageBox, QPushButton, QVBoxLayout

from core.up_image_upscale_logic import ImageUpscaleLogic
from core.up_settings_logic import SettingsLogic
from gui.up_image_upscale_scale_ui import ImageUpscaleScaleUI
from gui.up_image_upscale_widgets import ImageUpscaleProgressUI


class ImageUpscaleUI(QFrame):
    files_requested = Signal(list)
    run_requested = Signal(int, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('leftPanel')
        self.setFixedWidth(200)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(30)
        shadow.setOffset(0, 6)
        shadow.setColor(QColor(0, 0, 0, 60))
        self.setGraphicsEffect(shadow)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 20, 15, 20)
        self.btn_open = QPushButton(); self.btn_open.setObjectName('runButton'); self.btn_open.setMinimumHeight(60)
        self.open_menu = QMenu(self)
        self.act_files = self.open_menu.addAction('Files')
        self.act_folder = self.open_menu.addAction('Folder')
        self.act_files.triggered.connect(lambda: self._request_files(False))
        self.act_folder.triggered.connect(lambda: self._request_files(True))
        self.btn_open.setMenu(self.open_menu)
        self.btn_output = QPushButton(); self.btn_output.setMinimumHeight(60); self.btn_output.clicked.connect(self._choose_output)
        self.status_label = QLabel(); self.status_label.setWordWrap(True); self.status_label.setProperty('secondary', True); self.status_label.hide()
        self.label_upscaler = QLabel()
        self.combo_upscaler = QComboBox(); self.combo_upscaler.currentTextChanged.connect(ImageUpscaleLogic.set_active_model)
        self.btn_add_model = QPushButton('+'); self.btn_add_model.setFixedSize(35, 35); self.btn_add_model.clicked.connect(self._install_model)
        model_layout = QHBoxLayout(); model_layout.addWidget(self.combo_upscaler); model_layout.addWidget(self.btn_add_model)
        layout.addWidget(self.btn_open); layout.addWidget(self.btn_output); layout.addWidget(self.status_label); layout.addWidget(self.label_upscaler); layout.addLayout(model_layout); layout.addStretch(1)
        self.scale_ui = ImageUpscaleScaleUI(layout)
        self.btn_run = ImageUpscaleProgressUI(); self.btn_run.setObjectName('runButton'); self.btn_run.setMinimumHeight(80); self.btn_run.clicked.connect(self._run); self.btn_run.setEnabled(False)
        layout.addWidget(self.btn_run)
        self.output_dir = SettingsLogic.get_output_dir()
        self.refresh_models()
        self.retranslate_ui()

    def refresh_models(self):
        names = ImageUpscaleLogic.get_model_names()
        current = ImageUpscaleLogic.get_active_model_name()
        self.combo_upscaler.blockSignals(True)
        self.combo_upscaler.clear(); self.combo_upscaler.addItems(names)
        if current in names:
            self.combo_upscaler.setCurrentText(current)
        self.combo_upscaler.blockSignals(False)
        self.combo_upscaler.setEnabled(bool(names))
        self.show_status('' if names else SettingsLogic.tr('no_model'))

    def set_ready_state(self, enabled: bool):
        self.btn_run.setEnabled(enabled)

    def show_status(self, message: str):
        self.status_label.setText(message)
        self.status_label.setVisible(bool(message))

    def clear_status(self):
        self.status_label.clear(); self.status_label.hide()

    def _request_files(self, is_folder):
        tr = SettingsLogic.tr
        if is_folder:
            path = QFileDialog.getExistingDirectory(self, tr('open_folder'), '', options=QFileDialog.DontUseNativeDialog)
            if path:
                self.files_requested.emit([path])
            return
        paths, _ = QFileDialog.getOpenFileNames(self, tr('open_files'), '', f"{tr('filter_images')} (*.png *.jpg *.jpeg *.webp)", options=QFileDialog.DontUseNativeDialog)
        if paths:
            self.files_requested.emit(paths)

    def _choose_output(self):
        path = QFileDialog.getExistingDirectory(self, SettingsLogic.tr('select_output'), '', options=QFileDialog.DontUseNativeDialog)
        if path:
            self.output_dir = path
            SettingsLogic.set_output_dir(path)

    def _run(self):
        if not self.output_dir:
            self._choose_output()
        if self.output_dir:
            self.run_requested.emit(self.scale_ui.get(), self.output_dir)

    def _install_model(self):
        tr = SettingsLogic.tr
        path, _ = QFileDialog.getOpenFileName(self, tr('select_model_dir'), '', f"{tr('filter_zip')} (*.zip);;{tr('filter_all_files')} (*)", options=QFileDialog.DontUseNativeDialog)
        if not path:
            return
        try:
            model_name = ImageUpscaleLogic.install_model(Path(path))
        except Exception as exc:
            QMessageBox.critical(self, tr('error'), f"{tr('model_error')}:\n{exc}")
            return
        self.refresh_models(); self.combo_upscaler.setCurrentText(model_name)
        QMessageBox.information(self, tr('app_title'), tr('model_success'))

    def retranslate_ui(self):
        tr = SettingsLogic.tr
        self.btn_open.setText(tr('open_image').replace(' ', '\n', 1))
        self.btn_output.setText(tr('select_output').replace(' ', '\n', 1))
        self.btn_run.setText(tr('run'))
        self.label_upscaler.setText(tr('select_upscaler'))
        self.act_files.setText(tr('open_files')); self.act_folder.setText(tr('open_folder'))
        self.btn_add_model.setToolTip(tr('load_upscaler'))
        self.scale_ui.retranslate_ui()
