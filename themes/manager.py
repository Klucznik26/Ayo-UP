from config.settings import load_settings
from .light import LIGHT_THEME
from .dark import DARK_THEME
from .relax import RELAX_THEME
from .creative import CREATIVE_THEME
from .system import SYSTEM_THEME


class ThemeManager:
    @staticmethod
    def apply(app):
        settings = load_settings()
        theme = settings.get("theme", "system")

        if theme == "dark":
            app.setStyleSheet(DARK_THEME)
        elif theme == "light":
            app.setStyleSheet(LIGHT_THEME)
        elif theme == "relax":
            app.setStyleSheet(RELAX_THEME)
        elif theme == "creative":
            app.setStyleSheet(CREATIVE_THEME)
        else:
            # systemowy ≠ pusty
            app.setStyleSheet(SYSTEM_THEME)