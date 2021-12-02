from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout,QVBoxLayout
import sys
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QFormLayout,QLineEdit,QLabel, QListWidget,QListWidgetItem


class Example(QWidget):

    def __init__(self):
        super().__init__()

        # self.initUI()

        layout = QVBoxLayout(self)
        self.listWidget = QListWidget(self)
        layout.addWidget(self.listWidget)


        item = QListWidgetItem()  # 创建QListWidgetItem对象
        item.setSizeHint(QSize(300, 100))  # 设置QListWidgetItem大小


        item2 = QListWidgetItem()  # 创建QListWidgetItem对象
        item2.setSizeHint(QSize(300, 100))  # 设置QListWidgetItem大小

        self.listWidget.addItem(item)  # 添加item
        self.listWidget.addItem(item2)  # 添加item


        self.listWidget.setItemWidget(item, self.tab1UI())
        self.listWidget.setItemWidget(item2, self.tab2UI())

    def tab1UI(self):
        self.tab1 = QWidget()
        layout = QFormLayout()
        layout.addRow("姓名", QLineEdit())
        layout.addRow("地址", QLineEdit())
        self.tab1.setLayout(layout)
        return self.tab1

    def tab2UI(self):
        self.tab2 = QWidget()
        layout = QFormLayout()
        layout.addRow("年龄", QLineEdit())
        layout.addRow("性别", QLineEdit())
        self.tab2.setLayout(layout)
        return self.tab2

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Example()
    ex.show()

    sys.exit(app.exec_())