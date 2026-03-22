THEME_QSS = """
/* =========================
   MOTYW SYSTEMOWY
   (Pozostawiamy puste, aby zachować natywny wygląd OS)
   ========================= */

/* QMainWindow - System default */
/* QDialog - System default */

/* =========================
   RAMKI / PANELE
   ========================= */
/* QFrame - System default */

/* =========================
   TEKST
   ========================= */
/* QLabel - System default */

/* =========================
   PRZYCISKI
   ========================= */
/* QPushButton - System default */

/* =========================
   PRZYCISK WYKONAJ (AKCENT)
   ========================= */
/* QPushButton#runButton - System default */

/* =========================
   SUWAK SKALI
   ========================= */
/* QSlider - System default */

/* =========================
   KONTROLKI FORMULARZY
   ========================= */
/* QComboBox - System default */
/* QListView, QTreeView - System default */
/* QHeaderView - System default */
/* QLineEdit - System default */

QScrollBar:vertical {
    background: palette(base);
    width: 12px;
    margin: 2px;
    border: 1px solid palette(mid);
    border-radius: 6px;
}

QScrollBar::handle:vertical {
    background: palette(highlight);
    min-height: 24px;
    border-radius: 6px;
}

QScrollBar:horizontal {
    background: palette(base);
    height: 12px;
    margin: 2px;
    border: 1px solid palette(mid);
    border-radius: 6px;
}

QScrollBar::handle:horizontal {
    background: palette(highlight);
    min-width: 24px;
    border-radius: 6px;
}

QScrollBar::add-line, QScrollBar::sub-line,
QScrollBar::add-page, QScrollBar::sub-page {
    background: transparent;
    border: none;
}

/* =========================
   NARZĘDZIA
   ========================= */
/* QToolButton - System default */
"""

DROP_ZONE_QSS = """
    QLabel#dropArea {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgba(128, 128, 128, 0.2), stop:1 rgba(128, 128, 128, 0.05));
        border: 2px dashed palette(mid);
        border-radius: 8px;
        color: palette(text);
        font-size: 16px;
    }
"""
