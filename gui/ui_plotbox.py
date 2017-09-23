from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

class Ui_PlotBox(object):
    def setupUi(self, plotBox):
        plotBox.setObjectName("plotBox")

        #self.centralwidget = QtWidgets.QWidget(plotBox)
        #self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(plotBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plot_button = QtWidgets.QPushButton(plotBox)
        self.plot_button.setObjectName("plot_button")
        self.verticalLayout.addWidget(self.plot_button)
        # 將matplotlib嵌進來
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.verticalLayout.addWidget(self.canvas) 

        self.retranslateUi(plotBox)

        self.plot_button.clicked.connect(plotBox.plotData)

    def retranslateUi(self, plotBox):
        _translate = QtCore.QCoreApplication.translate
        plotBox.setTitle(_translate("PlotBox", "Plot CSV Data"))
        self.plot_button.setText(_translate("PlotBox", "Plot"))
