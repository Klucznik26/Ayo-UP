from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QColor, QPainter, QPen
from PySide6.QtWidgets import QDialog, QGridLayout, QLabel, QPushButton, QVBoxLayout, QWidget

from core.up_settings_logic import SettingsLogic
tr = SettingsLogic.tr


LANGUAGES = [
    ("pl", "Polski", "🇵🇱"),
    ("en", "English", "🇬🇧"),
    ("uk", "Українська", "🇺🇦"),
    ("tr", "Türkçe", "🇹🇷"),
    ("sw", "Kiswahili", "🇰🇪"),
    ("sv", "Svenska", "🇸🇪"),
    ("sr", "Српски", "🇷🇸"),
    ("sq", "Shqip", "🇦🇱"),
    ("sl", "Slovenščina", "🇸🇮"),
    ("sk", "Slovenčina", "🇸🇰"),
    ("ro", "Română", "🇷🇴"),
    ("pt", "Português", "🇵🇹"),
    ("no", "Norsk", "🇳🇴"),
    ("nl", "Nederlands", "🇳🇱"),
    ("mt", "Malti", "🇲🇹"),
    ("mk", "Македонски", "🇲🇰"),
    ("lv", "Latviešu", "🇱🇻"),
    ("lt", "Lietuvių", "🇱🇹"),
    ("it", "Italiano", "🇮🇹"),
    ("lb", "Lëtzebuergesch", "🇱🇺"),
    ("kk", "Қазақша", "🇰🇿"),
    ("ka", "ქართული", "🇬🇪"),
    ("ja", "日本語", "🇯🇵"),
    ("is", "Íslenska", "🇮🇸"),
    ("hy", "Հայերեն", "🇦🇲"),
    ("hu", "Magyar", "🇭🇺"),
    ("hr", "Hrvatski", "🇭🇷"),
    ("gl", "Galego", "🇪🇸"),
    ("ga", "Gaeilge", "🇮🇪"),
    ("fr", "Français", "🇫🇷"),
    ("fi", "Suomi", "🇫🇮"),
    ("eu", "Euskara", "🇪🇸"),
    ("et", "Eesti", "🇪🇪"),
    ("es", "Español", "🇪🇸"),
    ("el", "Ελληνικά", "🇬🇷"),
    ("de", "Deutsch", "🇩🇪"),
    ("da", "Dansk", "🇩🇰"),
    ("cs", "Čeština", "🇨🇿"),
    ("co", "Corsu", "🇫🇷"),
    ("ca", "Català", "🇦🇩"),
    ("bs", "Bosanski", "🇧🇦"),
    ("bg", "Български", "🇧🇬"),
    ("az", "Azərbaycan dili", "🇦🇿"),
]

ENGLISH_LANGUAGE_NAMES = {
    "pl": "Polish", "en": "English", "uk": "Ukrainian", "tr": "Turkish",
    "sw": "Swahili", "sv": "Swedish", "sr": "Serbian", "sq": "Albanian",
    "sl": "Slovenian", "sk": "Slovak", "ro": "Romanian", "pt": "Portuguese",
    "no": "Norwegian", "nl": "Dutch", "mt": "Maltese", "mk": "Macedonian",
    "lv": "Latvian", "lt": "Lithuanian", "it": "Italian", "lb": "Luxembourgish",
    "kk": "Kazakh", "ka": "Georgian", "ja": "Japanese", "is": "Icelandic",
    "hy": "Armenian", "hu": "Hungarian", "hr": "Croatian", "gl": "Galician",
    "ga": "Irish", "fr": "French", "fi": "Finnish", "eu": "Basque",
    "et": "Estonian", "es": "Spanish", "el": "Greek", "de": "German",
    "da": "Danish", "cs": "Czech", "co": "Corsican", "ca": "Catalan",
    "bs": "Bosnian", "bg": "Bulgarian", "az": "Azerbaijani"
}

