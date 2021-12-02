import PIL.Image as image
import PIL.ImageDraw as imgDraw
import PIL.ImageFont as imgFont
import PIL.ImageFilter as imgFilter
import random

font = imgFont.truetype(r"font.TTF", 50)

def randchar():
    """生成随机字母"""
    return chr(random.randint(65, 90))

def bgColor():
    """生成随机背景色"""
    return (random.randint(64,255),
            random.randint(64,255),
            random.randint(64,255))

def ftColor():
    """生成随机前景色"""
    return (random.randint(0,155),
            random.randint(0,155),
            random.randint(0,155))

def img(w, h):
    return image.new(mode="RGB", size=(w, h), color=(255,255,255))


if __name__ == '__main__':
    img = img(200,100)
    image = imgDraw.Draw(img)
    for x in range(200):
        for y in range(100):
            image.point((x,y), fill=bgColor())

    for i in range(4):
        image.text(xy=(45*i,20),text=randchar(),font=font, fill=ftColor())

    img.show()