from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QWidget
from PyQt5.QtWidgets import  QPushButton, QPlainTextEdit
from PyQt5.QtWidgets import QComboBox, QLineEdit, QSlider, QCheckBox, QRadioButton
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QFormLayout
from PyQt5.QtWidgets import QListWidgetItem, QListWidget
from PyQt5.QtCore import QSize
from PyQt5.QtCore import Qt


class Exp(QWidget):

    ################# 组件创建函数
    def generValueBox(self):
        self.tab1 = QWidget()
        layout = QFormLayout()
        layout.addRow("变量名", QLineEdit())
        layout.addRow("值", QLineEdit())
        self.tab1.setLayout(layout)
        return self.tab1

    def generSliderBox(self):
        self.tab2 = QWidget()
        layout = QFormLayout()

        layout.addRow("变量名", QLineEdit())

        minEdit = QLineEdit()
        maxEdit = QLineEdit()
        layout.addRow("最小值", minEdit)
        layout.addRow("最大值", maxEdit)

        layout.addRow("值", QSlider(Qt.Horizontal))


        self.tab2.setLayout(layout)
        return self.tab2

    ################# 槽函数
    def on_pushbutton_clicked(self):
        print("按钮1被按下")
        self.listItem = QListWidgetItem(self.listWidget)
        self.listItem.setSizeHint(QSize(300, 100))  # 设置QListWidgetItem大小

        self.listWidget.addItem(self.listItem)
        self.listWidget.setItemWidget(self.listItem, self.generValueBox())



    def on_pushbutton2_clicked(self):
        print("按钮2被按下")
        self.listItem = QListWidgetItem(self.listWidget)
        self.listItem.setSizeHint(QSize(300, 100))  # 设置QListWidgetItem大小

        self.listWidget.addItem(self.listItem)
        self.listWidget.setItemWidget(self.listItem, self.generSliderBox())


    def on_pushbutton3_clicked(self):
        print("按钮3被按下")
        self.listWidget.clear()

    def on_pushbutton4_clicked(self):
        print("按钮4被按下")
        str = self.plaintext.toPlainText()
        try:
            exec(str)
        except Exception as E:
            print(E)

    def on_combobox_currentTextChanged(self, str):
        print(str)

    ################
    def __init__(self):
        super(Exp, self).__init__()

        self.resize(1200,600)
        self.hlayout = QHBoxLayout(self)


        self.vlayout1 = QVBoxLayout(self)
        self.vlayout2 = QVBoxLayout(self)
        self.hlayout.addLayout(self.vlayout1)
        self.hlayout.addLayout(self.vlayout2)

        self.initVLayout1()
        self.initVlayout2()

    def initVLayout1(self):
        self.subhlayout = QHBoxLayout(self)

        self.plaintext = QPlainTextEdit(self)
        self.pushbutton = QPushButton(self)
        self.pushbutton.setText("添加 值控件")

        self.pushbutton2 = QPushButton(self)
        self.pushbutton2.setText("添加 滑动值控件")

        self.pushbutton3 = QPushButton(self)
        self.pushbutton3.setText("删除反射控件")

        self.pushbutton4 = QPushButton(self)
        self.pushbutton4.setText("执行代码块")

        self.subhlayout.addWidget(self.pushbutton)
        self.subhlayout.addWidget(self.pushbutton2)
        self.subhlayout.addWidget(self.pushbutton3)
        self.subhlayout.addWidget(self.pushbutton4)

        self.vlayout1.addLayout(self.subhlayout)
        self.vlayout1.addWidget(self.plaintext)


        self.pushbutton.clicked.connect(self.on_pushbutton_clicked)
        self.pushbutton2.clicked.connect(self.on_pushbutton2_clicked)
        self.pushbutton3.clicked.connect(self.on_pushbutton3_clicked)
        self.pushbutton4.clicked.connect(self.on_pushbutton4_clicked)

    def initVlayout2(self):
        self.listWidget = QListWidget(self)
        self.listWidget.setFixedWidth(300)
        self.vlayout2.addWidget(self.listWidget)



if __name__ == '__main__':
    app = QApplication([])

    exp = Exp()
    exp.show()

    app.exec_()




