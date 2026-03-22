from PySide6.QtCore import QRect, Qt, Signal
from PySide6.QtGui import QColor, QImage, QPainter, QPixmap
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QPushButton


class ThemeSelectorOptionUI(QPushButton):
    hovered = Signal(str, str)
    left = Signal()

    def __init__(self, icon_path, theme_name, code, is_top=False, glow_color='#FFFFFF', parent=None):
        super().__init__('', parent)
        self.theme_name = theme_name
        self.code = code
        self._hovered = False
        self._selected = False
        normal_target = 195 if is_top else 171
        hover_target = 205 if is_top else 180
        original = QPixmap(icon_path)
        self.pix_normal = self._crop(original.scaled(normal_target, normal_target, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.pix_hover = self._crop(original.scaled(hover_target, hover_target, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.setFixedSize(self.pix_hover.width(), self.pix_hover.height())
        self.setFlat(True)
        self.setStyleSheet('background: transparent; border: none;')
        self.setCursor(Qt.PointingHandCursor)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(12)
        self.shadow.setOffset(0, 0)
        self._apply_shadow(glow_color, 50, 12)
        self.setGraphicsEffect(self.shadow)

    def _crop(self, pixmap):
        if pixmap.isNull():
            return pixmap
        image = pixmap.toImage().convertToFormat(QImage.Format_ARGB32)
        w, h = image.width(), image.height()
        min_x, min_y, max_x, max_y = w, h, -1, -1
        for y in range(h):
            for x in range(w):
                if (image.pixel(x, y) >> 24) & 0xFF > 5:
                    min_x, max_x = min(min_x, x), max(max_x, x)
                    min_y, max_y = min(min_y, y), max(max_y, y)
        if min_x <= max_x and min_y <= max_y:
            return pixmap.copy(QRect(min_x, min_y, max_x - min_x + 1, max_y - min_y + 1))
        return pixmap

    def _apply_shadow(self, glow_color, alpha, blur):
        color = QColor(glow_color)
        color.setAlpha(alpha)
        self.shadow.setColor(color)
        self.shadow.setBlurRadius(blur)

    def set_selected(self, selected):
        self._selected = selected
        self._apply_shadow('#FFFFFF', 160 if selected else 50, 25 if selected else 12)
        self.update()

    def enterEvent(self, event):
        self._hovered = True
        self.raise_()
        self.hovered.emit(self.theme_name, self.code)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._hovered = False
        self.left.emit()
        super().leaveEvent(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
        current = self.pix_hover if self._hovered else self.pix_normal
        if current and not current.isNull():
            px = (self.width() - current.width()) // 2
            py = (self.height() - current.height()) // 2
            painter.drawPixmap(px, py, current)
