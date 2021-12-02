import PIL.Image as image

img1 = image.open("girl.jpg")

# 转换图像模式
# 1：1位像素
# L：8位像素 灰度图
# P：8像素
# RGB：3*8像素，真彩色
# RGBA：4*8像素，有透明通道的真彩色
img1.convert("L").show()

