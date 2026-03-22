THEME_QSS = """
/* =========================
   MOTYW CIEMNY (AYO DARK)
   ========================= */

QMainWindow, QDialog, QWidget#main_widget {
    background-color: #0F1412;
    color: #CFE8DC;
}

/* =========================
   RAMKI / PANELE
   ========================= */
QFrame#narrowPanel, 
QFrame#leftPanel, 
QFrame#rightPanel, 
QFrame#glassPanel {
    background-color: #161D1A;
    border-radius: 14px;
    border: 1px solid #1F2A25;
}

/* =========================
   TEKST
   ========================= */
QLabel {
    color: #CFE8DC;
}

QLabel[secondary="true"] {
    color: #7FAF9D;
}

/* =========================
   PRZYCISKI
   ========================= */
QPushButton {
    background-color: #1C2622;
    color: #CFE8DC;
    border: 1px solid #25332D;
    border-radius: 8px;
    padding: 8px 12px;
}

QPushButton:hover {
    background-color: #1F3A30;
    border: 1px solid #04E38A;
    color: #E6FFF6;
}

QPushButton:pressed {
    background-color: #04E38A;
    color: #0F1412;
}

QPushButton:disabled {
    background-color: #121917;
    color: rgba(207, 232, 220, 0.4);
    border: 1px solid #1F2A25;
}

/* =========================
   PRZYCISK WYKONAJ (AKCENT)
   ========================= */
QPushButton#runButton {
    background-color: #1F3A30;
    border: 1px solid #25332D;
    color: #04E38A;
    font-weight: bold;
}

QPushButton#runButton:hover {
    background-color: #04E38A;
    border: 1px solid #04E38A;
    color: #0F1412;
}

QPushButton#runButton:pressed {
    background-color: #03B86F;
}

/* =========================
   SUWAK SKALI
   ========================= */
QSlider::groove:horizontal {
    height: 6px;
    background: #121917;
    border-radius: 3px;
}

QSlider::handle:horizontal {
    background: #04E38A;
    width: 16px;
    margin: -5px 0;
    border-radius: 8px;
}

QSlider::sub-page:horizontal {
    background: #1F3A30;
    border-radius: 3px;
}

QSlider::add-page:horizontal {
    background: #121917;
    border-radius: 3px;
}

/* =========================
   KONTROLKI FORMULARZY
   ========================= */
QComboBox {
    background-color: #121917;
    color: #CFE8DC;
    border: 1px solid #25332D;
    padding: 4px;
    border-radius: 6px;
}

QComboBox::drop-down {
    border: none;
}

QListView, QTreeView, QTableWidget {
    background-color: #121917;
    color: #E0E0E0;
    border: 1px solid #25332D;
    border-radius: 6px;
    outline: none;
}

QListView::item:hover, QTreeView::item:hover, QTableWidget::item:hover {
    background-color: #1F3A30;
    color: #E6FFF6;
}

QListView::item:selected, QTreeView::item:selected, QTableWidget::item:selected {
    background-color: #04E38A;
    color: #0F1412;
}

QScrollBar:vertical {
    background: #121917;
    width: 12px;
    margin: 2px;
    border-radius: 6px;
}

QScrollBar::handle:vertical {
    background: #25332D;
    min-height: 24px;
    border-radius: 6px;
}

QScrollBar::handle:vertical:hover {
    background: #04E38A;
}

QScrollBar:horizontal {
    background: #121917;
    height: 12px;
    margin: 2px;
    border-radius: 6px;
}

QScrollBar::handle:horizontal {
    background: #25332D;
    min-width: 24px;
    border-radius: 6px;
}

QScrollBar::add-line, QScrollBar::sub-line,
QScrollBar::add-page, QScrollBar::sub-page {
    background: transparent;
    border: none;
}

QHeaderView::section {
    background-color: #1C2622;
    color: #CFE8DC;
    border: none;
    border-right: 1px solid #25332D;
    border-bottom: 1px solid #25332D;
    padding: 4px;
}

/* =========================
   PROGRESS BAR
   ========================= */
QProgressBar {
    background-color: #121917;
    border: 1px solid #25332D;
    border-radius: 6px;
    text-align: center;
    color: #CFE8DC;
}

QProgressBar::chunk {
    background-color: #04E38A;
    border-radius: 5px;
}

QLineEdit {
    background-color: #121917;
    color: #CFE8DC;
    border: 1px solid #25332D;
    border-radius: 6px;
    padding: 5px;
}

QLineEdit:focus {
    border: 1px solid #04E38A;
    background-color: #161D1A;
}

/* =========================
   NARZĘDZIA
   ========================= */
QToolButton {
    background-color: transparent;
    border: none;
    border-radius: 4px;
    color: #7FAF9D;
    padding: 4px;
}

QToolButton:hover {
    background-color: rgba(4, 227, 138, 0.15);
    color: #04E38A;
}

QToolButton:pressed {
    background-color: #04E38A;
    color: #0F1412;
}

/* =========================
   IKONY (LEWY PANEL)
   ========================= */
QFrame#narrowPanel QPushButton#iconButton {
    background-color: transparent;
    border: none;
    border-radius: 10px;
    font-size: 20px;
    color: #7FAF9D;
}

QFrame#narrowPanel QPushButton#iconButton:hover {
    background-color: rgba(4, 227, 138, 0.15);
    color: #04E38A;
}

QFrame#narrowPanel QPushButton#iconButton[danger="true"]:hover {
    background-color: #8B2E3C;
    color: white;
}
"""

DROP_ZONE_QSS = """
    QLabel#dropArea {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #0B0F0E, stop:1 #121A17);
        border: 1px solid rgba(255, 255, 255, 0.03);
        border-radius: 14px;
        padding: 15px;
        color: #CFE8DC;
        font-size: 16px;
    }
"""
