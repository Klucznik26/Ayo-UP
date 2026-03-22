import os

from PySide6.QtCore import QSize, Signal, QRect, QEvent
from PySide6.QtGui import QIcon, QColor, Qt, QPixmap, QImage
from PySide6.QtWidgets import QApplication, QFrame, QGraphicsDropShadowEffect, QPushButton, QSpacerItem, QSizePolicy, QVBoxLayout

from core.up_settings_logic import SettingsLogic
from core.up_theme_selector_logic import ThemeSelectorLogic
from gui.up_settings_info_ui import SettingsInfoUI
from gui.up_settings_language_ui import SettingsLanguageUI
from gui.up_theme_selector_ui import ThemeSelectorUI


class SettingsUI(QFrame):
    close_requested = Signal()
    language_changed = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('narrowPanel')
        self.setFixedWidth(60)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(30)
        shadow.setOffset(0, 6)
        shadow.setColor(QColor(0, 0, 0, 60))
        self.setGraphicsEffect(shadow)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 20, 0, 20)
        layout.setSpacing(20)
        self.btn_logo = QPushButton(); self.btn_logo.setObjectName('iconButton')
        self.btn_lang = QPushButton('🌐\uFE0E'); self.btn_lang.setObjectName('iconButton')
        self.btn_theme = QPushButton('⚙'); self.btn_theme.setObjectName('iconButton')
        self.btn_close = QPushButton('⏻'); self.btn_close.setObjectName('iconButton'); self.btn_close.setProperty('danger', True)
        for button in (self.btn_logo, self.btn_lang, self.btn_theme, self.btn_close):
            button.setCursor(Qt.PointingHandCursor)
            button.setFixedSize(44, 44)
            btn_shadow = QGraphicsDropShadowEffect(button)
            btn_shadow.setBlurRadius(20)
            btn_shadow.setOffset(0, 0)
            btn_shadow.setColor(QColor(4, 227, 138, 0)) # Szmaragdowy neon (domyślnie przezroczysty)
            button.setGraphicsEffect(btn_shadow)
            button.installEventFilter(self)
        self.btn_logo.clicked.connect(lambda: SettingsInfoUI('1.7.0', self).exec())
        self.btn_lang.clicked.connect(self._open_language_selector)
        self.btn_theme.clicked.connect(self._open_theme_selector)
        self.btn_close.clicked.connect(self.close_requested.emit)
        layout.addWidget(self.btn_logo, 0, Qt.AlignCenter)
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        layout.addWidget(self.btn_lang, 0, Qt.AlignCenter)
        layout.addWidget(self.btn_theme, 0, Qt.AlignCenter)
        layout.addWidget(self.btn_close, 0, Qt.AlignCenter)
        self._load_icons()
        self.retranslate_ui()

    def eventFilter(self, obj, event):
        # Animacja powiększania i świecenia po najechaniu myszką
        if event.type() == QEvent.Enter:
            if obj in (self.btn_lang, self.btn_theme, self.btn_close):
                obj.setIconSize(QSize(35, 35)) # Powiększenie z 32 na 35 (ok. 10%)
                if obj.graphicsEffect():
                    obj.graphicsEffect().setColor(QColor(4, 227, 138, 180))
            elif obj == self.btn_logo:
                obj.setIconSize(QSize(43, 43)) # Powiększenie z 39 na 43 (ok. 10%)
                if obj.graphicsEffect():
                    obj.graphicsEffect().setColor(QColor(4, 227, 138, 180))
        elif event.type() == QEvent.Leave:
            if obj in (self.btn_lang, self.btn_theme, self.btn_close):
                obj.setIconSize(QSize(32, 32)) # Powrót do pierwotnego rozmiaru
                if obj.graphicsEffect():
                    obj.graphicsEffect().setColor(QColor(4, 227, 138, 0))
            elif obj == self.btn_logo:
                obj.setIconSize(QSize(39, 39)) # Powrót do pierwotnego rozmiaru
                if obj.graphicsEffect():
                    obj.graphicsEffect().setColor(QColor(4, 227, 138, 0))
        return super().eventFilter(obj, event)

    def _load_icons(self):
        # Używamy ścieżek absolutnych, by zawsze trafiały w prawidłowe miejsce
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        logo_path = os.path.normpath(os.path.join(current_dir, '..', 'assets', 'AUP.png'))
        if os.path.exists(logo_path):
            self.btn_logo.setIcon(QIcon(logo_path))
            self.btn_logo.setIconSize(QSize(39, 39))
        else:
            self.btn_logo.setText('A')
            print(f"[DEBUG] Nie znaleziono logo: {logo_path}")
            
        lang_path = os.path.normpath(os.path.join(current_dir, '..', 'assets', 'icons', 'languages.png'))
        if os.path.exists(lang_path):
            self.btn_lang.setText('')
            pixmap = QPixmap(lang_path)
            cropped_pixmap = self._crop_pixmap(pixmap)
            self.btn_lang.setIcon(QIcon(cropped_pixmap))
            self.btn_lang.setIconSize(QSize(32, 32))
        else:
            self.btn_lang.setText('🌐\uFE0E')
            print(f"[DEBUG] Nie znaleziono ikony języka: {lang_path}")
            
        theme_path = os.path.normpath(os.path.join(current_dir, '..', 'assets', 'icons', 'settings.png'))
        if os.path.exists(theme_path):
            self.btn_theme.setText('')
            pixmap = QPixmap(theme_path)
            cropped_pixmap = self._crop_pixmap(pixmap)
            self.btn_theme.setIcon(QIcon(cropped_pixmap))
            self.btn_theme.setIconSize(QSize(32, 32))
        else:
            self.btn_theme.setText('⚙')
            print(f"[DEBUG] Nie znaleziono ikony motywu: {theme_path}")

        exit_path = os.path.normpath(os.path.join(current_dir, '..', 'assets', 'icons', 'exit.png'))
        if os.path.exists(exit_path):
            self.btn_close.setText('')
            pixmap = QPixmap(exit_path)
            cropped_pixmap = self._crop_pixmap(pixmap)
            self.btn_close.setIcon(QIcon(cropped_pixmap))
            self.btn_close.setIconSize(QSize(32, 32))
        else:
            self.btn_close.setText('⏻')
            print(f"[DEBUG] Nie znaleziono ikony wyjścia: {exit_path}")

    def _crop_pixmap(self, pixmap: QPixmap) -> QPixmap:
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

    def _open_language_selector(self):
        dialog = SettingsLanguageUI(self)
        dialog.language_selected.connect(self._apply_language)
        dialog.exec()

    def _open_theme_selector(self):
        dialog = ThemeSelectorUI(self)
        dialog.theme_selected.connect(self._apply_theme)
        dialog.exec()

    def _apply_language(self, code):
        SettingsLogic.set_language(code)
        SettingsLogic.setup_qt_translations(QApplication.instance())
        self.language_changed.emit()

    def _apply_theme(self, code):
        SettingsLogic.set_theme(code)
        ThemeSelectorLogic.apply(QApplication.instance())

    def retranslate_ui(self):
        tr = SettingsLogic.tr
        self.btn_lang.setToolTip(tr('settings_language'))
        self.btn_theme.setToolTip(tr('theme'))
        self.btn_close.setToolTip(tr('exit'))
        self.btn_logo.setToolTip(tr('app_info'))
