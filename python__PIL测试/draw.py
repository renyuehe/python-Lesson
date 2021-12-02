import PIL.Image as image
import PIL.ImageDraw as draw
import PIL.ImageFont as imgFont
font = imgFont.truetype(r"font.TTF", 50)

img1 = image.open("girl.jpg")

# 设置画家的绘制画板
paintBoard = draw.Draw(img1)
# 画点

paintBoard.point((100,100), fill="red")
paintBoard.point((102,102), fill="red")
paintBoard.point((104,104), fill="red")
paintBoard.point((106,106), fill="red")

# 画矩形
paintBoard.rectangle((30,30,50,50), fill="blue")

# 画线
paintBoard.line((110,110,10,110),fill="yellow", width=3)

# 字体
paintBoard.text(xy=(200,200),text=r"nihao", fill="green", font=font)

# 圆弧
paintBoard.arc((30,30, 100,120), 100, 200, fill="red", width=3)

# 闭合圆弧
paintBoard.chord((100, 60, 40, 120), 100, 200, fill="blue")

# 转换图像模式
# 1：1位像素
# L：8位像素 灰度图
# P：8像素
# RGB：3*8像素，真彩色
# RGBA：4*8像素，有透明通道的真彩色
# img1.convert("L").show()

img1.show()

