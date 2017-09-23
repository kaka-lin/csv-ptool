import os, sys
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from gui.ui_mainwindow import Ui_MainWindow
from gui.hiokitab import HiokiTab

class MainWindow(QMainWindow):
    def __init__ (self, app, translator, parent=None):
        super(MainWindow, self).__init__(parent)

        self._app = app
        self._translator = translator
        app.installTranslator(translator)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._setup_ui()
    
    def _setup_ui(self):
        self._hioki_tab = HiokiTab(self.ui.tab)
        
    
    def openFile(self):
        '''
        print(__file__) # /Users/kakalin/csv/gui/mainwindow.py
        print (os.path.dirname(__file__)) # /Users/kakalin/csv/gui
        print (os.path.abspath(__file__)) # /Users/kakalin/csv/gui/mainwindow.py
        print (os.path.abspath(os.path.dirname(__file__))) # /Users/kakalin/csv/gui
        print (os.path.dirname(os.path.abspath(__file__))) # /Users/kakalin/csv/gui
        '''

        dir = os.path.dirname(__file__)

        file_name = QFileDialog.getOpenFileName(self, 'Open file', dir)
        print(file_name)
