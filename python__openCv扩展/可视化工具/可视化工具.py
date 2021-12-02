# import 库
from logging import FileHandler
from vlogging import VisualRecord
import logging
import webbrowser
import cv2

# 初始化记录器
Imglogger = logging.getLogger("marker_logging")
export_loggingFile = "export_logging.html" # 会在当前目录创建一个Html文件
# if os.path.exists(export_loggingFile)is not None:
#     os.remove(export_loggingFile)
logfilehandler = FileHandler(export_loggingFile, mode="w")
Imglogger.setLevel(logging.DEBUG)
Imglogger.addHandler(logfilehandler)
# 使用记录器记录图片
Img = cv2.imread(r'D:/Desktop/small_girl.jpg', 0)
Imglogger.debug(VisualRecord("src", [Img], fmt="png"))
