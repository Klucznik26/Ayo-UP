from PySide6.QtGui import QColor, QPainter, QPainterPath
from PySide6.QtWidgets import QPushButton


class ImageUpscaleProgressUI(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._progress = 0
        self._total = 0

    def set_progress(self, current: int, total: int) -> None:
        self._progress = current
        self._total = total
        self.update()

    def reset_progress(self) -> None:
        self._progress = 0
        self._total = 0
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self._total <= 0 or self._progress <= 0:
            return
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        path = QPainterPath()
        path.addRoundedRect(self.rect(), 6, 6)
        painter.setClipPath(path)
        ratio = min(self._progress / self._total, 1.0)
        painter.setPen(0)
        painter.setBrush(QColor(255, 255, 255, 50))
        painter.drawRect(0, 0, int(self.width() * ratio), self.height())
