import numpy
import numpy as np
from PIL import Image

import yNumpyOper
import yPILOper

if __name__ == "__main__":
    myOper = yPILOper.PIL_Operation()
    npOper = yNumpyOper.NumpyOperator()
    img1 = Image.open("girl.jpg")
    img2 = Image.open("sea.jpg")
    l = [img1,img2]

    # 1 实现对图片 230 230
    tarSize = 230
    w, h = img1.size
    img1_data = numpy.array(img1)
    print(w,h)
    if(w>h):
        diff = w - h
        ret = npOper.ndarrayWrapper(np.array(img1), axis=(0,), len=diff/2, mode="wrap", value=0)
    else:
        diff = h - w
        ret = npOper.ndarrayWrapper(np.array(img1), axis=(1,), len=diff/2, mode="wrap", value=0)
    img = Image.fromarray(ret)
    img.resize((tarSize, tarSize)).show()


    # 2 三通道
    # ret = myOper.getImgRGB(myimg=img2)#获取三通道
    # img_data = np.concatenate((np.array(ret[0]), np.array(ret[1]), np.array(ret[2])), 0)
    # print(img_data.dtype)
    # img  = Image.fromarray(
    #     np.concatenate((np.array(ret[0]), np.array(ret[1]), np.array(ret[2])), 0)
    # )
    # img.show()

    # 3 纵横裁剪
    # b = myOper.cutImg(img=img, horizontal=4, vertical=5)
    #
    # n = 1
    # w = len(b)
    # h = len(b[0])
    # print(w, h, n)
    # for i in range(w):
    #     for j in range(h):
    #         print(w, h, n, "------")
    #         ax = plt.subplot(w,h,n)
    #         plt.imshow(b[i][j])
    #         n += 1
    #
    # plt.show()

    # 4 轮播图
    # plt.ion()
    # while True:
    #     plt.imshow(l[0])
    #     plt.show()
    #     plt.pause(0.5)
    #     plt.cla()
    #     plt.imshow(l[1])
    #     plt.show()
    #     plt.pause(0.5)
    # plt.ioff()

