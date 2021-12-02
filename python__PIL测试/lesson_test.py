import PIL.Image as image
import numpy as np

img1 = image.open("sea.jpg")
# img1.show() # 默认打开工具打开

print(img1.size)

img = np.array(img1)
print(img.shape)
print(img.transpose(2,0,1).shape)


#获取通道
print(img1.getbands())
print("---")

#获取模式
# print(img1.mode)
# img2 = img1.convert("1")
# img2.show()
# print(img2.mode)

# 查看某个像素的值
pixel = img1.getpixel((100,100))
print(pixel)

#改变长和宽
# print(img1.size)
# img1.resize((100,100)).show()

# 保存图像
img1.save("save.jpg")

# 抠图
img = img1.crop((150,150,250,250))
img.show()

# 旋转
img1.rotate(45).show()

im = image.open("girl.jpg")
# 粘贴
img1.paste(im,(200,200))
img1.show()
# 翻转
# img1.transpose(image.FLIP_LEFT_RIGHT).show()

# 画图
# 导入画图包
import PIL.ImageDraw as imgDraw
# 创建画笔
draw = imgDraw.Draw(img1)
draw.rectangle((100,100,200,200), outline="red", width=3)
draw.ellipse(xy=((200,200),(210,210)))
# img1.show()

import PIL.ImageFilter as ImgFilter

# img1.filter(ImgFilter.CONTOUR).show()
# img1.filter(ImgFilter.GaussianBlur).show()
# img1.filter(ImgFilter.Color3DLUT).show()
# img1.filter(ImgFilter.DETAIL).show()
# img1.filter(ImgFilter.EDGE_ENHANCE).show()
# img1.filter(ImgFilter.EDGE_ENHANCE_MORE).show()
# img1.filter(ImgFilter.FIND_EDGES).show()


from PIL import Image
import numpy as np

img = Image.open("girl.jpg")

#图像转 numpy
img_data = np.array(img)
print(
    img_data,# hwc
    img_data.shape
)

# 操作矩阵的方式来操作图像
b_data = img_data[...,2]
b_data = np.expand_dims(b_data, axis=2)

# numpy 转图像
# img = Image.fromarray(img_data)
# print(img.mode)
# img.show()


# print("b_data_type", b_data.dtype)
# print(b_data.shape)
b_data = np.array(b_data, dtype=np.uint8)
print("b_data",b_data.shape, b_data.dtype)

# 构建 0 矩阵
back_data = np.zeros((1080,1920,1), dtype=np.uint8)
# back_data = np.array(back_data)
print("back_data",back_data.shape, back_data.dtype)
# print("back_data",back_data.dtype)

b_img = np.concatenate((back_data,b_data,back_data),axis=2)
# Image.fromarray(b_img).show()

# b_img.show()

# 图片生成一张二维码
import random
from PIL import Image,ImageDraw,ImageFont,ImageFilter

class GenerateCoder():
    #生成随机内容（A~Z）
    def get_text(self):
        return chr(random.randint(65,90)) # 返回 ascii 码并转化成字符
    #生成随机的前景色
    def font_color(self):
        return (random.randint(60,120),
                random.randint(60,120),
                random.randint(60,120),)

    def back_color(self):
        return (random.randint(110,200),
                random.randint(110,200),
                random.randint(110,200),)

    def encoder(self):
        w, h = 500, 60
        #创建画板
        panel = Image.new(size=(w,h), color=(255,0,255),mode='RGB')

        #创建画家
        draw = ImageDraw.Draw(panel)
        #
        #创建字体
        font = ImageFont.truetype(font=r"C:\Users\60161\Desktop\python_go\PILTest\comic.ttf",size=30)
        #
        #给画板上色
        for y in range(h):
            for x in range(w):
                draw.point((x,y), fill=self.back_color())
        # panel = panel.filter(ImageFilter.CONTOUR)


        # draw = ImageDraw.Draw(panel)
        #填入内容
        for i in range(4):
            draw.text((125*i+20, 0), text=chr(65), font=font, fill=self.font_color())

        return panel

if __name__ == '__main__':
    gen = GenerateCoder()
    img = gen.encoder()
    img.show()



