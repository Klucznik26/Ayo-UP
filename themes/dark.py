DARK_THEME = """
/* =========================
   OKNO GŁÓWNE
   ========================= */
QMainWindow {
    background-color: #2F2A25;  /* ciepły, miedziany ciemny */
}

/* =========================
   RAMKI / PANELE
   ========================= */
QFrame {
    background-color: #3A342E;
    border: 1px solid #4A423B;
}

/* =========================
   TEKST
   ========================= */
QLabel {
    color: #E6DED2;   /* jaśniejszy — czytelny */
}

QLabel[secondary="true"] {
    color: #B8AFA3;   /* pomocniczy */
}

/* =========================
   PRZYCISKI – STANDARD
   ========================= */
QPushButton {
    padding: 8px 14px;
    background-color: #3E3832;
    border: 1px solid #5A5248;
    border-radius: 8px;
    color: #E8E2D8;
}

QPushButton:hover {
    background-color: #4A433C;
}

QPushButton:pressed {
    background-color: #352F2A;
}

QPushButton:disabled {
    background-color: #2E2925;
    color: #8F8578;
    border-color: #3A342E;
}

/* =========================
   PRZYCISK WYKONAJ (AKCENT)
   ========================= */
QPushButton#runButton {
    background-color: #9C5532;   /* cegła */
    border: none;
    color: #FFFFFF;
}

QPushButton#runButton:hover {
    background-color: #B35E34;
}

QPushButton#runButton:pressed {
    background-color: #864A2C;
}

/* =========================
   SUWAK SKALI
   ========================= */
QSlider::groove:horizontal {
    height: 6px;
    background: #4A433C;
    border-radius: 3px;
}

QSlider::handle:horizontal {
    background: #C96A3A;
    width: 16px;
    margin: -5px 0;
    border-radius: 8px;
}

QSlider::sub-page:horizontal {
    background: #7A4A32;
    border-radius: 3px;
}

QSlider::add-page:horizontal {
    background: #3E3832;
    border-radius: 3px;
}

/* =========================
   DIALOGI (Wybór plików, Ustawienia)
   ========================= */
QDialog {
    background-color: #2F2A25;
    color: #E6DED2;
}

QTreeView, QListView {
    background-color: #3A342E;
    color: #E6DED2;
    border: 1px solid #4A423B;
    outline: none;
}

QTreeView::item:selected, QListView::item:selected {
    background-color: #9C5532;
    color: #FFFFFF;
}

QHeaderView::section {
    background-color: #3E3832;
    color: #E6DED2;
    border: none;
    padding: 4px;
}

QLineEdit {
    background-color: #3A342E;
    color: #E6DED2;
    border: 1px solid #5A5248;
    border-radius: 4px;
}

QComboBox {
    background-color: #3E3832;
    color: #E6DED2;
    border: 1px solid #5A5248;
    padding: 4px;
}

QComboBox::drop-down {
    border: none;
}

/* =========================
   NARZĘDZIA (np. nawigacja w QFileDialog)
   ========================= */
QToolButton {
    background-color: transparent;
    border: none;
    border-radius: 4px;
    color: #E6DED2;
    padding: 4px;
}

QToolButton:hover {
    background-color: #4A433C;
}

QToolButton:pressed {
    background-color: #352F2A;
}
"""