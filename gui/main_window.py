import os

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QMenu,
    QApplication,
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from gui.widgets import DropImageLabel, FanPreviewWidget, ProgressButton
from gui.actions import MainWindowActions
from gui.scale import ScaleController
from gui.settings_dialog import SettingsDialog
from themes import ThemeManager

from core.model_manager import ensure_model_dirs
from config.settings import load_settings
from i18n import tr


class MainWindow(QMainWindow, MainWindowActions):
    def __init__(self):
        super().__init__()

        # =========================
        # STAN PODSTAWOWY
        # =========================
        self.input_files = []
        settings = load_settings()
        self.output_dir = settings.get("output_dir", "")

        ensure_model_dirs()

        # =========================
        # OKNO
        # =========================
        self.setFixedSize(870, 550)

        central = QWidget()
        self.setCentralWidget(central)

        root_layout = QHBoxLayout(central)
        root_layout.setContentsMargins(10, 20, 10, 20)
        root_layout.setSpacing(15)

        # ==================================================
        # LEWA KOLUMNA
        # ==================================================
        left_container = QWidget()
        left_container.setFixedWidth(240)
        left_panel = QVBoxLayout(left_container)
        left_panel.setContentsMargins(0, 0, 0, 0)
        left_panel.setSpacing(8)

        self.btn_open = QPushButton()
        
        # Menu dla przycisku (Pliki / Folder)
        self.open_menu = QMenu(self)
        self.act_files = self.open_menu.addAction("Files")
        self.act_folder = self.open_menu.addAction("Folder")
        self.act_files.triggered.connect(self._open_files_dialog)
        self.act_folder.triggered.connect(self._open_folder_dialog)
        self.btn_open.setMenu(self.open_menu)
        
        left_panel.addWidget(self.btn_open)

        self.btn_output = QPushButton()
        self.btn_output.clicked.connect(self._choose_output_dir)
        left_panel.addWidget(self.btn_output)

        left_panel.addStretch()

        # ==================================================
        # SKALA (x2 / x4)
        # ==================================================
        self.scale_controller = ScaleController(left_panel)

        # ==================================================
        # WYKONAJ
        # ==================================================
        self.btn_run = ProgressButton()
        self.btn_run.setObjectName("runButton")
        self.btn_run.setFixedHeight(60)
        self.btn_run.clicked.connect(self._run_upscale)
        left_panel.addWidget(self.btn_run)

        self.model_status_label = QLabel("")
        self.model_status_label.setAlignment(Qt.AlignCenter)
        self.model_status_label.setProperty("secondary", True)
        left_panel.addWidget(self.model_status_label)

        left_panel.addStretch()

        # ==================================================
        # DOLNE PRZYCISKI
        # ==================================================
        bottom = QHBoxLayout()

        self.btn_settings = QPushButton()
        self.btn_settings.clicked.connect(self._open_settings)

        self.btn_close = QPushButton()
        self.btn_close.clicked.connect(self.close)

        bottom.addWidget(self.btn_settings)
        bottom.addWidget(self.btn_close)

        left_panel.addLayout(bottom)
        root_layout.addWidget(left_container)

        # ==================================================
        # PODGLĄD OBRAZU
        # ==================================================
        preview_frame = QFrame()
        preview_layout = QVBoxLayout(preview_frame)

        self.preview_label = DropImageLabel(
            on_drop=self._load_images
        )
        self.preview_label.setAlignment(Qt.AlignCenter)
        preview_layout.addWidget(self.preview_label)

        root_layout.addWidget(preview_frame, 3)

        # ==================================================
        # PRAWY PANEL (Wachlarz + Logo)
        # ==================================================
        right_panel = QVBoxLayout()
        right_container = QWidget()
        right_container.setFixedWidth(220)
        right_panel = QVBoxLayout(right_container)
        right_panel.setContentsMargins(0, 0, 0, 0)

        # Wachlarz (Góra)
        self.fan_widget = FanPreviewWidget()
        self.fan_widget.hide()
        right_panel.addWidget(self.fan_widget, alignment=Qt.AlignTop | Qt.AlignRight)

        self.output_name_label = QLabel("")
        self.output_name_label.setProperty("secondary", True)
        self.output_name_label.setAlignment(Qt.AlignRight)
        self.output_name_label.setContentsMargins(0, 0, 25, 0)
        self.output_name_label.hide()
        right_panel.addWidget(self.output_name_label, alignment=Qt.AlignTop | Qt.AlignRight)

        right_panel.addStretch()

        # Logo (Dół)
        logo_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "assets",
            "AyoUP.png"
        )

        logo = QLabel()
        pixmap = QPixmap(logo_path)
        logo.setPixmap(
            pixmap.scaled(
                120,
                120,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )
        logo.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        right_panel.addWidget(logo, alignment=Qt.AlignBottom | Qt.AlignRight)

        root_layout.addWidget(right_container)

        # =========================
        # FINALIZACJA
        # =========================
        self.retranslate_ui()
        self._update_run_state()

    # ==================================================
    # USTAWIENIA
    # ==================================================
    def _open_settings(self):
        dialog = SettingsDialog(self)
        dialog.exec()

        # 🔥 PRZEŁADOWANIE MOTYWU RUNTIME
        ThemeManager.apply(QApplication.instance())

        self.retranslate_ui()
        self._update_run_state()

    # ==================================================
    # I18N
    # ==================================================
    def retranslate_ui(self):
        self.setWindowTitle(f"{tr('app_title')} v 1.0.1")
        self.btn_open.setText(tr("open_image"))
        self.act_files.setText(tr("open_files"))
        self.act_folder.setText(tr("open_folder"))
        self.btn_output.setText(tr("select_output"))
        self.btn_run.setText(tr("run"))
        self.btn_close.setText(tr("exit"))
        self.btn_settings.setText(tr("settings"))
        self.scale_controller.retranslate()
