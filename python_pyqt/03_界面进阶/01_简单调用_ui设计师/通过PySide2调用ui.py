from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile

import os
import PySide2
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class Stats:

    def __init__(self):
        # 从文件中加载UI定义
        qfile_simple = QFile(r"./simple.ui")
        qfile_simple.open(QFile.ReadOnly)
        qfile_simple.close()

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load(qfile_simple)

        self.ui.pushButton.clicked.connect(self.handleCalc)

    def handleCalc(self):
        print("增加一个手动信号槽")
        ...

app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()