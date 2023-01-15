import json
import os

from PyQt5.QtGui import QIcon


class Model:
    def __init__(self):
        self.root = os.getcwd()
        self.config = self.read()

        self.encoding = "UTF-8"
        self.title = "Not Defteri"
        self.icon = "./assets/img/notebook.png"
        self.filename = None
        self.path = None
        self.changed = False
        self.file_filter = "Metin Belgeleri (*.txt);;Tüm Dosyalar (*.*)"

        self.new_icon = QIcon("./assets/img/document--plus.png")
        self.new_window_icon = QIcon("./assets/img/newspapers.png")
        self.open_icon = QIcon("./assets/img/document-import.png")
        self.save_icon = QIcon("./assets/img/disk-return.png")
        self.save_as_icon = QIcon("./assets/img/disks.png")
        self.print_icon = QIcon("./assets/img/printer.png")
        self.exit_icon = QIcon("./assets/img/door-open-in.png")
        self.select_all_icon = QIcon("./assets/img/selection-select.png")
        self.undo_icon = QIcon("./assets/img/arrow-turn-180-left.png")
        self.redo_icon = QIcon("./assets/img/arrow-turn.png")
        self.cut_icon = QIcon("./assets/img/scissors.png")
        self.copy_icon = QIcon("./assets/img/document-copy.png")
        self.paste_icon = QIcon("./assets/img/clipboard-paste.png")
        self.find_icon = QIcon("./assets/img/magnifier.png")
        self.replace_icon = QIcon("./assets/img/magnifier--pencil.png")
        self.clock_icon = QIcon("./assets/img/sort-date.png")
        self.full_icon = QIcon("./assets/img/application-resize-full.png")
        self.menu_icon = QIcon("./assets/img/ui-menu.png")
        self.toolbar_icon = QIcon("./assets/img/ui-toolbar.png")
        self.fg_icon = QIcon("./assets/img/highlighter-color.png")
        self.bg_icon = QIcon("./assets/img/paint-can-color.png")
        self.font_icon = QIcon("./assets/img/layer-shape-text.png")
        self.help_icon = QIcon("./assets/img/question.png")
        self.about_icon = QIcon("./assets/img/information.png")

    def new(self) -> None:
        """
        ayarları sıfırlar
        :rtype: None
        """
        self.config = {
            'fg': '#000000',
            'bg': '#ffffff',
            'font-family': 'Arial',
            'font-style': 'normal',
            'font-size': 14,
        }

        self._write()

    def _write(self) -> None:
        """
        Sınıf içerisinde dosyaya yazmak için kullanılmalıdır.
        :rtype: None
        """
        dumping = json.dumps(self.config, indent=4, sort_keys=True)

        with open(os.path.join(self.root, "model", "config.json"), "w") as f:
            f.write(dumping)

        style = f"""
            color: {self.config.get('fg')};
            background-color: {self.config.get('bg')};
            font-family: '{self.config.get('font-family')}';
            font-style: {self.config.get('font-style')};
            font-size: {self.config.get('font-size')}pt;
            """

        field = """@charset "UTF-8";\nQPlainTextEdit{"""
        field += style
        field += "}"
        field = field.replace(' ', '')
        field = field.replace('\n', '')

        with open(os.path.join(self.root, "./assets/css/style.min.css"), 'w') as f:
            f.write(field)

    def update(self, key: str, value: any) -> None:
        """
        Belli bir ayarı değiştirmek ve kaydetmek için kullanılır
        :rtype: None
        """
        self.config = self.read()
        self.config[key] = value
        self._write()

    def read(self) -> dict:
        """
        Ayarları okutur ve geri döndürür
        :rtype: dict
        """
        with open(os.path.join(self.root, "model", "config.json")) as f:
            json_data = f.read()
            dict_data = json.loads(json_data)
            self.config = dict_data
            return dict_data

    def read_stylesheets(self) -> str:
        """
        json dosyasından alınıp css dosyasına yazılan verileri döndürür
        :rtype: str
        """
        with open(os.path.join(self.root, "./assets/css/style.min.css")) as f:
            return f.read()
