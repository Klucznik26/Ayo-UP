from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QComboBox,
    QPushButton,
    QHBoxLayout,
)

from config.settings import load_settings, save_settings
from i18n import tr


class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setModal(True)
        self.setFixedSize(320, 240)

        self.settings = load_settings()

        layout = QVBoxLayout(self)
        layout.setSpacing(12)

        # =========================
        # JĘZYK
        # =========================
        self.lbl_language = QLabel()
        layout.addWidget(self.lbl_language)

        self.language_combo = QComboBox()
        self.language_combo.addItem("Polski", "pl")
        self.language_combo.addItem("English", "en")
        self.language_combo.addItem("Українська", "ua")
        self.language_combo.addItem("Latviešu", "lv")
        self.language_combo.addItem("Lietuvių", "lt")
        self.language_combo.addItem("Eesti", "ee")

        current_lang = self.settings.get("language", "pl")
        index = self.language_combo.findData(current_lang)
        if index >= 0:
            self.language_combo.setCurrentIndex(index)

        self.language_combo.currentIndexChanged.connect(
            self._on_language_changed
        )

        layout.addWidget(self.language_combo)

        # =========================
        # MOTYW
        # =========================
        self.lbl_theme = QLabel()
        layout.addWidget(self.lbl_theme)

        self.theme_combo = QComboBox()
        self.theme_combo.addItem(tr("theme_system"), "system")
        self.theme_combo.addItem(tr("theme_light"), "light")
        self.theme_combo.addItem(tr("theme_dark"), "dark")

        current_theme = self.settings.get("theme", "system")
        index = self.theme_combo.findData(current_theme)
        if index >= 0:
            self.theme_combo.setCurrentIndex(index)

        layout.addWidget(self.theme_combo)

        layout.addStretch()

        # =========================
        # PRZYCISKI
        # =========================
        buttons = QHBoxLayout()

        self.btn_cancel = QPushButton()
        self.btn_cancel.clicked.connect(self.reject)

        self.btn_save = QPushButton()
        self.btn_save.clicked.connect(self._save)

        buttons.addWidget(self.btn_cancel)
        buttons.addWidget(self.btn_save)

        layout.addLayout(buttons)

        # =========================
        # INIT I18N
        # =========================
        self.retranslate_ui()

    # =========================
    # LIVE ZMIANA JĘZYKA
    # =========================
    def _on_language_changed(self):
        self.settings["language"] = self.language_combo.currentData()
        save_settings(self.settings)
        self.retranslate_ui()

    # =========================
    # ZAPIS
    # =========================
    def _save(self):
        self.settings["language"] = self.language_combo.currentData()
        self.settings["theme"] = self.theme_combo.currentData()
        save_settings(self.settings)
        self.accept()

    # =========================
    # I18N
    # =========================
    def retranslate_ui(self):
        self.setWindowTitle(tr("settings"))

        self.lbl_language.setText(tr("settings_language"))
        self.lbl_theme.setText(tr("theme"))

        self.btn_save.setText(tr("save"))
        self.btn_cancel.setText(tr("cancel"))

        # aktualizacja nazw motywów po zmianie języka
        current_theme = self.theme_combo.currentData()
        self.theme_combo.blockSignals(True)
        self.theme_combo.clear()
        self.theme_combo.addItem(tr("theme_system"), "system")
        self.theme_combo.addItem(tr("theme_light"), "light")
        self.theme_combo.addItem(tr("theme_dark"), "dark")
        index = self.theme_combo.findData(current_theme)
        if index >= 0:
            self.theme_combo.setCurrentIndex(index)
        self.theme_combo.blockSignals(False)
