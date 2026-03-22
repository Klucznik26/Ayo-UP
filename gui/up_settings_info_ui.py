from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout, QWidget

from core.up_settings_logic import SettingsLogic


class SettingsInfoUI(QDialog):
    def __init__(self, version, parent=None):
        super().__init__(parent)
        self.version = version
        self.setWindowTitle(self._text('info_title', 'About Ayo UP'))
        self.setFixedSize(450, 680)
        self.setStyleSheet(
            """
            QDialog { background-color: #1a1b26; }
            QLabel { color: #e0af68; font-family: 'Segoe UI'; }
            QLabel#Section { font-size: 15px; font-weight: bold; margin-top: 15px; }
            QLabel#Text { font-size: 12px; }
            QPushButton {
                background-color: #24283b; color: #e0af68;
                border: 1px solid #e0af68; padding: 10px; border-radius: 4px; font-weight: bold;
            }
            """
        )
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 20)
        self.banner = QLabel()
        self._load_banner()
        layout.addWidget(self.banner)
        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(25, 10, 25, 10)
        self._add_info_block(
            content_layout,
            self._text('info_name_up', f'Ayo UP v {self.version}'),
            self._text('info_desc_up', 'Powerful upscaler using neural networks to enlarge photos x2 and x4.'),
        )
        layout.addWidget(content)
        layout.addStretch()
        self.btn_close = QPushButton(self._text('info_btn_close', 'Back'))
        self.btn_close.clicked.connect(self.accept)
        btn_layout = QVBoxLayout()
        btn_layout.setContentsMargins(25, 0, 25, 0)
        btn_layout.addWidget(self.btn_close)
        layout.addLayout(btn_layout)

    def _text(self, key, fallback):
        value = SettingsLogic.tr(key)
        return fallback if value == key else value

    def _add_info_block(self, layout, title_text, body_text):
        title = QLabel(title_text)
        title.setObjectName('Section')
        body = QLabel(body_text)
        body.setObjectName('Text')
        body.setWordWrap(True)
        layout.addWidget(title)
        layout.addWidget(body)

    def _load_banner(self):
        path = Path(__file__).resolve().parent.parent / 'assets' / 'Ayo.png'
        if path.exists():
            pixmap = QPixmap(str(path))
            if not pixmap.isNull():
                self.banner.setPixmap(pixmap.scaled(450, 250, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation))
