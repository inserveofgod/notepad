from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QAction


class Actions:
    def __init__(self, controller):
        self.controller = controller
        self.model = self.controller.model

        self.file_new = QAction(self.model.new_icon, "Yeni")
        self.file_new_window = QAction(self.model.new_window_icon, "Yeni Pencere")
        self.file_open = QAction(self.model.open_icon, "Aç")
        self.file_save = QAction(self.model.save_icon, "Kaydet")
        self.file_save_as = QAction(self.model.save_as_icon, "Farklı Kaydet")
        self.file_print = QAction(self.model.print_icon, "Yazdır")
        self.file_exit = QAction(self.model.exit_icon, "Çık")

        self.edit_select_all = QAction(self.model.select_all_icon, "Hepsini Seç")
        self.edit_undo = QAction(self.model.undo_icon, "Geri al")
        self.edit_redo = QAction(self.model.redo_icon, "İleri al")
        self.edit_cut = QAction(self.model.cut_icon, "Kes")
        self.edit_copy = QAction(self.model.copy_icon, "Kopyala")
        self.edit_paste = QAction(self.model.paste_icon, "Yapıştır")
        self.edit_find = QAction(self.model.find_icon, "Bul")
        self.edit_replace = QAction(self.model.replace_icon, "Değiştir")
        self.edit_datetime = QAction(self.model.clock_icon, "Tarih & Saat")

        self.view_full = QAction(self.model.full_icon, "Tam Ekran")
        self.view_toggle_menu = QAction(self.model.menu_icon, "Menü Göster/Gizle")
        self.view_toggle_toolbar = QAction(self.model.toolbar_icon, "Araç Çubuğu Göster/Gizle")

        self.settings_fg = QAction(self.model.fg_icon, "Yazı Rengi")
        self.settings_bg = QAction(self.model.bg_icon, "Arkaplan Rengi")
        self.settings_font = QAction(self.model.font_icon, "Font Ayarları")

        self.help_help = QAction(self.model.help_icon, "Yardım")
        self.help_about = QAction(self.model.about_icon, "Hakkında")

    def shortcuts(self):
        self.file_new.setShortcut(QKeySequence("Ctrl+N"))
        self.file_new_window.setShortcut(QKeySequence("Ctrl+Shift+N"))
        self.file_open.setShortcut(QKeySequence("Ctrl+O"))
        self.file_save.setShortcut(QKeySequence("Ctrl+S"))
        self.file_save_as.setShortcut(QKeySequence("Ctrl+Shift+S"))
        self.file_print.setShortcut(QKeySequence("Ctrl+P"))
        self.file_exit.setShortcut(QKeySequence("Alt+F4"))

        self.edit_select_all.setShortcut(QKeySequence("Ctrl+A"))
        self.edit_undo.setShortcut(QKeySequence("Ctrl+Z"))
        self.edit_redo.setShortcut(QKeySequence("Ctrl+Y"))
        self.edit_cut.setShortcut(QKeySequence("Ctrl+X"))
        self.edit_copy.setShortcut(QKeySequence("Ctrl+C"))
        self.edit_paste.setShortcut(QKeySequence("Ctrl+V"))
        self.edit_find.setShortcut(QKeySequence("Ctrl+F"))
        self.edit_replace.setShortcut(QKeySequence("Ctrl+R"))
        self.edit_datetime.setShortcut(QKeySequence("F5"))

        self.view_full.setShortcut(QKeySequence("F11"))
        self.view_toggle_menu.setShortcut(QKeySequence("Ctrl+Shift+M"))
        self.view_toggle_toolbar.setShortcut(QKeySequence("Ctrl+Shift+T"))

        self.settings_fg.setShortcut(QKeySequence("Ctrl+Shift+T"))
        self.settings_bg.setShortcut(QKeySequence("Ctrl+Shift+B"))
        self.settings_font.setShortcut(QKeySequence("Ctrl+Shift+F"))

        self.help_help.setShortcut(QKeySequence("Ctrl+H"))
        self.help_about.setShortcut(QKeySequence("Ctrl+Shift+O"))

    def checks(self):
        self.view_full.setCheckable(True)
        self.view_full.setChecked(False)

        self.view_toggle_menu.setCheckable(True)
        self.view_toggle_menu.setChecked(True)

        self.view_toggle_toolbar.setCheckable(True)
        self.view_toggle_toolbar.setChecked(True)

    def triggers(self):
        self.file_new.triggered.connect(self.controller.action_file_new)
        self.file_new_window.triggered.connect(self.controller.action_file_new_window)
        self.file_open.triggered.connect(self.controller.action_file_open)
        self.file_save.triggered.connect(self.controller.action_file_save)
        self.file_save_as.triggered.connect(self.controller.action_file_save_as)
        self.file_print.triggered.connect(self.controller.action_file_print)
        self.file_exit.triggered.connect(self.controller.action_file_exit)

        self.edit_select_all.triggered.connect(self.controller.action_edit_select_all)
        self.edit_undo.triggered.connect(self.controller.action_edit_undo)
        self.edit_redo.triggered.connect(self.controller.action_edit_redo)
        self.edit_cut.triggered.connect(self.controller.action_edit_cut)
        self.edit_copy.triggered.connect(self.controller.action_edit_copy)
        self.edit_paste.triggered.connect(self.controller.action_edit_paste)
        self.edit_find.triggered.connect(self.controller.action_edit_find)
        self.edit_replace.triggered.connect(self.controller.action_edit_replace)
        self.edit_datetime.triggered.connect(self.controller.action_edit_datetime)

        self.view_full.triggered.connect(self.controller.action_view_full)
        self.view_toggle_menu.triggered.connect(self.controller.action_view_menu)
        self.view_toggle_toolbar.triggered.connect(self.controller.action_view_toolbar)

        self.settings_fg.triggered.connect(self.controller.action_settings_fg)
        self.settings_bg.triggered.connect(self.controller.action_settings_bg)
        self.settings_font.triggered.connect(self.controller.action_settings_font)

        self.help_help.triggered.connect(self.controller.action_help_help)
        self.help_about.triggered.connect(self.controller.action_help_about)
