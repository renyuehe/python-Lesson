from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

from PyQt5.QtWidgets import QComboBox, QLineEdit

def combobox_currentTextChanged(str):
    print(str)

class Exp(QWidget):
    def __init__(self):
        super(Exp, self).__init__()

        self.resize(500,500)

        self.combobox = QComboBox(self)
        self.combobox.addItems(("var_value", "var_slider"))

        self.combobox.currentTextChanged.connect(combobox_currentTextChanged)


if __name__ == '__main__':
    app = QApplication([])

    exp = Exp()
    exp.show()

    app.exec_()