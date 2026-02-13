import random
from PySide6.QtWidgets import QLabel, QWidget, QPushButton
from PySide6.QtGui import QPainter, QPixmap, QColor, QPainterPath
from PySide6.QtCore import Qt


class DropImageLabel(QLabel):
    def __init__(self, parent=None, on_drop=None):
        super().__init__(parent)
        self.on_drop = on_drop
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if not urls:
            return

        paths = [url.toLocalFile() for url in urls]
        # Przekazujemy listę ścieżek do handlera
        if self.on_drop:
            self.on_drop(paths)


class FanPreviewWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(240, 195)
        self.paths = []
        # Widget musi przepuszczać zdarzenia myszy (drop), aby działało upuszczanie pod nim
        self.setAttribute(Qt.WA_TransparentForMouseEvents)

    def set_images(self, paths):
        if len(paths) > 5:
            self.paths = random.sample(paths, 5)
        else:
            self.paths = paths
        self.update()

    def paintEvent(self, event):
        if not self.paths:
            return

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)

        count = len(self.paths)
        
        # Punkt zaczepienia wachlarza (pivot)
        cx = self.width() / 2
        cy = self.height() / 2 + 45

        # Kąty rozłożenia kart
        spread = 40
        start_angle = -spread / 2
        step = spread / (count - 1) if count > 1 else 0

        card_w, card_h = 90, 90

        for i, path in enumerate(self.paths):
            pix = QPixmap(path)
            if pix.isNull():
                continue

            scaled = pix.scaled(card_w, card_h, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            angle = start_angle + i * step if count > 1 else 0

            painter.save()
            painter.translate(cx, cy)
            painter.rotate(angle)
            painter.translate(0, -60) # Promień wachlarza

            # Biała ramka + obrazek
            ox, oy = -scaled.width() / 2, -scaled.height() / 2
            painter.setBrush(QColor(255, 255, 255))
            painter.drawRoundedRect(ox - 4, oy - 4, scaled.width() + 8, scaled.height() + 8, 3, 3)
            painter.drawPixmap(int(ox), int(oy), scaled)
            painter.restore()


class ProgressButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._progress = 0
        self._total = 0

    def set_progress(self, current, total):
        self._progress = current
        self._total = total
        self.update()

    def reset_progress(self):
        self._progress = 0
        self._total = 0
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)

        if self._total > 0 and self._progress > 0:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            
            # Przycinanie do zaokrąglonych rogów (dopasowanie do stylu motywu)
            path = QPainterPath()
            path.addRoundedRect(self.rect(), 6, 6)
            painter.setClipPath(path)

            ratio = self._progress / self._total
            ratio = min(ratio, 1.0)
            w = self.width() * ratio
            
            painter.setPen(Qt.NoPen)
            # Biała, półprzezroczysta nakładka (ok. 20% widoczności)
            painter.setBrush(QColor(255, 255, 255, 50))
            
            painter.drawRect(0, 0, int(w), self.height())
