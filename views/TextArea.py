from PyQt5.QtWidgets import QPlainTextEdit


class TextArea(QPlainTextEdit):
    def __init__(self, controller):
        super(TextArea, self).__init__()

        self.controller = controller
        self.win = self.controller.main_view
        self.textChanged.connect(self.controller.make_changed)
        self.model = self.controller.model
        self.config = self.model.config

        self._stylesheets()

    def main(self):
        self.win.layout().addWidget(self)
        self.win.setCentralWidget(self)

    def _stylesheets(self):
        styles = self.model.read_stylesheets()
        self.setStyleSheet(styles)

    def refresh(self):
        self._stylesheets()
