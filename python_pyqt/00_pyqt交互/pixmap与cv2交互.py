import numpy as np
from PyQt5.QtWidgets import QLabel,QApplication,QWidget
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPixmap

import cv2

def cvimg2Pixmap(img_data):
    img_data = cv2.cvtColor(img_data, cv2.COLOR_BGR2RGB)
    img_data = cv2.resize(img_data, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    img_data= np.asanyarray(img_data)
    qimg = QImage(img_data, img_data.shape[1], img_data.shape[0], QImage.Format_RGB888)

    return QPixmap(qimg)

def pixmap2cvimg(piximg):
    ...

if __name__ == '__main__':
    app = QApplication([])

    img_data = cv2.imread("D:/Desktop/small_girl.jpg")
    img = cvimg2Pixmap(img_data)

    widget = QWidget()
    widget.resize(QSize(500,500))

    label = QLabel(widget)
    label.setPixmap(img)
    label.adjustSize()

    widget.show()

    app.exec_()
