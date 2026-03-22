#!/usr/bin/env python3
"""
Ayo Up — application launcher
"""

import sys
import os

# Upewnij się, że katalog projektu jest na PYTHONPATH
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFont
from gui.up_main_ui import MainUI

def main():
    app = QApplication(sys.argv)
    
    # Ustawienie globalnej czcionki z dobrymi fallbackami dla nietypowych znaków i CJK
    font = app.font()
    font.setFamilies(["Noto Sans", "Segoe UI", "Ubuntu", "sans-serif"])
    app.setFont(font)

    # Ładowanie warstwy logicznej zgodnie z konwencją {app}_{component}_logic
    from core.up_theme_selector_logic import ThemeSelectorLogic
    from core.up_settings_logic import SettingsLogic
    
    ThemeSelectorLogic.apply(app)
    SettingsLogic.setup_qt_translations(app)

    window = MainUI()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
