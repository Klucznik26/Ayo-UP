import os

from PySide6.QtGui import QColor, QPixmap, Qt
from PySide6.QtWidgets import QFrame, QGraphicsDropShadowEffect, QLabel, QListWidget, QSizePolicy, QVBoxLayout

from core.up_settings_logic import SettingsLogic
from gui.up_preview_widgets import PreviewFanUI


class PreviewUI(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('rightPanel')
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumWidth(260)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(30); shadow.setOffset(0, 6); shadow.setColor(QColor(0, 0, 0, 60))
        self.setGraphicsEffect(shadow)
        layout = QVBoxLayout(self); layout.setContentsMargins(10, 10, 10, 10); layout.setSpacing(10)
        glass = 'QFrame { background-color: rgba(150,150,150,0.1); border-radius: 12px; border: 1px solid rgba(150,150,150,0.15); }'
        self.top_glass = QFrame(); self.top_glass.setStyleSheet(glass)
        self.mid_glass = QFrame(); self.mid_glass.setStyleSheet(glass)
        self.bottom_glass = QFrame(); self.bottom_glass.setStyleSheet(glass)
        self.fan_ui = PreviewFanUI(); self.fan_ui.hide()
        fan_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding); fan_policy.setRetainSizeWhenHidden(True); self.fan_ui.setSizePolicy(fan_policy)
        self.out_name = QLabel(); self.out_name.setProperty('secondary', True); self.out_name.hide()
        self.file_list = QListWidget(); self.file_list.setStyleSheet('QListWidget { background: transparent; border: none; outline: none; } QListWidget::item { padding: 4px 8px; border-radius: 6px; }')
        self.logo_label = QLabel(); self.logo_label.setAlignment(Qt.AlignCenter); self._load_logo()
        top_layout = QVBoxLayout(self.top_glass); top_layout.addWidget(self.fan_ui); top_layout.addWidget(self.out_name, 0, Qt.AlignCenter)
        mid_layout = QVBoxLayout(self.mid_glass); mid_layout.addWidget(self.file_list)
        bottom_layout = QVBoxLayout(self.bottom_glass); bottom_layout.addWidget(self.logo_label, 0, Qt.AlignCenter)
        layout.addWidget(self.top_glass, 1); layout.addWidget(self.mid_glass, 2); layout.addWidget(self.bottom_glass, 1)

    def _load_logo(self):
        logo_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'AyoUP.png')
        pixmap = QPixmap(logo_path)
        if not pixmap.isNull():
            self.logo_label.setPixmap(pixmap.scaled(120, 120, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def update_files(self, paths: list[str]):
        self.file_list.clear()
        for path in paths:
            self.file_list.addItem(os.path.basename(path))
        if self.file_list.count() > 0:
            self.file_list.setCurrentRow(0)
        if len(paths) > 1:
            self.out_name.setText(SettingsLogic.tr('files_selected').format(len(paths)))
            self.out_name.show(); self.fan_ui.set_images(paths); self.fan_ui.show()
        else:
            self.out_name.hide(); self.fan_ui.hide()

    def clear_files(self, completed=False):
        self.file_list.clear(); self.fan_ui.hide()
        if completed:
            self.out_name.setText(SettingsLogic.tr('completed')); self.out_name.show()
        else:
            self.out_name.clear(); self.out_name.hide()

    def retranslate_ui(self):
        if self.out_name.isVisible() and self.file_list.count() > 1:
            self.out_name.setText(SettingsLogic.tr('files_selected').format(self.file_list.count()))
