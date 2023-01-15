from PyQt5.QtPrintSupport import QPrintDialog


class PrintDialog(QPrintDialog):
    def __init__(self, controller):
        super(PrintDialog, self).__init__()
        self.controller = controller
