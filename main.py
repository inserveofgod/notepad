import sys
from controllers.MainController import MainController
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainController = MainController()
    mainController.menu()
    mainController.text_area()
    mainController.main()

    app.exec()
