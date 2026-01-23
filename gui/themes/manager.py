from config.settings import load_settings
from gui.themes.light import LIGHT_THEME
from gui.themes.dark import DARK_THEME


SYSTEM_THEME = """
/* =========================
   DROP ZONE – MINIMUM UX
   ========================= */
QFrame {
    background-color: palette(base);
    border: 2px dashed palette(mid);
}

QLabel {
    color: palette(windowText);
}
"""


class ThemeManager:
    @staticmethod
    def apply(app):
        settings = load_settings()
        theme = settings.get("theme", "system")

        if theme == "dark":
            app.setStyleSheet(DARK_THEME)
        elif theme == "light":
            app.setStyleSheet(LIGHT_THEME)
        else:
            # systemowy ≠ pusty
            app.setStyleSheet(SYSTEM_THEME)
