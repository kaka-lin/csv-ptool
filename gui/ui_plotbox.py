from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

class Ui_PlotBox(object):
    def setupUi(self, plotBox):
        plotBox.setObjectName("plotBox")

        self.gridLayout = QtWidgets.QGridLayout(plotBox)
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setVerticalSpacing(12)
    
        self.open_button = QtWidgets.QPushButton(plotBox)
        self.open_button.setObjectName("open_button")
        self.plot_button = QtWidgets.QPushButton(plotBox)
        self.plot_button.setObjectName("plot_button")
        self.fileName_lineEdit = QtWidgets.QLineEdit(plotBox)
        self.fileName_lineEdit.setReadOnly(True)
        self.fileName_lineEdit.setObjectName("fileName_lineEdit")
        # 將matplotlib嵌進來
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        # listView
        self.list = QtWidgets.QListView()
        self.model = QtGui.QStandardItemModel(self.list)
        self.list.setModel(self.model)
        
        self.gridLayout.addWidget(self.fileName_lineEdit, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.open_button, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.plot_button, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.list, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.canvas, 2, 0, 1, 2)
        
        self.retranslateUi(plotBox)

        self.open_button.clicked.connect(plotBox.openFile)
        self.plot_button.clicked.connect(plotBox.plotData)
        self.model.itemChanged.connect(plotBox.onItemChanged)

    def retranslateUi(self, plotBox):
        _translate = QtCore.QCoreApplication.translate
        plotBox.setTitle(_translate("PlotBox", "Plot CSV Data"))
        self.open_button.setText(_translate("PlotBox", "Open"))
        self.plot_button.setText(_translate("PlotBox", "Plot"))
    