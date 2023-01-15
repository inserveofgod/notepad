from PyQt5.QtGui import QTextCharFormat, QTextCursor, QColor
from PyQt5.QtWidgets import QPlainTextEdit

from model.model import Model
from views.FindDialog import FindDialog


class FindController:
    def __init__(self):
        # model
        self.model = Model()

        # view
        self.findDialog = FindDialog(self)

        # text area field

        self.textArea = None

    def main(self, area: QPlainTextEdit):
        self.findDialog.main()
        self.textArea = area

    def find(self) -> dict:
        fmt = QTextCharFormat()
        fmt.setBackground(QColor("#5F9EA0"))
        fmt.setForeground(QColor("white"))

        cursor = QTextCursor(self.textArea.document())

        target = self.findDialog.entry_find.text()
        content = str(self.textArea.toPlainText())
        index = content.find(target)
        fields = {
            'target': target,
            'content': content,
            'index': index
        }

        if index:
            cursor.setPosition(index, QTextCursor.MoveAnchor)
            cursor.setPosition(index + len(target), QTextCursor.KeepAnchor)
            cursor.setCharFormat(fmt)

        return fields

    def replace(self):
        fields = self.find()
        target = fields.get('target')
        content = str(fields.get('content'))
        index = fields.get('index')
        repl = self.findDialog.entry_replace.text()

        if index:
            content = content.replace(target, repl, 1)
            self.textArea.setPlainText(content)


