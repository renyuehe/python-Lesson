from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QPlainTextEdit


def on_pushbutton_clicked():
    print("按钮被按下")

if __name__ == '__main__':
    app = QApplication([])
    window = QMainWindow()
    window.resize(500,500)

    plaintext = QPlainTextEdit(window)
    pushbutton = QPushButton(window)


    pushbutton.clicked.connect(on_pushbutton_clicked)

    window.show()

    app.exec_()

