from PySide6.QtCore import Signal
from PySide6.QtGui import QColor, Qt, QPixmap
from PySide6.QtWidgets import QFrame, QGraphicsDropShadowEffect, QSizePolicy, QVBoxLayout

from core.up_settings_logic import SettingsLogic
from gui.up_file_drop_widgets import FileDropImageUI


class FileDropUI(QFrame):
    files_dropped = Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('rightPanel')
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(30); shadow.setOffset(0, 6); shadow.setColor(QColor(0, 0, 0, 60))
        self.setGraphicsEffect(shadow)
        layout = QVBoxLayout(self); layout.setContentsMargins(15, 15, 15, 15)
        self.preview_label = FileDropImageUI(on_drop=self.files_dropped.emit)
        self.preview_label.setObjectName('dropArea')
        self.preview_label.setAlignment(Qt.AlignCenter)
        self.preview_label.setWordWrap(True)
        self.preview_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        layout.addWidget(self.preview_label, 0, Qt.AlignCenter)
        self.retranslate_ui()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        height = event.size().height(); drop_height = height - 30
        if drop_height > 0:
            drop_width = int(drop_height * (2 / 3))
            panel_width = drop_width + 30
            if self.width() != panel_width:
                self.setFixedWidth(panel_width)
            self.preview_label.setFixedSize(drop_width, drop_height)

    def show_preview(self, image_path: str):
        pixmap = QPixmap(image_path).scaled(self.preview_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.preview_label.setPixmap(pixmap)
        self.preview_label.set_rotation(0)

    def reset_preview(self):
        self.preview_label.clear()
        self.preview_label.setText(SettingsLogic.tr('completed'))

    def retranslate_ui(self):
        if not self.preview_label.pixmap() or self.preview_label.pixmap().isNull():
            if self.preview_label.text() != SettingsLogic.tr('completed'):
                self.preview_label.setText(SettingsLogic.tr('open_image'))
