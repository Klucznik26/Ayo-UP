from PySide6.QtWidgets import QLabel


class DropImageLabel(QLabel):
    def __init__(self, parent=None, on_drop=None):
        super().__init__(parent)
        self.on_drop = on_drop
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if not urls:
            return

        path = urls[0].toLocalFile()
        if path.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            if self.on_drop:
                self.on_drop(path)
