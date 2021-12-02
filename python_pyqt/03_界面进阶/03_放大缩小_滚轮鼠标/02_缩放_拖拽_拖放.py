
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt5.Qt import QPixmap, QPoint, Qt, QPainter, QIcon

class ImageBox(QWidget):
    def __init__(self):
        super(ImageBox, self).__init__()
        self.img = None
        self.scaled_img = None
        self.point = QPoint(0, 0)
        self.start_pos = None
        self.end_pos = None
        self.left_click = False
        self.scale = 1
        self.initUI()
        # self.setScaledContents(True)  # 图片自适应
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
        # self.setPixmap(self.pixmap)
        self.set_image(self.cuurentimgpath)
        e.accept()

    def init_ui(self):
        self.setWindowTitle("ImageBox")

    def set_image(self, img_path):
        """
        open image file
        :param img_path: image file path
        :return:
        """
        # img = QImageReader(img_path)
        # img.setScaledSize(QSize(self.size().width(), self.size().height()))
        # img = img.read()
        self.img = QPixmap(img_path)
        self.scaled_img = self.img

    def paintEvent(self, e):
        """
        receive paint events
        :param e: QPaintEvent
        :return:
        """
        if self.scaled_img:
            painter = QPainter()
            painter.begin(self)
            painter.scale(self.scale, self.scale)
            painter.drawPixmap(self.point, self.scaled_img)
            painter.end()

    def wheelEvent(self, event):
        angle = event.angleDelta() / 8  # 返回QPoint对象，为滚轮转过的数值，单位为1/8度
        angleY = angle.y()
        # 获取当前鼠标相对于view的位置
        if angleY > 0:
            self.scale *= 1.1
        else:  # 滚轮下滚
            self.scale *= 0.9
        self.adjustSize()
        self.update()


    def mouseMoveEvent(self, e):
        """
        mouse move events for the widget
        :param e: QMouseEvent
        :return:
        """
        if self.left_click:
            self.end_pos = e.pos() - self.start_pos
            self.point = self.point + self.end_pos
            self.start_pos = e.pos()
            self.repaint()

    def mousePressEvent(self, e):
        """
        mouse press events for the widget
        :param e: QMouseEvent
        :return:
        """
        if e.button() == Qt.LeftButton:
            self.left_click = True
            self.start_pos = e.pos()

    def mouseReleaseEvent(self, e):
        """
        mouse release events for the widget
        :param e: QMouseEvent
        :return:
        """
        if e.button() == Qt.LeftButton:
            self.left_click = False

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    imagebox = ImageBox()
    imagebox.show()
    sys.exit(app.exec_())

