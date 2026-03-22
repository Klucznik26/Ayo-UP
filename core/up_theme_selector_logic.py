from core.up_settings_logic import SettingsLogic
from core.up_theme_selector_theme_arctic import DROP_ZONE_QSS as ARCTIC_DROP_ZONE, THEME_QSS as ARCTIC_THEME
from core.up_theme_selector_theme_creative import DROP_ZONE_QSS as CREATIVE_DROP_ZONE, THEME_QSS as CREATIVE_THEME
from core.up_theme_selector_theme_dark import DROP_ZONE_QSS as DARK_DROP_ZONE, THEME_QSS as DARK_THEME
from core.up_theme_selector_theme_light import DROP_ZONE_QSS as LIGHT_DROP_ZONE, THEME_QSS as LIGHT_THEME
from core.up_theme_selector_theme_relax import DROP_ZONE_QSS as RELAX_DROP_ZONE, THEME_QSS as RELAX_THEME
from core.up_theme_selector_theme_system import DROP_ZONE_QSS as SYSTEM_DROP_ZONE, THEME_QSS as SYSTEM_THEME


COMMON_CHROME = """
QFrame#leftPanel, QFrame#rightPanel {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0.20), stop:1 rgba(255, 255, 255, 0.08));
    border-radius: 14px;
    border: 1px solid rgba(255,255,255,0.40);
}
QFrame#narrowPanel {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0.25), stop:1 rgba(0, 0, 0, 0.15));
    border-radius: 14px;
    border: 1px solid rgba(255,255,255,0.1);
}
QPushButton#iconButton {
    background-color: transparent;
    border: none;
    font-size: 24px;
    padding: 8px;
    color: rgba(255, 255, 255, 0.85);
}
QPushButton#iconButton:hover {
    background-color: rgba(255, 255, 255, 0.15);
    border-radius: 10px;
}
QPushButton#iconButton[danger="true"] { color: #ff5a5a; }
QPushButton#iconButton[danger="true"]:hover {
    color: #ff7a7a;
    background-color: rgba(255, 90, 90, 0.18);
    border-radius: 10px;
}
"""

ARCTIC_CHROME = """
QFrame#leftPanel, QFrame#rightPanel {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgba(220, 245, 255, 0.26), stop:1 rgba(120, 210, 255, 0.10));
    border-radius: 14px;
    border: 1px solid rgba(140, 225, 255, 0.45);
}
QFrame#narrowPanel {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(120, 220, 255, 0.30), stop:0.55 rgba(80, 170, 220, 0.22), stop:1 rgba(40, 120, 175, 0.32));
    border-radius: 14px;
    border: 1px solid rgba(165, 236, 255, 0.55);
}
QPushButton#iconButton {
    background-color: transparent;
    border: none;
    font-size: 24px;
    padding: 8px;
    color: #E7FBFF;
}
QPushButton#iconButton:hover {
    background-color: rgba(165, 236, 255, 0.24);
    border-radius: 10px;
}
QPushButton#iconButton[danger="true"] { color: #ff5a5a; }
QPushButton#iconButton[danger="true"]:hover {
    color: #ff7a7a;
    background-color: rgba(255, 90, 90, 0.18);
    border-radius: 10px;
}
"""


class ThemeSelectorLogic:
    @staticmethod
    def get_theme_codes() -> list[str]:
        return ['dark', 'light', 'creative', 'relax', 'arctic', 'system']

    @staticmethod
    def apply(app):
        theme = SettingsLogic.get_theme()
        theme_map = {
            'dark': DARK_THEME + DARK_DROP_ZONE,
            'light': LIGHT_THEME + COMMON_CHROME + LIGHT_DROP_ZONE,
            'creative': CREATIVE_THEME + COMMON_CHROME + CREATIVE_DROP_ZONE,
            'relax': RELAX_THEME + COMMON_CHROME + RELAX_DROP_ZONE,
            'arctic': ARCTIC_THEME + ARCTIC_CHROME + ARCTIC_DROP_ZONE,
            'system': SYSTEM_THEME + COMMON_CHROME + SYSTEM_DROP_ZONE,
        }
        app.setStyleSheet(theme_map.get(theme, theme_map['system']))
