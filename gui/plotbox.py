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

        self.ui = Ui_PlotBox()
        self.ui.setupUi(self)
        self._setup_ui()

    def _setup_ui(self):
        """ """
    

    def plotData(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file')

        if file_name[0]:
            csv_handle = CSVHandle()
            data = csv_handle.read(file_name[0])

        print(data[:, 1])
        
        ax = self.ui.figure.add_subplot(111)
        ax.clear()
        ax.plot(data[1: ,1])
        ax.set_ylabel(data[0][1])
        #ax.set_ylim(20, 40)
        

        self.ui.canvas.draw()
