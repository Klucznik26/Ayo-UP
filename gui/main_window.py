import os

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QApplication,
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from gui.widgets import DropImageLabel
from gui.actions import MainWindowActions
from gui.scale import ScaleController
from gui.settings_dialog import SettingsDialog
from gui.themes import ThemeManager

from core.model_manager import ensure_model_dirs
from i18n import tr


class MainWindow(QMainWindow, MainWindowActions):
    def __init__(self):
        super().__init__()

        # =========================
        # STAN PODSTAWOWY
        # =========================
        self.input_image = None
        self.output_dir = None

        ensure_model_dirs()

        # =========================
        # OKNO
        # =========================
        self.setFixedSize(900, 550)

        central = QWidget()
        self.setCentralWidget(central)

        root_layout = QHBoxLayout(central)
        root_layout.setContentsMargins(20, 20, 20, 20)
        root_layout.setSpacing(20)

        # ==================================================
        # LEWA KOLUMNA
        # ==================================================
        left_panel = QVBoxLayout()
        left_panel.setSpacing(8)

        self.btn_open = QPushButton()
        self.btn_open.clicked.connect(self._open_image)
        left_panel.addWidget(self.btn_open)

        self.btn_output = QPushButton()
        self.btn_output.clicked.connect(self._choose_output_dir)
        left_panel.addWidget(self.btn_output)

        self.output_name_label = QLabel("—")
        self.output_name_label.setWordWrap(True)
        self.output_name_label.setProperty("secondary", True)
        left_panel.addWidget(self.output_name_label)

        left_panel.addStretch()

        # ==================================================
        # SKALA (x2 / x4)
        # ==================================================
        self.scale_controller = ScaleController(left_panel)

        # ==================================================
        # WYKONAJ
        # ==================================================
        self.btn_run = QPushButton()
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
        root_layout.addLayout(left_panel, 1)

        # ==================================================
        # PODGLĄD OBRAZU
        # ==================================================
        preview_frame = QFrame()
        preview_layout = QVBoxLayout(preview_frame)

        self.preview_label = DropImageLabel(
            on_drop=self._load_image_from_path
        )
        self.preview_label.setAlignment(Qt.AlignCenter)
        preview_layout.addWidget(self.preview_label)

        root_layout.addWidget(preview_frame, 3)

        # ==================================================
        # LOGO
        # ==================================================
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
        root_layout.addWidget(logo, alignment=Qt.AlignBottom)

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
        self.setWindowTitle(tr("app_title"))
        self.btn_open.setText(tr("open_image"))
        self.btn_output.setText(tr("select_output"))
        self.btn_run.setText(tr("run"))
        self.btn_close.setText(tr("exit"))
        self.btn_settings.setText(tr("settings"))
        self.scale_controller.retranslate()
