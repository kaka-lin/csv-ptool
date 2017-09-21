from PyQt5.QtWidgets import QMainWindow
from gui.ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__ (self, app, parent=None):
        super(MainWindow, self).__init__(parent)

        self._app = app

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._setup_ui()
    
    def _setup_ui(self):
        pass
