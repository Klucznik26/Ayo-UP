import os
from pathlib import Path

from PySide6.QtWidgets import QFileDialog, QApplication
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QEventLoop

from core.engine_manager import run_waifu2x
from core.model_manager import is_model_available
from gui.settings_dialog import SettingsDialog
from i18n import tr
from config.settings import load_settings, save_settings


class MainWindowActions:
    IMG_EXTS = (".png", ".jpg", ".jpeg", ".webp")

    # ==================================================
    # OBRAZ
    # ==================================================
    def _open_files_dialog(self):
        filters = f"{tr('filter_images')} (*.png *.jpg *.jpeg *.webp)"
        paths, _ = QFileDialog.getOpenFileNames(
            self,
            tr("open_files"),
            "",
            filters,
            options=QFileDialog.DontUseNativeDialog
        )
        if paths:
            self._load_images(paths)

    def _open_folder_dialog(self):
        path = QFileDialog.getExistingDirectory(
            self,
            tr("open_folder"),
            "",
            options=QFileDialog.DontUseNativeDialog
        )
        if path:
            self._load_images([path])

    def _load_images(self, paths):
        """
        Ładuje obrazy z podanej listy ścieżek (plików lub folderów).
        """
        valid_images = []

        for p in paths:
            if os.path.isdir(p):
                # Skanowanie folderu
                for root, _, files in os.walk(p):
                    for f in files:
                        if f.lower().endswith(self.IMG_EXTS):
                            valid_images.append(os.path.join(root, f))
            elif p.lower().endswith(self.IMG_EXTS):
                valid_images.append(p)

        if not valid_images:
            return

        self.input_files = sorted(list(set(valid_images)))  # Unikalne i posortowane

        # Podgląd pierwszego obrazu
        if self.input_files:
            first_img = self.input_files[0]
            pixmap = QPixmap(first_img)
            self.preview_label.setPixmap(
                pixmap.scaled(
                    self.preview_label.size(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
            )

        # Obsługa wachlarza miniatur (tylko dla > 1 pliku)
        if len(self.input_files) > 1:
            self.fan_widget.set_images(self.input_files)
            self.fan_widget.show()
        else:
            self.fan_widget.hide()

        self._update_output_name()
        self._update_run_state()

    # ==================================================
    # KATALOG WYJŚCIOWY
    # ==================================================
    def _choose_output_dir(self):
        path = QFileDialog.getExistingDirectory(
            self,
            tr("select_output"),
            "",
            options=QFileDialog.DontUseNativeDialog
        )
        if path:
            self.output_dir = path
            settings = load_settings()
            settings["output_dir"] = path
            save_settings(settings)
            self._update_run_state()

    # ==================================================
    # STAN / UI
    # ==================================================
    def _update_output_name(self):
        count = len(self.input_files)

        if count > 1:
            self.output_name_label.setText(tr("files_selected").format(count))
            self.output_name_label.show()
        else:
            self.output_name_label.hide()

    def _update_run_state(self):
        has_files = bool(self.input_files)
        has_model = is_model_available()

        # Przycisk aktywny, gdy mamy pliki i model.
        # Katalog wyjściowy można wybrać po kliknięciu.
        can_run = has_files and has_model
        self.btn_run.setEnabled(can_run)

        if not has_files:
            message = ""
        elif not has_model:
            message = tr("no_model")
        elif not self.output_dir:
            message = tr("tooltip_select_output")
        else:
            message = ""

        self.btn_run.setToolTip(message)
        self.model_status_label.setText(message)
        self.model_status_label.setVisible(bool(message))

    # ==================================================
    # UPSCALING
    # ==================================================
    def _run_upscale(self):
        if not self.input_files:
            return

        if not self.output_dir:
            self._choose_output_dir()
            if not self.output_dir:
                return

        scale = self.scale_controller.get()
        total = len(self.input_files)
        errors = []
        success_count = 0

        self.btn_run.setEnabled(False)
        self.btn_close.setEnabled(False)
        self.btn_run.set_progress(0, total)
        self.model_status_label.show()
        
        # Upewnij się, że pierwszy obraz jest poprawnie załadowany do podglądu
        if self.input_files:
            first_pix = QPixmap(self.input_files[0]).scaled(
                self.preview_label.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            self.preview_label.setPixmap(first_pix)
            self.preview_label.set_rotation(0)

        for i, file_path in enumerate(self.input_files, 1):
            self.model_status_label.setText(tr("processing").format(i, total))
            QApplication.processEvents()  # Odśwież UI

            try:
                input_path = Path(file_path).resolve()
                # Użycie pathlib do budowania nazwy pliku (czyściej i szybciej)
                output_filename = f"{input_path.stem}_AUPx{scale}{input_path.suffix}"
                output_path = (Path(self.output_dir) / output_filename).resolve()

                run_waifu2x(
                    input_image=str(input_path),
                    output_image=str(output_path),
                    scale=int(scale),
                )

                if not output_path.exists():
                    errors.append(file_path)
                else:
                    success_count += 1

            except Exception:
                errors.append(file_path)
            
            self.btn_run.set_progress(i, total)

            # =========================
            # ANIMACJA PRZEJŚCIA
            # =========================
            # Przygotuj następny obraz (jeśli istnieje)
            if i < len(self.input_files):
                next_path = self.input_files[i] # i to indeks następnego (bo enumerate od 1)
                next_pix = QPixmap(next_path).scaled(
                    self.preview_label.size(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
                self.preview_label.set_next_pixmap(next_pix)
            
            # Uruchom animację i czekaj na jej koniec
            loop = QEventLoop()
            anim = self.preview_label.animate_discard()
            anim.finished.connect(loop.quit)
            anim.start()
            loop.exec() # Blokuje pętlę for, ale pozwala działać GUI

            # Po animacji: podmień obraz na wierzchu
            self.preview_label.apply_next_image()

        self.btn_run.reset_progress()
        self.btn_close.setEnabled(True)

        # Reset UI po zakończeniu
        self.input_files = []
        self.preview_label.clear()
        self.preview_label.setText(tr("completed"))
        self.fan_widget.hide()
        self._update_output_name()
        self._update_run_state()
        
        if errors:
            self.model_status_label.setText(tr("done_errors").format(success_count, total, len(errors)))
            self.model_status_label.show()
        else:
            self.model_status_label.clear()
            self.model_status_label.hide()

    # ==================================================
    # USTAWIENIA
    # ==================================================
    def _open_settings(self):
        dialog = SettingsDialog(self)
        dialog.exec()
        self.retranslate_ui()
        self._update_run_state()
