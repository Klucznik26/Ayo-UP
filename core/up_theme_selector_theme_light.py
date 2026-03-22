THEME_QSS = """
/* =========================
   MOTYW JASNY (BEŻOWY)
   ========================= */

QMainWindow {
    background-color: #F4EFE6;
}

QDialog {
    background-color: #F4EFE6;
}

/* =========================
   RAMKI / PANELE
   ========================= */
QFrame {
    background-color: #FFFFFF;
    border: 1px solid #D6C8B4;
}

/* =========================
   TEKST
   ========================= */
QLabel {
    color: #2F2620;
}

QLabel[secondary="true"] {
    color: #7A6B5C;
}

/* =========================
   PRZYCISKI
   ========================= */
QPushButton {
    padding: 8px 14px;
    background-color: #F0E8DC;
    border: 1px solid #D6C8B4;
    border-radius: 6px;
    color: #2F2620;
}

QPushButton:hover {
    background-color: #E6DED4;
}

QPushButton:pressed {
    background-color: #DCD4CA;
}

QPushButton:disabled {
    background-color: #F4EFE6;
    color: #7A6B5C;
    border-color: #D6C8B4;
}

/* =========================
   PRZYCISK WYKONAJ (AKCENT)
   ========================= */
QPushButton#runButton {
    background-color: #C96A3A;
    border: none;
    color: #FFFFFF;
}

QPushButton#runButton:hover {
    background-color: #D97A4A;
}

QPushButton#runButton:pressed {
    background-color: #B95A2A;
}

/* =========================
   SUWAK SKALI
   ========================= */
QSlider::groove:horizontal {
    height: 6px;
    background: #F0E8DC;
    border-radius: 3px;
}

QSlider::handle:horizontal {
    background: #C96A3A;
    width: 16px;
    margin: -5px 0;
    border-radius: 8px;
}

QSlider::sub-page:horizontal {
    background: #A8552F;
    border-radius: 3px;
}

QSlider::add-page:horizontal {
    background: #F0E8DC;
    border-radius: 3px;
}

/* =========================
   KONTROLKI FORMULARZY
   ========================= */
QComboBox {
    background-color: #F0E8DC;
    color: #2F2620;
    border: 1px solid #D6C8B4;
    padding: 4px;
}

QComboBox::drop-down {
    border: none;
}

QListView, QTreeView {
    background-color: #FFFFFF;
    color: #2F2620;
    border: 1px solid #D6C8B4;
    outline: none;
}

QTreeView::item:selected, QListView::item:selected {
    background-color: #C96A3A;
    color: #FFFFFF;
}

QScrollBar:vertical {
    background: #FFFFFF;
    width: 12px;
    margin: 2px;
    border: 1px solid #D6C8B4;
    border-radius: 6px;
}

QScrollBar::handle:vertical {
    background: #C96A3A;
    min-height: 24px;
    border-radius: 6px;
}

QScrollBar::handle:vertical:hover {
    background: #D97A4A;
}

QScrollBar:horizontal {
    background: #FFFFFF;
    height: 12px;
    margin: 2px;
    border: 1px solid #D6C8B4;
    border-radius: 6px;
}

QScrollBar::handle:horizontal {
    background: #C96A3A;
    min-width: 24px;
    border-radius: 6px;
}

QScrollBar::add-line, QScrollBar::sub-line,
QScrollBar::add-page, QScrollBar::sub-page {
    background: transparent;
    border: none;
}

QHeaderView::section {
    background-color: #F0E8DC;
    color: #2F2620;
    border: none;
    padding: 4px;
}

QLineEdit {
    background-color: #FFFFFF;
    color: #2F2620;
    border: 1px solid #D6C8B4;
    border-radius: 4px;
}

/* =========================
   NARZĘDZIA
   ========================= */
QToolButton {
    background-color: transparent;
    border: none;
    border-radius: 4px;
    color: #2F2620;
    padding: 4px;
}

QToolButton:hover {
    background-color: #F0E8DC;
}

QToolButton:pressed {
    background-color: #E6DED4;
}
"""

DROP_ZONE_QSS = """
    QLabel#dropArea {
        border: 2px dashed #D6C8B4;
        border-radius: 8px;
        color: #2F2620;
        font-size: 16px;
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0.1), stop:1 rgba(0, 0, 0, 0.02));
    }
"""
