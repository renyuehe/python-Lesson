'''
SmartImage：
原则：
1、只接受 cv 或者 pil 的 img。
2、不管输入是什么类型，输出的一定是 uint8类型的数值。
3、可以灵活的在 PIL 和 CV 图片之间相互转换
用法：
smartimg = SmartImage(any_img)
smartimg.cvimg  # 返回一个 uint8 类型的 np.ndarray 即 cvimg
smartimg.pilimg # 返回一个 uint8 类型的 PIL.Image.Image

代码写法：
通过type元类创建类的方式来创建, 主要是为了学习语法, 工作中不建议这样的写法
'''

import cv2
import numpy
import numpy as np
from PIL import Image
import PIL

def __init__(self, img):
    assert isinstance(img, numpy.ndarray) or isinstance(img, PIL.Image.Image)
    self.img = img
    if isinstance(img, numpy.ndarray):
        if 'float32' == img.dtype:
            self.img = (img * 255).astype(np.uint8)

@property
def cv_img(self):
    '''
    :param dtype: np.float32 或者 np.uint8
    :return: 一定返回一个 uint8 类型
    '''
    if isinstance(self.img, PIL.Image.Image):
        pildata = np.array(self.img)
        return cv2.cvtColor(pildata, cv2.COLOR_RGB2BGR)
    elif isinstance(self.img, numpy.ndarray):
            return self.img
    else:
        raise Exception("非法图片格式:图片必须是 numpy.ndarray 或 PIL.Image.Image")

@property
def pil_mage(self):
    if isinstance(self.img, PIL.Image.Image):
        return self.img
    elif isinstance(self.img, numpy.ndarray):
        return PIL.Image.fromarray(cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB))
    else:
        raise Exception("非法图片格式:图片必须是 numpy.ndarray 或 PIL.Image.Image")

@property
def img_type(self):
    return type(self.img)

def img_dtype(self):
    return self.img.dtype

def __call__(self):
    return self.img


# type 原类创建法
'''
SmartImage：
原则：
1、只接受 cv 或者 pil 的 img。
2、不管输入是什么类型，输出的一定是 uint8类型的数值。
3、可以灵活的在 PIL 和 CV 图片之间相互转换
用法：
smartimg = SmartImage(any_img)
smartimg.cvimg  # 返回一个 uint8 类型的 np.ndarray 即 cvimg
smartimg.pilimg # 返回一个 uint8 类型的 PIL.Image.Image
'''
SmartImage = type('Foo', (object, ), {'__init__' : __init__,
                                      'cvimg': cv_img,
                                      'pilimg':pil_mage,
                                      'type':img_type,
                                      '__call__':__call__
                                      })

# 验证用法
if __name__ == '__main__':

    pilimg = Image.open(r"D:/Desktop/small_girl.jpg")
    cvimg = cv2.imread(r"D:/Desktop/small_girl.jpg")
    f_cvimg = cvimg.astype(np.float32)/255


    smartImg1 = SmartImage(pilimg)
    smartImg1.pilimg.show()
    cv2.imshow("cvimg", smartImg1.cvimg) #

    smartImg2 = SmartImage(cvimg)
    smartImg2.pilimg.show()
    cv2.imshow("cvimg", smartImg2.cvimg)

    smartImg3 = SmartImage(f_cvimg)
    smartImg3.pilimg.show()
    cv2.imshow("cvimg", smartImg3())

