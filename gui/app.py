import sys
from PyQt5.QtWidgets import QApplication
from gui.mainwindow import MainWindow

def run():
    app = QApplication(sys.argv)

    main_window = MainWindow(app)
    main_window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    run()