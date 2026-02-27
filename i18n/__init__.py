import os
import sys
import PySide6
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
from .es import STRINGS as ES
from .ro import STRINGS as RO
from .fr import STRINGS as FR
from .it import STRINGS as IT
from .gr import STRINGS as GR

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
    "es": ES,
    "ro": RO,
    "fr": FR,
    "it": IT,
    "gr": GR,
}

_qt_translators = []


class InternalQtTranslator(QTranslator):
    """
    Tłumacz awaryjny dla wbudowanych elementów Qt (QFileDialog itp.),
    gdy brakuje plików .qm lub są niekompletne.
    """
    def __init__(self, lang_code, parent=None):
        super().__init__(parent)
        self.lang_code = lang_code
        self.map = {
            # QFileDialog / QDialog
            "Look in:": "qt_look_in",
            "File &name:": "qt_file_name",
            "File name:": "qt_file_name",
            "Files of type:": "qt_files_of_type",
            "&Open": "qt_open",
            "Open": "qt_open",
            "&Save": "qt_save",
            "Save": "qt_save",
            "&Cancel": "qt_cancel",
            "Cancel": "qt_cancel",
            
            # QFileSystemModel (nagłówki kolumn)
            "Name": "qt_name",
            "Size": "qt_size",
            "Type": "qt_type",
            "Date Modified": "qt_date_modified",
        }

    def translate(self, context, source_text, disambiguation=None, n=-1):
        key = self.map.get(source_text)
        if key:
            strings = _LANG_MAP.get(self.lang_code)
            if strings and key in strings:
                return strings[key]
        return ""

def setup_qt_translations(app):
    """
    Ładuje systemowe tłumaczenia Qt (np. dla QFileDialog, QColorDialog).
    """
    global _qt_translators
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
        "pt": "pt_BR",
        "ro": "ro_RO",  # Wymuszamy pełny kod dla Rumunii
        "es": "es_ES",  # Dla pewności Hiszpański
        "gr": "el",     # Grecki w Qt to 'el' (Elliniká)
        # pl, en, lv, lt są zgodne
    }
    
    qt_lang = qt_lang_map.get(lang, lang)

    # Usuń poprzednie tłumacze
    for t in _qt_translators:
        app.removeTranslator(t)
    _qt_translators.clear()
    
    # Ścieżki poszukiwań tłumaczeń Qt
    search_paths = [
        os.path.join(os.path.dirname(__file__), "qt"),
        QLibraryInfo.path(QLibraryInfo.TranslationsPath),
        os.path.join(os.path.dirname(PySide6.__file__), "translations"),
        os.path.join(os.path.dirname(PySide6.__file__), "Qt", "translations"),
        os.path.join(sys.prefix, "share", "qt6", "translations"),
        os.path.join(sys.prefix, "share", "qt5", "translations"), # Fallback
    ]
    
    # Pliki do załadowania (qtbase to podstawa, qt to meta-plik)
    files = [f"qtbase_{qt_lang}", f"qt_{qt_lang}", f"qt_help_{qt_lang}"]

    # Fallback: jeśli mamy np. ro_RO, spróbujmy też samego ro
    if "_" in qt_lang:
        short = qt_lang.split("_")[0]
        files.extend([f"qtbase_{short}", f"qt_{short}"])

    for filename in files:
        translator = QTranslator()
        for path in search_paths:
            if translator.load(filename, path):
                app.installTranslator(translator)
                _qt_translators.append(translator)
                break

    # Na koniec instalujemy nasz wewnętrzny tłumacz, aby miał priorytet
    # (app.installTranslator dodaje na początek stosu)
    internal_translator = InternalQtTranslator(lang)
    app.installTranslator(internal_translator)
    _qt_translators.append(internal_translator)


def tr(key: str) -> str:
    """
    Zwraca przetłumaczony tekst na podstawie aktualnego języka
    zapisanego w ustawieniach użytkownika.
    """
    settings = load_settings()
    lang = settings.get("language", "pl")

    return _LANG_MAP.get(lang, PL).get(key, key)
