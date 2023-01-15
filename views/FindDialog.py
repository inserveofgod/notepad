from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QLineEdit, QFormLayout, QPushButton, QHBoxLayout


class FindDialog(QDialog):
    def __init__(self, controller):
        super(FindDialog, self).__init__()

        self.controller = controller
        self.model = self.controller.model
        self.main_layout = QFormLayout()
        self.btn_layout = QHBoxLayout()

        self.entry_find = QLineEdit()
        self.entry_replace = QLineEdit()

        self.btn_find = QPushButton(self.model.find_icon, "Bul")
        self.btn_replace = QPushButton(self.model.replace_icon, "Değiştir")

        self._settings()
        self._add()
        self._listeners()

    def main(self):
        self.show()

    def _settings(self):
        self.setFixedSize(300, 100)
        self.setWindowTitle(self.model.title)
        self.setWindowIcon(QIcon(self.model.icon))
        self.setLayout(self.main_layout)

    def _add(self):
        self.main_layout.addRow("Bul : ", self.entry_find)
        self.main_layout.addRow("Değiştir : ", self.entry_replace)
        self.main_layout.addRow(self.btn_layout)

        self.btn_layout.addWidget(self.btn_find)
        self.btn_layout.addWidget(self.btn_replace)

    def _listeners(self):
        self.btn_find.clicked.connect(self.controller.find)
        self.btn_replace.clicked.connect(self.controller.replace)
