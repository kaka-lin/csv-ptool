import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from gui.ui_plotbox import Ui_PlotBox
from app.csv_handle import CSVHandle
import matplotlib.pyplot as plt
import numpy as np

class PlotBox(QtWidgets.QGroupBox):
    """ Serial number edit box """
    def __init__(self, parent=None):
        super(PlotBox, self).__init__(parent)

        self.data = []
        self.isHaveData = False

        self.ui = Ui_PlotBox()
        self.ui.setupUi(self)
        self._setup_ui()

    def _setup_ui(self):
        """ """
    
    def openFile(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Open file')

        self.ui.fileName_lineEdit.setText(file)

        if file:
            csv_handle = CSVHandle()
            self.data = csv_handle.read(file)
            self.isHaveData = True
        
    def plotData(self):
        
        if self.isHaveData:
            ax = self.ui.figure.add_subplot(111)
            ax.clear()
            ax.plot(self.data[1: ,1])
            ax.set_ylabel(self.data[0][1])
            self.ui.canvas.draw()
        else:
            print('NO Data!')
