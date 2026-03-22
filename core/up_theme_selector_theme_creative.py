THEME_QSS = """
/* =========================
   MOTYW KREATYWNY (PURPLE/CYAN)
   ========================= */

QMainWindow {
    background-color: #4A1E2D;
}

QDialog {
    background-color: #4A1E2D;
    color: #E6E8FF;
}

/* =========================
   RAMKI / PANELE
   ========================= */
QFrame {
    background-color: #1E2129;
    border: 1px solid #3A3F55;
}

/* =========================
   TEKST
   ========================= */
QLabel {
    color: #E6E8FF;
}

QLabel[secondary="true"] {
    color: #8F93B0;
}

/* =========================
   PRZYCISKI
   ========================= */
QPushButton {
    padding: 8px 14px;
    background-color: #2B2F3A;
    border: 1px solid #3A3F55;
    border-radius: 6px;
    color: #E6E8FF;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #3A3F55;
    color: #FFFFFF;
}

QPushButton:pressed {
    background-color: #1F222B;
    border: 1px solid #3A3F55;
}

QPushButton:disabled {
    background-color: #1E2129;
    color: #8F93B0;
    border: 1px solid #3A3F55;
}

/* =========================
   PRZYCISK WYKONAJ (AKCENT)
   ========================= */
QPushButton#runButton {
    background-color: #8A5CFF;
    border: none;
    color: #FFFFFF;
}

QPushButton#runButton:hover {
    background-color: #B88CFF;
}

QPushButton#runButton:pressed {
    background-color: #6A3AB2;
}

/* =========================
   SUWAK SKALI
   ========================= */
QSlider::groove:horizontal {
    height: 6px;
    background: #2B2F3A;
    border-radius: 3px;
}

QSlider::handle:horizontal {
    background: #8A5CFF;
    width: 16px;
    margin: -5px 0;
    border-radius: 8px;
}

QSlider::sub-page:horizontal {
    background: #00E5FF;
    border-radius: 3px;
}

QSlider::add-page:horizontal {
    background: #2B2F3A;
    border-radius: 3px;
}

/* =========================
   KONTROLKI FORMULARZY
   ========================= */
QComboBox {
    background-color: #252833;
    color: #E6E8FF;
    border: 1px solid #3A3F55;
    padding: 4px;
}

QComboBox::drop-down {
    border: none;
}

QListView, QTreeView {
    background-color: #252833;
    color: #E6E8FF;
    border: 1px solid #3A3F55;
    outline: none;
}

QTreeView::item:selected, QListView::item:selected {
    background-color: #8A5CFF;
    color: #FFFFFF;
}

QScrollBar:vertical {
    background: #252833;
    width: 12px;
    margin: 2px;
    border: 1px solid #3A3F55;
    border-radius: 6px;
}

QScrollBar::handle:vertical {
    background: #8A5CFF;
    min-height: 24px;
    border-radius: 6px;
}

QScrollBar::handle:vertical:hover {
    background: #B88CFF;
}

QScrollBar:horizontal {
    background: #252833;
    height: 12px;
    margin: 2px;
    border: 1px solid #3A3F55;
    border-radius: 6px;
}

QScrollBar::handle:horizontal {
    background: #8A5CFF;
    min-width: 24px;
    border-radius: 6px;
}

QScrollBar::add-line, QScrollBar::sub-line,
QScrollBar::add-page, QScrollBar::sub-page {
    background: transparent;
    border: none;
}

QHeaderView::section {
    background-color: #252833;
    color: #E6E8FF;
    border: none;
    padding: 4px;
}

QLineEdit {
    background-color: #252833;
    color: #E6E8FF;
    border: 1px solid #3A3F55;
    border-radius: 4px;
}

/* =========================
   NARZĘDZIA
   ========================= */
QToolButton {
    background-color: transparent;
    border: none;
    border-radius: 4px;
    color: #E6E8FF;
    padding: 4px;
}

QToolButton:hover {
    background-color: #252833;
}

QToolButton:pressed {
    background-color: #1E2129;
}
"""

DROP_ZONE_QSS = """
    QLabel#dropArea {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgba(138, 92, 255, 0.25), stop:1 rgba(0, 229, 255, 0.08));
        border: 2px dashed #8A5CFF;
        border-radius: 10px;
        color: #8A5CFF;
        font-size: 18px;
    }
"""
