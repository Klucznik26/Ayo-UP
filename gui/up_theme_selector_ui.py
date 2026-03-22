import os

from PySide6.QtCore import QEvent, Qt, Signal
from PySide6.QtGui import QColor, QMouseEvent
from PySide6.QtWidgets import QDialog, QFrame, QGraphicsDropShadowEffect, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget

from core.up_settings_logic import SettingsLogic
from gui.up_theme_selector_widgets import ThemeSelectorOptionUI


class ThemeSelectorUI(QDialog):
    theme_selected = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.btn_confirm = None
        self.btn_confirm_shadow = None
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setModal(True)
        self.setMinimumSize(510, 486)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self.main_container = QWidget(self)
        layout.addWidget(self.main_container)
        container_layout = QVBoxLayout(self.main_container)
        container_layout.setContentsMargins(5, 5, 5, 5)
        self.glass_panel = QFrame(self.main_container)
        container_layout.addWidget(self.glass_panel)
        glass_layout = QVBoxLayout(self.glass_panel)
        glass_layout.setContentsMargins(6, 6, 6, 6)
        glass_layout.setSpacing(5)

        top_bar = QHBoxLayout()
        top_bar.addWidget(QWidget())
        self.title_label = QLabel(SettingsLogic.tr('select_theme_title').rstrip(':'))
        self.title_label.setAlignment(Qt.AlignCenter)
        self.btn_close = QPushButton('✕')
        self.btn_close.setFixedSize(30, 30)
        self.btn_close.clicked.connect(self.reject)
        top_bar.addStretch()
        top_bar.addWidget(self.title_label)
        top_bar.addStretch()
        top_bar.addWidget(self.btn_close)
        glass_layout.addLayout(top_bar)

        self.info_label = QLabel(' ')
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setFixedHeight(32)
        glass_layout.addWidget(self.info_label)
        self._build_theme_grid(glass_layout)

        bottom_bar = QHBoxLayout()
        bottom_bar.addStretch()
        self.btn_confirm = QPushButton(SettingsLogic.tr('apply'))
        self.btn_confirm.clicked.connect(self.confirm_theme)
        self.btn_confirm_shadow = QGraphicsDropShadowEffect()
        self.btn_confirm.setGraphicsEffect(self.btn_confirm_shadow)
        self.btn_confirm.installEventFilter(self)
        bottom_bar.addWidget(self.btn_confirm)
        bottom_bar.addStretch()
        glass_layout.addLayout(bottom_bar)

        self.current_theme = SettingsLogic.get_theme()
        self.preview_theme = self.current_theme
        self.apply_preview_theme()
        self._update_selected_button()

    def _build_theme_grid(self, glass_layout):
        themes = [
            ('dark', SettingsLogic.tr('theme_dark'), 't-night.png'),
            ('light', SettingsLogic.tr('theme_light'), 't_light.png'),
            ('creative', SettingsLogic.tr('theme_creative'), 't_creative.png'),
            ('relax', SettingsLogic.tr('theme_relax'), 't-relaxing.png'),
            ('arctic', SettingsLogic.tr('theme_arctic'), 't_arctic.png'),
            ('system', SettingsLogic.tr('theme_system'), 't_system.png'),
        ]
        glow = {'dark': '#818CF8', 'light': '#FBBF24', 'creative': '#F43F5E', 'relax': '#34D399', 'arctic': '#22D3EE', 'system': '#94A3B8'}
        assets_dir = os.path.join(os.path.dirname(__file__), '..', 'assets', 'themes_logo')
        fallback = os.path.join(os.path.dirname(__file__), '..', 'assets', 'AyoUP.png')
        grid_widget = QWidget()
        pyramid_layout = QVBoxLayout(grid_widget)
        theme_index = 0
        for row_index, count in enumerate([1, 2, 3]):
            row_layout = QHBoxLayout()
            row_layout.addStretch()
            for _ in range(count):
                if theme_index >= len(themes):
                    break
                code, name, filename = themes[theme_index]
                icon_path = os.path.join(assets_dir, filename)
                button = ThemeSelectorOptionUI(icon_path if os.path.exists(icon_path) else fallback, name, code, row_index == 0, glow[code])
                button.clicked.connect(lambda _checked=False, theme_code=code: self.on_theme_clicked(theme_code))
                button.hovered.connect(self.on_hover)
                button.left.connect(self.on_leave)
                row_layout.addWidget(button)
                theme_index += 1
            row_layout.addStretch()
            pyramid_layout.addLayout(row_layout)
        glass_layout.addWidget(grid_widget)

    def eventFilter(self, obj, event):
        if obj is self.btn_confirm and self.btn_confirm_shadow and event.type() in {QEvent.Enter, QEvent.Leave}:
            alpha = 110 if event.type() == QEvent.Enter else 60
            blur = 20 if event.type() == QEvent.Enter else 15
            self.btn_confirm_shadow.setColor(QColor(4, 227, 138, alpha))
            self.btn_confirm_shadow.setBlurRadius(blur)
        return super().eventFilter(obj, event)

    def on_theme_clicked(self, theme_code):
        self.preview_theme = theme_code
        self.apply_preview_theme()
        self._update_selected_button()

    def _update_selected_button(self):
        for button in self.findChildren(ThemeSelectorOptionUI):
            button.set_selected(button.code == self.preview_theme)

    def confirm_theme(self):
        self.theme_selected.emit(self.preview_theme)
        self.accept()

    def apply_preview_theme(self):
        colors = {
            'dark': {'bg': 'rgba(10, 25, 20, 0.75)', 'text': '#FFFFFF', 'glow': '#04E38A'},
            'light': {'bg': 'rgba(230, 245, 240, 0.75)', 'text': '#1A1A1A', 'glow': '#00A86B'},
            'creative': {'bg': 'rgba(30, 45, 40, 0.75)', 'text': '#FFFFFF', 'glow': '#FF2E63'},
            'relax': {'bg': 'rgba(15, 35, 25, 0.75)', 'text': '#FFFFFF', 'glow': '#81C784'},
            'arctic': {'bg': 'rgba(10, 30, 35, 0.75)', 'text': '#FFFFFF', 'glow': '#00E5FF'},
            'system': {'bg': 'rgba(10, 25, 20, 0.75)', 'text': '#FFFFFF', 'glow': '#04E38A'},
        }
        data = colors.get(self.preview_theme, colors['dark'])
        self.info_label.setText(' ')
        self.glass_panel.setStyleSheet(f"QFrame {{ background: {data['bg']}; border-radius: 20px; border: 1px solid rgba(255,255,255,0.08); }}")
        self.title_label.setStyleSheet(f"color: {data['text']}; background: transparent; border: none;")
        self.btn_close.setStyleSheet(f"QPushButton {{ color: {data['text']}; }}")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(30)
        shadow.setOffset(0, 5)
        color = QColor(data['glow'])
        color.setAlpha(60)
        shadow.setColor(color)
        self.glass_panel.setGraphicsEffect(shadow)
        if self.btn_confirm_shadow:
            self.btn_confirm_shadow.setColor(QColor(4, 227, 138, 60))
            self.btn_confirm_shadow.setBlurRadius(15)
            self.btn_confirm_shadow.setOffset(0, 0)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self._drag_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() == Qt.LeftButton and hasattr(self, '_drag_pos'):
            self.move(event.globalPosition().toPoint() - self._drag_pos)
            event.accept()

    def on_hover(self, theme_name, _code):
        self.info_label.setText(theme_name)

    def on_leave(self):
        self.info_label.setText(' ')