POLISH_LANGUAGE_NAMES = {
    "pl": "polski", "en": "angielski", "uk": "ukraiński", "tr": "turecki",
    "sw": "suahili", "sv": "szwedzki", "sr": "serbski", "sq": "albański",
    "sl": "słoweński", "sk": "słowacki", "ro": "rumuński", "pt": "portugalski",
    "no": "norweski", "nl": "niderlandzki", "mt": "maltański", "mk": "macedoński",
    "lv": "łotewski", "lt": "litewski", "it": "włoski", "lb": "luksemburski",
    "kk": "kazachski", "ka": "gruziński", "ja": "japoński", "is": "islandzki",
    "hy": "ormiański", "hu": "węgierski", "hr": "chorwacki", "gl": "galisyjski",
    "ga": "irlandzki", "fr": "francuski", "fi": "fiński", "eu": "baskijski",
    "et": "estoński", "es": "hiszpański", "el": "grecki", "de": "niemiecki",
    "da": "duński", "cs": "czeski", "co": "korsykański", "ca": "kataloński",
    "bs": "bośniacki", "bg": "bułgarski", "az": "azerski"
}


class SettingsLanguageOptionUI(QPushButton):
    hovered = Signal(str, str, str)
    left = Signal()

    def __init__(self, flag, native_name, code, parent=None):
        super().__init__("", parent)
        self.flag = flag
        self.native_name = native_name
        self.code = code
        self._hovered = False
        self._tile_size = 56
        self._normal_font_px = 46
        self._hover_font_px = 60
        self.setFixedSize(72, 72)
        self.setFlat(True)
        self.setStyleSheet("background: transparent; border: none;")
        self.setCursor(Qt.PointingHandCursor)

    def enterEvent(self, event):
        self._hovered = True
        self.raise_()
        self.update()
        self.hovered.emit(self.flag, self.native_name, self.code)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._hovered = False
        self.update()
        self.left.emit()
        super().leaveEvent(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        try:
            painter.setRenderHint(QPainter.Antialiasing, True)
            tile_color = QColor(255, 255, 255, 80 if self._hovered else 62)
            border_color = QColor(255, 255, 255, 190 if self._hovered else 148)

            x = (self.width() - self._tile_size) // 2
            y = (self.height() - self._tile_size) // 2
            tile_rect = self.rect().adjusted(
                x,
                y,
                -(self.width() - self._tile_size - x),
                -(self.height() - self._tile_size - y),
            )

            painter.setBrush(tile_color)
            painter.setPen(QPen(border_color, 1))
            painter.drawRoundedRect(tile_rect, 12, 12)

            font = self.font()
            font.setPixelSize(self._hover_font_px if self._hovered else self._normal_font_px)
            painter.setFont(font)
            painter.setPen(self.palette().color(self.foregroundRole()))
            painter.drawText(self.rect(), Qt.AlignCenter, self.flag)
        finally:
            painter.end()


class SettingsLanguageUI(QDialog):
    language_selected = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(tr("select_language_title").rstrip(":"))
        self.setModal(True)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)

        self.info_label = QLabel(" ")
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setStyleSheet(
            "font-size: 18px; font-weight: normal; color: palette(text); "
            "padding: 10px 14px; "
            "background-color: rgba(255, 255, 255, 0.32); "
            "border: 1px solid rgba(255, 255, 255, 0.58); "
            "border-radius: 12px;"
        )
        layout.addWidget(self.info_label)

        grid_widget = QWidget()
        grid_layout = QGridLayout(grid_widget)
        grid_layout.setSpacing(8)

        columns = 7
        for i, (code, native_name, flag) in enumerate(LANGUAGES):
            row = i // columns
            col = i % columns
            btn = SettingsLanguageOptionUI(flag, native_name, code)
            btn.clicked.connect(lambda _checked=False, c=code: (self.language_selected.emit(c), self.accept()))
            btn.hovered.connect(self.on_hover)
            btn.left.connect(self.on_leave)
            grid_layout.addWidget(btn, row, col)

        layout.addWidget(grid_widget)

    def on_hover(self, _flag, native_name, _code):
        code = _code
        key = f"lang_{code}"
        localized_name = tr(key)

        if localized_name == key:
            current_lang = SettingsLogic.get_language()
            if current_lang == "pl":
                localized_name = POLISH_LANGUAGE_NAMES.get(code, native_name)
            else:
                localized_name = ENGLISH_LANGUAGE_NAMES.get(code, native_name)

        if localized_name == native_name:
            self.info_label.setText(native_name)
        else:
            self.info_label.setText(f"{native_name} — {localized_name}")

    def on_leave(self):
        self.info_label.setText(" ")
