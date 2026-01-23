from PySide6.QtWidgets import QLabel, QSlider
from PySide6.QtCore import Qt

from i18n import tr


class ScaleController:
    """
    Kontroler skali (x2 / x4)
    Estetyczny suwak + czytelny napis
    Działa poprawnie w jasnym i ciemnym motywie
    """

    def __init__(self, parent_layout, initial=2):
        self.scale = initial

        # =========================
        # LABEL
        # =========================
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("""
            QLabel {
                font-size: 13px;
                font-weight: 500;
                color: palette(windowText);
            }
        """)
        parent_layout.addWidget(self.label)

        # =========================
        # SUWAK
        # =========================
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(2)
        self.slider.setMaximum(4)
        self.slider.setSingleStep(2)
        self.slider.setPageStep(2)
        self.slider.setTickInterval(2)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setValue(initial)

        # Styl neutralny – oparty o paletę Qt
        self.slider.setStyleSheet("""
            QSlider {
                height: 22px;
            }

            QSlider::groove:horizontal {
                height: 6px;
                background: palette(mid);
                border-radius: 3px;
            }

            QSlider::sub-page:horizontal {
                background: #C96A3A;
                border-radius: 3px;
            }

            QSlider::handle:horizontal {
                width: 18px;
                height: 18px;
                margin: -6px 0;
                border-radius: 9px;
                background: #C96A3A;
                border: 2px solid palette(dark);
            }

            QSlider::handle:horizontal:hover {
                background: #B35E34;
            }
        """)

        self.slider.valueChanged.connect(self._on_changed)
        parent_layout.addWidget(self.slider)

        self.retranslate()

    # =========================
    # LOGIKA
    # =========================
    def _on_changed(self, value: int):
        if value not in (2, 4):
            value = 2
            self.slider.setValue(2)

        self.scale = value
        self.retranslate()

    # =========================
    # API
    # =========================
    def get(self) -> int:
        return self.scale

    # =========================
    # I18N
    # =========================
    def retranslate(self):
        self.label.setText(f"{tr('scale')}: x{self.scale}")
