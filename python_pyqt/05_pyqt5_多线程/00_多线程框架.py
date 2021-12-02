from PyQt5.Qt import (QApplication, QWidget, QPushButton,
                      QThread)
import sys
import time

# 继承QThread
class Thread_1(QThread):  # 线程1
    def __init__(self):
        super().__init__()

    def run(self):
        values = [1, 2, 3, 4, 5]
        for i in values:
            print(i)
            time.sleep(0.5)  # 休眠

class Thread_2(QThread):  # 线程2
    def __init__(self):
        super().__init__()

    def run(self):
        values = ["a", "b", "c", "d", "e"]
        for i in values:
            print(i)
            time.sleep(0.5)