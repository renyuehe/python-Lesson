import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("simple.ui", self)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
