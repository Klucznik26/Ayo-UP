import random
from PySide6.QtWidgets import QLabel, QWidget, QPushButton
from PySide6.QtGui import QPainter, QPixmap, QColor, QPainterPath
from PySide6.QtCore import Qt, Property, QPropertyAnimation, QEasingCurve, QPoint


class DropImageLabel(QLabel):
    def __init__(self, parent=None, on_drop=None):
        super().__init__(parent)
        self.on_drop = on_drop
        self.setAcceptDrops(True)
        self._rotation = 0.0
        self._next_pixmap = None  # Obraz, który ma się pojawić pod spodem

    # =========================
    # DRAG & DROP
    # =========================

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

    # =========================
    # ANIMACJA I RYSOWANIE
    # =========================
    def get_rotation(self):
        return self._rotation

    def set_rotation(self, angle):
        self._rotation = angle
        self.update()

    # Rejestracja właściwości dla QPropertyAnimation
    rotation = Property(float, get_rotation, set_rotation)

    def set_next_pixmap(self, pixmap):
        """Ustawia obraz, który będzie widoczny pod spodem podczas animacji."""
        self._next_pixmap = pixmap
        self.update()

    def apply_next_image(self):
        """Zatwierdza zmianę: następny obraz staje się obecnym, reset rotacji."""
        if self._next_pixmap:
            self.setPixmap(self._next_pixmap)
            self._next_pixmap = None
        else:
            self.clear()
        self._rotation = 0.0
        self.update()

    def animate_discard(self):
        """Tworzy i zwraca animację odrzucenia obrazu w lewo."""
        anim = QPropertyAnimation(self, b"rotation")
        anim.setDuration(600)
        anim.setStartValue(0.0)
        anim.setEndValue(-90.0)  # Obrót w lewo o 90 stopni
        anim.setEasingCurve(QEasingCurve.InBack) # Efekt "zamachu" przed ruchem
        return anim

    def paintEvent(self, event):
        # Jeśli nie ma obrazka, rysujemy standardowo (np. tekst placeholder)
        if not self.pixmap() or self.pixmap().isNull():
            super().paintEvent(event)
            return

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)

        # 1. Rysuj NASTĘPNY obraz pod spodem (jeśli istnieje)
        if self._next_pixmap and not self._next_pixmap.isNull():
            # Centrujemy następny obraz
            x = (self.width() - self._next_pixmap.width()) // 2
            y = (self.height() - self._next_pixmap.height()) // 2
            painter.drawPixmap(x, y, self._next_pixmap)

        # 2. Rysuj OBECNY obraz z uwzględnieniem rotacji
        painter.save()
        
        # Efekt zanikania (fade out) w miarę obrotu w lewo
        if self._rotation < 0:
            opacity = 1.0 - (abs(self._rotation) / 90.0)
            painter.setOpacity(max(0.0, min(1.0, opacity)))
        
        # Oś obrotu: Lewy Dolny Róg
        # Przesuwamy układ współrzędnych do lewego dolnego rogu widgetu
        pivot_y = self.height()
        painter.translate(0, pivot_y)
        painter.rotate(self._rotation)
        painter.translate(0, -pivot_y)

        # Rysujemy obecny pixmap (wycentrowany w oryginalnym układzie)
        current_pix = self.pixmap()
        x = (self.width() - current_pix.width()) // 2
        y = (self.height() - current_pix.height()) // 2
        painter.drawPixmap(x, y, current_pix)

        painter.restore()


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
