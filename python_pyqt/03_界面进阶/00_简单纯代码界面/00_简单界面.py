
import sys
from PyQt5.QtWidgets import QApplication , QMainWindow, QPushButton, QPlainTextEdit

app = QApplication([])
window = QMainWindow()
window.resize(500, 400)
window.move(300, 300)
window.setWindowTitle("设置标题")

pushbutton = QPushButton(window)
pushbutton.move(320,180)

plaintextedit = QPlainTextEdit(window)
plaintextedit.move(10,10)
plaintextedit.resize(300,380)


if __name__ == '__main__':
    window.show()
    app.exec_()


