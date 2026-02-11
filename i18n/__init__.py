from config.settings import load_settings

from .pl import STRINGS as PL
from .en import STRINGS as EN
from .ua import STRINGS as UA
from .lv import STRINGS as LV
from .lt import STRINGS as LT
from .ee import STRINGS as EE
from .pt import STRINGS as PT

_LANG_MAP = {
    "pl": PL,
    "en": EN,
    "ua": UA,
    "lv": LV,
    "lt": LT,
    "ee": EE,
    "pt": PT,
}


def tr(key: str) -> str:
    """
    Zwraca przetłumaczony tekst na podstawie aktualnego języka
    zapisanego w ustawieniach użytkownika.
    """
    settings = load_settings()
    lang = settings.get("language", "pl")

    return _LANG_MAP.get(lang, PL).get(key, key)
