from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QSlider

from core.up_settings_logic import SettingsLogic


class ImageUpscaleScaleUI:
    def __init__(self, parent_layout, initial=2):
        self.scale = initial
        self.label = QLabel()
        self.label.setObjectName('scaleLabel')
        self.label.setAlignment(Qt.AlignCenter)
        parent_layout.addWidget(self.label)
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(2)
        self.slider.setMaximum(4)
        self.slider.setSingleStep(2)
        self.slider.setPageStep(2)
        self.slider.setTickInterval(2)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setValue(initial)
        self.slider.valueChanged.connect(self._on_changed)
        parent_layout.addWidget(self.slider)
        self.retranslate_ui()

    def _on_changed(self, value: int):
        if value not in (2, 4):
            value = 2
            self.slider.setValue(2)
        self.scale = value
        self.retranslate_ui()

    def get(self) -> int:
        return self.scale

    def retranslate_ui(self):
        self.label.setText(f"{SettingsLogic.tr('scale')}: x{self.scale}")
