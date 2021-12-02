from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.Qt import QPixmap
import sys


class DragableLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setScaledContents(True)  # 图片自适应
        self.setFixedSize(400, 400)
        self.cuurentimgpath = None

    def initUI(self):
        self.setAcceptDrops(True)
        self.setWindowTitle('可拖放')

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        self.cuurentimgpath = e.mimeData().urls()[0].path()[1:]
        print(self.cuurentimgpath)
        self.pixmap = QPixmap(self.cuurentimgpath)
        self.setPixmap(self.pixmap)
        e.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = DragableLabel()
    example.show()
    sys.exit(app.exec_())