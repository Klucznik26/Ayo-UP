THEME_QSS = """
/* =========================
   MOTYW ARCTIC (NEON ICE)
   ========================= */

QMainWindow {
    background-color: #0B3A5A;
}

QDialog {
    background-color: #0B3A5A;
    color: #A0E6FF;
}

/* =========================
   LEWY PASEK BOCZNY (SIDEBAR)
   ========================= */
QFrame#leftPanel,
QFrame#narrowPanel,
QFrame#sidebar,
QFrame[objectName="sidebar"] {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #005F8F, stop:1 #003D5C);
    border-right: 2px solid #00DDEB;
    border-left: none;
    border-top: none;
    border-bottom: none;
}

/* =========================
   RAMKI / PANELE GŁÓWNE
   ========================= */
QFrame {
    background-color: #003D5C;
    border: 1px solid #00DDEB;
    border-radius: 2px;
}

/* =========================
   TEKST
   ========================= */
QLabel {
    color: #A0E6FF;
}

QLabel#titleLabel {
    color: #00FFFF;
    font-weight: bold;
}

/* =========================
   PRZYCISKI (LODOWE BLOKI)
   ========================= */
QPushButton {
    padding: 8px 14px;
    background-color: #005F8F;
    border: 1px solid #00DDEB;
    border-radius: 4px;
    color: #FFFFFF;
}

QPushButton:hover {
    background-color: #008CC7;
    border: 1px solid #70FFFF;
}

QPushButton:pressed {
    background-color: #003D5C;
}

/* =========================
   PRZYCISK WYKONAJ (MAX BŁĘKIT)
   ========================= */
QPushButton#runButton {
    background-color: #2E78A8;
    border: 2px solid #8FC9EE;
    color: #EAF7FF;
    font-weight: bold;
}

QPushButton#runButton:hover {
    background-color: #3B88BA;
    color: #F5FBFF;
}

QPushButton#runButton:pressed {
    background-color: #245F86;
    color: #E1F3FF;
}

/* =========================
   SUWAK I KONTROLKI
   ========================= */
QSlider::groove:horizontal {
    height: 8px;
    background: #003D5C;
    border: 1px solid #00DDEB;
}

QSlider::handle:horizontal {
    background: #FFFFFF;
    border: 2px solid #00FFFF;
    width: 18px;
}

/* =========================
   LISTY I INPUTY
   ========================= */
QLineEdit, QComboBox, QListView {
    background-color: #004E7A;
    color: #FFFFFF;
    border: 2px solid #00DDEB;
}

QListView::item:selected,
QTreeView::item:selected,
QTreeWidget::item:selected {
    background-color: #00FFFF;
    color: #002B45;
}

QScrollBar:vertical {
    background: #004E7A;
    width: 12px;
    margin: 2px;
    border: 1px solid #00DDEB;
    border-radius: 6px;
}

QScrollBar::handle:vertical {
    background: #00FFFF;
    min-height: 24px;
    border-radius: 6px;
}

QScrollBar::handle:vertical:hover {
    background: #70FFFF;
}

QScrollBar:horizontal {
    background: #004E7A;
    height: 12px;
    margin: 2px;
    border: 1px solid #00DDEB;
    border-radius: 6px;
}

QScrollBar::handle:horizontal {
    background: #00FFFF;
    min-width: 24px;
    border-radius: 6px;
}

QScrollBar::add-line, QScrollBar::sub-line,
QScrollBar::add-page, QScrollBar::sub-page {
    background: transparent;
    border: none;
}

/* =========================
   TOOL BUTTONS
   ========================= */
QToolButton {
    color: #00FFFF;
    icon-size: 32px;
}

QToolButton:hover {
    background-color: rgba(0, 255, 255, 0.2);
    border: 1px solid #00FFFF;
}
"""

DROP_ZONE_QSS = """
    QLabel#dropArea {
        border: 2px dashed #00DDEB;
        border-radius: 8px;
        color: #A0E6FF;
        font-size: 16px;
        background: qlineargradient(
            x1:0, y1:0, x2:1, y2:1,
            stop:0 rgba(0, 255, 255, 0.22),
            stop:1 rgba(0, 94, 143, 0.10)
        );
    }
"""
