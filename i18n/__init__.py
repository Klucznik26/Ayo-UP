from core.up_settings_logic import SettingsLogic


def tr(key: str) -> str:
    return SettingsLogic.tr(key)


def setup_qt_translations(app):
    return SettingsLogic.setup_qt_translations(app)


__all__ = ["tr", "setup_qt_translations"]
