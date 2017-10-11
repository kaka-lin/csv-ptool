from PyQt5 import QtCore, QtGui, QtWidgets
from gui.plotbox import PlotBox

class AgilentTab(QtWidgets.QVBoxLayout):
    def __init__(self, parent=None):
        super(AgilentTab, self).__init__(parent)

        self.plot_box = PlotBox('A')

        self.addWidget(self.plot_box)
      
        self._setup_ui()
    
    def _setup_ui(self):
        self.retranslateUi()
    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
