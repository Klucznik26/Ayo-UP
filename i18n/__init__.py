from PySide6.QtCore import QTranslator, QLibraryInfo
from config.settings import load_settings

from .pl import STRINGS as PL
from .en import STRINGS as EN
from .ua import STRINGS as UA
from .lv import STRINGS as LV
from .lt import STRINGS as LT
from .ee import STRINGS as EE
from .pt import STRINGS as PT
from .cz import STRINGS as CZ
from .si import STRINGS as SI
from .ge import STRINGS as GE

_LANG_MAP = {
    "pl": PL,
    "en": EN,
    "ua": UA,
    "lv": LV,
    "lt": LT,
    "ee": EE,
    "pt": PT,
    "cz": CZ,
    "si": SI,
    "ge": GE,
}

_qt_translator = None


def setup_qt_translations(app):
    """
    Ładuje systemowe tłumaczenia Qt (np. dla QFileDialog, QColorDialog).
    """
    global _qt_translator
    settings = load_settings()
    lang = settings.get("language", "pl")

    # Mapowanie kodów aplikacji na kody Qt/ISO 639-1
    # Qt używa standardowych kodów (np. uk dla ukraińskiego, cs dla czeskiego)
    qt_lang_map = {
        "ua": "uk",
        "cz": "cs",
        "si": "sl",
        "ge": "ka",
        "ee": "et",
        # pl, en, lv, lt, pt są zgodne
    }
    
    qt_lang = qt_lang_map.get(lang, lang)

    if _qt_translator:
        app.removeTranslator(_qt_translator)
    
    _qt_translator = QTranslator()
    path = QLibraryInfo.path(QLibraryInfo.TranslationsPath)
    
    # Ładowanie tłumaczeń bazowych Qt (qtbase_xx.qm)
    if _qt_translator.load(f"qtbase_{qt_lang}", path):
        app.installTranslator(_qt_translator)


def tr(key: str) -> str:
    """
    Zwraca przetłumaczony tekst na podstawie aktualnego języka
    zapisanego w ustawieniach użytkownika.
    """
    settings = load_settings()
    lang = settings.get("language", "pl")

    return _LANG_MAP.get(lang, PL).get(key, key)
