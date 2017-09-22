import os, sys
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from gui.ui_mainwindow import Ui_MainWindow
from app.csv_handle import CSVHandle
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pyplot as plt

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
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.ui.verticalLayout.addWidget(self.canvas)
        
    
    def onOpenFile(self):
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

        if file_name[0]:
            csv_handle = CSVHandle()
            data = csv_handle.read(file_name[0])
        
        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.plot(data)

        self.canvas.draw()
        
