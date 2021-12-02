
import sys
from PyQt5.QtWidgets import QApplication , QMainWindow, QPushButton, QPlainTextEdit


if __name__ == '__main__':

    app = QApplication([])
    window = QMainWindow()
    window.resize(500, 400)
    window.move(300, 300)
    window.setWindowTitle("设置标题")

    pushbutton = QPushButton(window)
    pushbutton.move(320, 180)

    plaintextedit = QPlainTextEdit(window)
    plaintextedit.move(10, 10)
    plaintextedit.resize(300, 380)

    def on_pushbutton_clicked():
        str = plaintextedit.toPlainText()
        try:
            exec(str)
        except Exception as E:
            print(E)

    pushbutton.clicked.connect(on_pushbutton_clicked)

    window.show()
    app.exec_()


