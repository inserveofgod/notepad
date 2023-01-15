from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self, controller):
        super(MainWindow, self).__init__()

        self.controller = controller
        self.main_layout = QHBoxLayout(self)

        self.screen_width = self.screen().geometry().width()
        self.screen_height = self.screen().geometry().height()
        self.default_width = self.screen_width // 3
        self.default_height = self.screen_height // 3

    def main(self):
        self.setWindowTitle("Not Defteri")
        self.setGeometry((self.screen_width - self.default_width) // 2, (self.screen_height - self.default_height) // 2,
                         self.default_width, self.default_height)
        self.setWindowIcon(QIcon(self.controller.model.icon))
        self.setLayout(self.main_layout)
        self.show()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        if self.controller.action_exit():
            a0.accept()
            return None

        a0.ignore()
