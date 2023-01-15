import os
import time

from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import QFileDialog, QColorDialog, QFontDialog
from PyQt5.QtWidgets import QMessageBox, QDialog

from controllers.FindController import FindController
from model.model import Model
from views.MainWindow import MainWindow
from views.Menus import Menus
from views.PrintDialog import PrintDialog
from views.TextArea import TextArea


class MainController:
    def __init__(self):
        # model
        self.model = Model()

        # views
        self.main_view = MainWindow(self)
        self.menu_view = Menus(self)
        self.text_view = TextArea(self)
        self.printer_view = PrintDialog(self)

        # controllers
        self.findController = FindController()

    # private methods

    def _check_changes(self) -> int:
        confirm = QMessageBox.question(self.main_view, self.model.title,
                                       "Yaptığınız değişiklikleri kaydetmek istiyor musunuz?",
                                       QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        return confirm

    # initialize views

    def main(self) -> MainWindow:
        """
        ana pencere
        :rtype: MainWindow
        """
        self.main_view.main()
        return self.main_view

    def menu(self) -> Menus:
        """
        ana pencere menüleri
        :rtype: Menus
        """
        self.menu_view.triggers()
        self.menu_view.checks()
        self.menu_view.shortcuts()
        self.menu_view.main()
        return self.menu_view

    def text_area(self) -> TextArea:
        """
        ana pencere yazı kısmı
        :rtype: TextArea
        """
        self.text_view.main()
        return self.text_view

    # window event listeners

    def action_exit(self) -> bool:
        if self.model.changed:
            confirm = self._check_changes()

            if confirm == QMessageBox.Yes:
                self.action_file_save()
                return True

            if confirm == QMessageBox.Cancel:
                return False

        return True

    # text area event listeners

    def make_changed(self) -> None:
        if not self.model.changed:
            self.model.changed = True
            self.main_view.setWindowTitle(f"{self.main_view.windowTitle()} * ")

    # action listeners

    def action_file_new(self):
        if self.model.changed:
            confirm = self._check_changes()

            if confirm == QMessageBox.Cancel:
                return False

            if confirm == QMessageBox.Yes:
                self.action_file_save()

        self.model.changed = False
        self.model.path = None
        self.model.filename = None

        self.text_view.setPlainText("")
        self.main_view.setWindowTitle(self.model.title)

    @staticmethod
    def action_file_new_window():
        new_instance = MainController()
        new_instance.menu()
        new_instance.text_area()
        new_instance.main()

    def action_file_open(self):
        filename, ext = QFileDialog.getOpenFileName(self.main_view, "Dosya Aç", os.getcwd(), self.model.file_filter)
        if filename:
            # check if previous file is open
            if self.model.filename is not None and self.model.changed:
                self.action_file_save()

            try:
                with open(filename, 'r', encoding=self.model.encoding) as f:
                    data = f.read()
                    self.text_view.setPlainText(data)
                    self.model.filename = os.path.basename(filename)
                    self.model.path = filename
                    self.model.changed = False
                    self.main_view.setWindowTitle(self.model.title + f" - {self.model.filename} ")

            except FileNotFoundError:
                QMessageBox.warning(self.main_view, self.model.title, "Dosya bulunamadı!", QMessageBox.Ok)
                self.model.filename = None
                self.model.path = None
                self.model.changed = False
                self.text_view.setPlainText("")

    def action_file_save(self):
        text = self.text_view.toPlainText()

        try:
            with open(self.model.path, "w", encoding=self.model.encoding) as f:
                f.write(text)
                self.model.changed = False
                self.main_view.setWindowTitle(self.model.title + f" - {self.model.filename} ")

        except PermissionError:
            QMessageBox.warning(self.main_view, self.model.title, "Erişim reddedildi!", QMessageBox.Ok)

        except TypeError:
            self.action_file_save_as()

    def action_file_save_as(self):
        filename, ext = QFileDialog.getSaveFileName(self.main_view, "Dosya Kaydet", os.getcwd(), self.model.file_filter)
        if filename:
            self.model.filename = os.path.basename(filename)
            self.model.path = filename
            self.action_file_save()

    def action_file_print(self) -> None:
        if self.printer_view.exec() == QDialog.Accepted:
            self.text_view.print(self.printer_view.printer())

    def action_file_exit(self) -> None:
        self.main_view.close()

    def action_edit_select_all(self) -> None:
        self.text_view.selectAll()

    def action_edit_undo(self) -> None:
        self.text_view.undo()

    def action_edit_redo(self) -> None:
        self.text_view.redo()

    def action_edit_cut(self) -> None:
        self.text_view.cut()

    def action_edit_copy(self) -> None:
        self.text_view.copy()

    def action_edit_paste(self) -> None:
        self.text_view.paste()

    def action_edit_find(self):
        self.findController.main(self.text_view)

    def action_edit_replace(self):
        # one can change its mind about design, so keeping this function as it is
        self.action_edit_find()

    def action_edit_datetime(self) -> None:
        self.text_view.insertPlainText(time.ctime())

    def action_view_full(self) -> None:
        if self.main_view.isFullScreen():
            self.main_view.showNormal()

        else:
            self.main_view.showFullScreen()

    def action_view_menu(self) -> None:
        menubar = self.main_view.menuBar()

        if menubar.isVisible():
            menubar.setVisible(False)

        else:
            menubar.setVisible(True)

    def action_view_toolbar(self) -> None:
        pass

    def action_settings_fg(self):
        dialog = QColorDialog()
        color = QColor()
        fg = self.model.config.get('fg')

        color.setNamedColor(fg)
        color = dialog.getColor(color).name()

        if fg != color:
            self.model.update("fg", color)
            self.text_view.refresh()

    def action_settings_bg(self):
        dialog = QColorDialog()
        color = QColor()
        bg = self.model.config.get('bg')

        color.setNamedColor(bg)
        color = dialog.getColor(color).name()

        if bg != color:
            self.model.update("bg", color)
            self.text_view.refresh()

    def action_settings_font(self):
        dialog = QFontDialog()

        font_family = self.model.config.get('font-family')
        font_size = self.model.config.get('font-size')
        font_style = self.model.config.get('font-style')

        font = QFont()
        font.setFamily(font_family)
        font.setPointSize(font_size)
        font.setStyleName(font_style)

        font = dialog.getFont(font, self.main_view, "Font Seç")[0]
        style = font.style()

        if style == QFont.Bold:
            new_font_style = 'bold'

        elif style == QFont.StyleItalic:
            new_font_style = 'italic'

        elif style == QFont.Light:
            new_font_style = 'light'

        else:
            new_font_style = 'normal'

        self.model.update("font-family", font.family())
        self.model.update("font-size", font.pointSize())
        self.model.update("font-style", new_font_style)
        self.text_view.refresh()

    def action_help_help(self):
        QMessageBox.information(self.main_view, self.model.title,
                                "Program hakkında inserveofgod@gmail.com\nadresine mail gönderebilirsiniz",
                                QMessageBox.Ok)

    def action_help_about(self):
        QMessageBox.information(self.main_view, self.model.title,
                                "Bu program Python programalama dili ile PyQt5\n"
                                "kütüphanesi kullanılarak yapılmıştır.",
                                QMessageBox.Ok)

