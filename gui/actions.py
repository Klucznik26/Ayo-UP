import os
from pathlib import Path

from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from core.engine_manager import run_waifu2x
from core.model_manager import is_model_available
from gui.settings_dialog import SettingsDialog
from i18n import tr


class MainWindowActions:
    # ==================================================
    # OBRAZ
    # ==================================================
    def _open_image(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            tr("open_image"),
            "",
            "Images (*.png *.jpg *.jpeg *.webp)"
        )
        if path:
            self._load_image_from_path(path)

    def _load_image_from_path(self, path):
        self.input_image = path

        pixmap = QPixmap(path)
        self.preview_label.setPixmap(
            pixmap.scaled(
                self.preview_label.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )

        self._update_output_name()
        self._update_run_state()

    # ==================================================
    # KATALOG WYJŚCIOWY
    # ==================================================
    def _choose_output_dir(self):
        path = QFileDialog.getExistingDirectory(
            self,
            tr("select_output")
        )
        if path:
            self.output_dir = path
            self._update_run_state()

    # ==================================================
    # STAN / UI
    # ==================================================
    def _update_output_name(self):
        if not self.input_image:
            self.output_name_label.setText("—")
            return

        base, ext = os.path.splitext(os.path.basename(self.input_image))
        scale = self.scale_controller.get()

        name = f"{base}_AUPx{scale}{ext}"
        self.output_name_label.setText(name)

    def _update_run_state(self):
        has_image = bool(self.input_image)
        has_output = bool(self.output_dir)
        has_model = is_model_available()

        can_run = has_image and has_output and has_model
        self.btn_run.setEnabled(can_run)

        if not has_output:
            message = tr("tooltip_select_output")
        elif not has_image:
            message = tr("tooltip_select_image")
        elif not has_model:
            message = tr("no_model")
        else:
            message = ""

        self.btn_run.setToolTip(message)
        self.model_status_label.setText(message)

    # ==================================================
    # UPSCALING
    # ==================================================
    def _run_upscale(self):
        if not self.input_image or not self.output_dir:
            return

        input_path = Path(self.input_image)
        base, ext = os.path.splitext(input_path.name)
        scale = self.scale_controller.get()

        output_path = Path(self.output_dir) / f"{base}_AUPx{scale}{ext}"

        try:
            self.btn_run.setEnabled(False)
            self.model_status_label.setText(tr("processing"))

            run_waifu2x(
                input_image=input_path,
                output_image=output_path,
                scale=scale,
            )

            self.model_status_label.setText(tr("done"))

        except Exception as e:
            self.model_status_label.setText(f"{tr('error')}: {e}")

        finally:
            self._update_run_state()

    # ==================================================
    # USTAWIENIA
    # ==================================================
    def _open_settings(self):
        dialog = SettingsDialog(self)
        dialog.exec()
        self.retranslate_ui()
        self._update_run_state()

