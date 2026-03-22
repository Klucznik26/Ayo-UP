from PySide6.QtCore import Property, QEasingCurve, QPropertyAnimation
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QLabel


class FileDropImageUI(QLabel):
    def __init__(self, parent=None, on_drop=None):
        super().__init__(parent)
        self.on_drop = on_drop
        self.setAcceptDrops(True)
        self._rotation = 0.0
        self._next_pixmap = None

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        paths = [url.toLocalFile() for url in event.mimeData().urls()]
        if paths and self.on_drop:
            self.on_drop(paths)

    def get_rotation(self):
        return self._rotation

    def set_rotation(self, angle):
        self._rotation = angle
        self.update()

    rotation = Property(float, get_rotation, set_rotation)

    def set_next_pixmap(self, pixmap):
        self._next_pixmap = pixmap
        self.update()

    def apply_next_image(self):
        if self._next_pixmap:
            self.setPixmap(self._next_pixmap)
            self._next_pixmap = None
        else:
            self.clear()
        self._rotation = 0.0
        self.update()

    def animate_discard(self):
        animation = QPropertyAnimation(self, b'rotation')
        animation.setDuration(600)
        animation.setStartValue(0.0)
        animation.setEndValue(-90.0)
        animation.setEasingCurve(QEasingCurve.InBack)
        return animation

    def paintEvent(self, event):
        if not self.pixmap() or self.pixmap().isNull():
            super().paintEvent(event)
            return
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        if self._next_pixmap and not self._next_pixmap.isNull():
            x = (self.width() - self._next_pixmap.width()) // 2
            y = (self.height() - self._next_pixmap.height()) // 2
            painter.drawPixmap(x, y, self._next_pixmap)
        painter.save()
        if self._rotation < 0:
            opacity = 1.0 - (abs(self._rotation) / 90.0)
            painter.setOpacity(max(0.0, min(1.0, opacity)))
        pivot_y = self.height()
        painter.translate(0, pivot_y)
        painter.rotate(self._rotation)
        painter.translate(0, -pivot_y)
        current = self.pixmap()
        x = (self.width() - current.width()) // 2
        y = (self.height() - current.height()) // 2
        painter.drawPixmap(x, y, current)
        painter.restore()
