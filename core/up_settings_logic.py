import json
import os
import sys
from pathlib import Path

import PySide6
from PySide6.QtCore import QLibraryInfo, QTranslator

from config.settings import load_settings, save_settings


_LANG_CACHE = {}
_QT_TRANSLATORS = []


class InternalQtTranslator(QTranslator):
    def __init__(self, lang_code, parent=None):
        super().__init__(parent)
        self.lang_code = lang_code
        self.map = {
            'Look in:': 'qt_look_in',
            'File &name:': 'qt_file_name',
            'File name:': 'qt_file_name',
            'Files of type:': 'qt_files_of_type',
            '&Open': 'qt_open',
            'Open': 'qt_open',
            '&Save': 'qt_save',
            'Save': 'qt_save',
            '&Cancel': 'qt_cancel',
            'Cancel': 'qt_cancel',
            'Name': 'qt_name',
            'Size': 'qt_size',
            'Type': 'qt_type',
            'Date Modified': 'qt_date_modified',
        }

    def translate(self, context, source_text, disambiguation=None, n=-1):
        key = self.map.get(source_text)
        if not key:
            return ''
        strings = SettingsLogic.get_translations(self.lang_code)
        return strings.get(key, '')


class SettingsLogic:
    @staticmethod
    def load() -> dict:
        return load_settings()

    @staticmethod
    def save(settings: dict) -> None:
        save_settings(settings)

    @staticmethod
    def get_language() -> str:
        return SettingsLogic.load().get('language', 'pl')

    @staticmethod
    def set_language(code: str) -> None:
        settings = SettingsLogic.load()
        settings['language'] = code
        SettingsLogic.save(settings)

    @staticmethod
    def get_theme() -> str:
        return SettingsLogic.load().get('theme', 'system')

    @staticmethod
    def set_theme(code: str) -> None:
        settings = SettingsLogic.load()
        settings['theme'] = code
        SettingsLogic.save(settings)

    @staticmethod
    def get_output_dir() -> str:
        return SettingsLogic.load().get('output_dir', '')

    @staticmethod
    def set_output_dir(path: str) -> None:
        settings = SettingsLogic.load()
        settings['output_dir'] = path
        SettingsLogic.save(settings)

    @staticmethod
    def get_translations(lang_code: str) -> dict:
        # Mapowanie starszych/niestandardowych kodów na standardowe pliki ISO
        iso_map = {'cz': 'cs', 'si': 'sl', 'ge': 'ka', 'ua': 'uk', 'ee': 'et', 'gr': 'el'}
        lang_code = iso_map.get(lang_code, lang_code)

        if lang_code in _LANG_CACHE:
            return _LANG_CACHE[lang_code]
        i18n_dir = Path(__file__).parent.parent / 'i18n'
        json_file = i18n_dir / f'{lang_code}.json'
        if not json_file.exists():
            json_file = i18n_dir / 'pl.json'
        try:
            _LANG_CACHE[lang_code] = json.loads(json_file.read_text(encoding='utf-8'))
        except Exception:
            _LANG_CACHE[lang_code] = {}
        return _LANG_CACHE[lang_code]

    @staticmethod
    def setup_qt_translations(app):
        global _QT_TRANSLATORS
        lang = SettingsLogic.get_language()
        qt_lang_map = {
            'ua': 'uk', 'cz': 'cs', 'si': 'sl', 'ge': 'ka',
            'ee': 'et', 'pt': 'pt_BR', 'ro': 'ro_RO',
            'es': 'es_ES', 'gr': 'el',
        }
        qt_lang = qt_lang_map.get(lang, lang)
        for translator in _QT_TRANSLATORS:
            app.removeTranslator(translator)
        _QT_TRANSLATORS.clear()
        search_paths = [
            QLibraryInfo.path(QLibraryInfo.TranslationsPath),
            os.path.join(os.path.dirname(PySide6.__file__), 'translations'),
            os.path.join(sys.prefix, 'share', 'qt6', 'translations'),
        ]
        files = [f'qtbase_{qt_lang}', f'qt_{qt_lang}', f'qt_help_{qt_lang}']
        if '_' in qt_lang:
            short = qt_lang.split('_')[0]
            files.extend([f'qtbase_{short}', f'qt_{short}'])
        for filename in files:
            translator = QTranslator()
            for path in search_paths:
                if translator.load(filename, path):
                    app.installTranslator(translator)
                    _QT_TRANSLATORS.append(translator)
                    break
        internal = InternalQtTranslator(lang)
        app.installTranslator(internal)
        _QT_TRANSLATORS.append(internal)

    @staticmethod
    def tr(key: str) -> str:
        strings = SettingsLogic.get_translations(SettingsLogic.get_language())
        return strings.get(key, key)
