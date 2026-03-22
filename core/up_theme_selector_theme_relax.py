THEME_QSS = """
/* =========================
   MOTYW RELAKSACYJNY (NATURE)
   ========================= */

QMainWindow {
    background-color: #C0D3AC;
}

QDialog {
    background-color: #C0D3AC;
    color: #2F3E36;
}

/* =========================
   RAMKI / PANELE
   ========================= */
QFrame {
    background-color: #E7E3D8;
    border: 1px solid #88B283;
}

/* =========================
   TEKST
   ========================= */
QLabel {
    color: #2F3E36;
}

QLabel[secondary="true"] {
    color: #6B7F72;
}

/* =========================
   PRZYCISKI
   ========================= */
QPushButton {
    padding: 8px 14px;
    background-color: #E7E3D8;
    border: 1px solid #88B283;
    border-radius: 6px;
    color: #2F3E36;
}

QPushButton:hover {
    background-color: #F2EFE7;
}

QPushButton:pressed {
    background-color: #D7D3C8;
}

QPushButton:disabled {
    background-color: #C9D2BE;
    color: #6B7F72;
    border: 1px solid #88B283;
}

/* =========================
   PRZYCISK WYKONAJ (AKCENT)
   ========================= */
QPushButton#runButton {
    background-color: #73AE74;
    border: none;
    color: #FFFFFF;
}

QPushButton#runButton:hover {
    background-color: #98C998;
}

QPushButton#runButton:pressed {
    background-color: #5B8A5E;
}

/* =========================
   SUWAK SKALI
   ========================= */
QSlider::groove:horizontal {
    height: 6px;
    background: #E7E3D8;
    border-radius: 3px;
}

QSlider::handle:horizontal {
    background: #73AE74;
    width: 16px;
    margin: -5px 0;
    border-radius: 8px;
}

QSlider::sub-page:horizontal {
    background: #5B8A5E;
    border-radius: 3px;
}

QSlider::add-page:horizontal {
    background: #E7E3D8;
    border-radius: 3px;
}

/* =========================
   KONTROLKI FORMULARZY
   ========================= */
QComboBox {
    background-color: #F0EDE5;
    color: #2F3E36;
    border: 1px solid #88B283;
    padding: 4px;
}

QComboBox::drop-down {
    border: none;
}

QListView, QTreeView {
    background-color: #F0EDE5;
    color: #2F3E36;
    border: 1px solid #88B283;
    outline: none;
}

QTreeView::item:selected, QListView::item:selected {
    background-color: #73AE74;
    color: #FFFFFF;
}

QScrollBar:vertical {
    background: #F0EDE5;
    width: 12px;
    margin: 2px;
    border: 1px solid #88B283;
    border-radius: 6px;
}

QScrollBar::handle:vertical {
    background: #73AE74;
    min-height: 24px;
    border-radius: 6px;
}

QScrollBar::handle:vertical:hover {
    background: #98C998;
}

QScrollBar:horizontal {
    background: #F0EDE5;
    height: 12px;
    margin: 2px;
    border: 1px solid #88B283;
    border-radius: 6px;
}

QScrollBar::handle:horizontal {
    background: #73AE74;
    min-width: 24px;
    border-radius: 6px;
}

QScrollBar::add-line, QScrollBar::sub-line,
QScrollBar::add-page, QScrollBar::sub-page {
    background: transparent;
    border: none;
}

QHeaderView::section {
    background-color: #E7E3D8;
    color: #2F3E36;
    border: none;
    padding: 4px;
}

QLineEdit {
    background-color: #F0EDE5;
    color: #2F3E36;
    border: 1px solid #88B283;
    border-radius: 4px;
}

/* =========================
   NARZĘDZIA
   ========================= */
QToolButton {
    background-color: transparent;
    border: none;
    border-radius: 4px;
    color: #2F3E36;
    padding: 4px;
}

QToolButton:hover {
    background-color: #E7E3D8;
}

QToolButton:pressed {
    background-color: #D7D3C8;
}
"""

DROP_ZONE_QSS = """
    QLabel#dropArea {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgba(115, 174, 116, 0.25), stop:1 rgba(115, 174, 116, 0.05));
        border: 2px dashed #73AE74;
        border-radius: 10px;
        color: #73AE74;
        font-size: 18px;
    }
"""
