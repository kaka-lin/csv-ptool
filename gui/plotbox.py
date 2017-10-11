import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from gui.ui_plotbox import Ui_PlotBox
from app.csv_handle import CSVHandle
import matplotlib.pyplot as plt
import numpy as np

class PlotBox(QtWidgets.QGroupBox):
    """ Serial number edit box """
    def __init__(self, _class, parent=None):
        super(PlotBox, self).__init__(parent)

        self._class = _class

        self.data = []
        self.data_title = []
        self.isHaveData = False

        self.ui = Ui_PlotBox()
        self.ui.setupUi(self)
        self._setup_ui()

    def _setup_ui(self):
        """ """
    
    def openFile(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Open file')

        self.ui.fileName_lineEdit.setText(file)

        self.readData(file)
    
    def readData(self, file=None):
        if file:
            csv_handle = CSVHandle()
            if self._class == 'H':
                self.data, self.data_title = csv_handle.readHioki(file)
            else:
                self.data, self.data_title = csv_handle.read(file)

            self.isHaveData = True

            try:
                self.showItem()
            except Exception as  err:
                self.ui.statusbar.showMessage('Error: ' + str(err))
            except:
                #print('No data or data format wrong!')
                self.ui.statusbar.showMessage('No data or data format wrong!')
        else:
            self.data = []
            self.data_title = []
            self.isHaveData = False
            self.ui.model.clear()
            
    
    def showItem(self):
        self.ui.model.clear()
        if self.isHaveData:
            if self.data_title:
                for title in self.data_title[0]:
                    item = QtGui.QStandardItem(title)
                    item.setCheckable(True)
                    self.ui.model.appendRow(item)
            else:
                #print('No data or data format wrong!')
                self.ui.statusbar.showMessage('No data or data format wrong!')

        else:
            self.ui.model.clear()
        
        self.index = []
    
    def onItemChanged(self, item):
        if item.checkState():
            for i in range(len(self.data_title[0])):
                if item.text() == self.data_title[0][i]:
                    self.index.append(i)
        else:
            for i in range(len(self.data_title[0])):
                if item.text() == self.data_title[0][i]:
                    self.index.remove(i)
        
    def plotData(self):
        ax = self.ui.figure.add_subplot(111)
        if self.isHaveData:
            if self.index:
                ax.clear()
                for i in range(len(self.index)):
                    try:
                        ax.plot(self.data[0: , self.index[i]], label = self.data_title[0][self.index[i]])
                        ax.legend(loc='best')
                        ax.grid(linestyle='dashed', alpha=0.5)
                    except Exception as err:
                        #print('Error:', err)
                        self.ui.statusbar.showMessage('Error: ' + str(err))
                
                self.ui.figure.tight_layout()
                self.ui.canvas.draw()
            else:
                ax.clear()
                self.ui.canvas.draw()
        else:
            ax.clear()
            self.ui.canvas.draw()
            #print('NO Data!')
            self.ui.statusbar.showMessage('No Data!')
