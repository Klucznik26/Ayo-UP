CREATIVE_THEME = """
/* =========================
   MOTYW KREATYWNY (BLUE)
   ========================= */

QMainWindow {
    background-color: #1B262C;
}

QDialog {
    background-color: #1B262C;
}

/* =========================
   RAMKI / PANELE
   ========================= */
QFrame {
    background-color: #202d36;
    border: 1px solid #3282B8;
}

/* =========================
   TEKST
   ========================= */
QLabel {
    color: #BBE1FA;
}

QLabel[secondary="true"] {
    color: #566E7A;
}

QLabel#scaleLabel {
    color: #FFFFFF;
}

/* =========================
   PRZYCISKI
   ========================= */
QPushButton {
    padding: 8px 14px;
    background-color: #0F4C75;
    border: 1px solid #3282B8;
    border-radius: 6px;
    color: #BBE1FA;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #3282B8;
    color: #FFFFFF;
}

QPushButton:pressed {
    background-color: #0F4C75;
    border: 2px solid #BBE1FA;
}

QPushButton:disabled {
    background-color: #243441;
    color: #566E7A;
    border: 1px solid #2C3E50;
}

/* =========================
   PRZYCISK WYKONAJ (AKCENT)
   ========================= */
QPushButton#runButton {
    background-color: #3282B8;
    border: none;
    color: #FFFFFF;
}

QPushButton#runButton:hover {
    background-color: #5199C9;
}

QPushButton#runButton:pressed {
    background-color: #266590;
}

/* =========================
   SUWAK SKALI
   ========================= */
QSlider::groove:horizontal {
    height: 6px;
    background: #0F4C75;
    border-radius: 3px;
}

QSlider::handle:horizontal {
    background: #3282B8;
    width: 16px;
    margin: -5px 0;
    border-radius: 8px;
}

QSlider::sub-page:horizontal {
    background: #BBE1FA;
    border-radius: 3px;
}

QSlider::add-page:horizontal {
    background: #0F4C75;
    border-radius: 3px;
}

/* =========================
   KONTROLKI FORMULARZY
   ========================= */
QComboBox {
    background-color: #0F4C75;
    color: #BBE1FA;
    border: 1px solid #3282B8;
    padding: 4px;
}

QComboBox::drop-down {
    border: none;
}

QListView, QTreeView {
    background-color: #202d36;
    color: #BBE1FA;
    border: 1px solid #3282B8;
}
"""

DROP_ZONE = """
    QLabel {
        background-color: #0F4C75;
        border: 2px dashed #3282B8;
        border-radius: 10px;
        color: #BBE1FA;
        font-size: 18px;
    }
"""