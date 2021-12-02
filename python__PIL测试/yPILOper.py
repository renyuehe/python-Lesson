import PIL.Image as Image
import numpy as np

class PIL_Operation():

    def img_To_RGB(self, subimg:Image, myrgb: str) -> Image:
        img_data = np.array(subimg)
        b_data = img_data[..., [0]]
        zero_data = np.copy(b_data) * 0
        if (myrgb == "B"):
            b_data = img_data[..., [0]]
            rgb_b_data = np.concatenate((zero_data, zero_data, b_data), 2)
            return Image.fromarray(rgb_b_data)
        elif (myrgb == "G"):
            b_data = img_data[..., [1]]
            rgb_b_data = np.concatenate((zero_data, b_data, zero_data), 2)
            return Image.fromarray(rgb_b_data)
        elif (myrgb == "R"):
            b_data = img_data[..., [2]]
            rgb_b_data = np.concatenate((b_data, zero_data, zero_data), 2)
            return Image.fromarray(rgb_b_data)

    def getImgRGB(self, myimg:Image) -> tuple:
        '''
        获取三通道图
        :param myimg: 输入图
        :return: 输入三通道元组图
        '''
        rImg = self.img_To_RGB(subimg=myimg, myrgb="B")
        gImg = self.img_To_RGB(subimg=myimg, myrgb="G")
        bImg = self.img_To_RGB(subimg=myimg, myrgb="R")
        return (rImg, gImg, bImg)

    def cutImg(self, img:Image, horizontal:int, vertical:int) -> list:
        img_data = np.array(img)

        h,w,c = img_data.shape
        print(w,h,c)
        w2 = int(w/horizontal)#块水平像素
        h2 = int(h/vertical)#块垂直像素
        print(h2,"h2")
        print(h/h2)

        b = []
        for i in range(int(h/h2)):#行数
            a = []
            rowCut = img_data[h2*i:h2*(i+1)]
            for j in range(int(w/w2)):#列数
                print(i)
                # print(img_data[:,h2*i:h2*(i+1)][w2*j:w2*(j+1)].shape)
                rowColumnCut = Image.fromarray(rowCut[:,w2*j:w2*(j+1)])
                a.append(rowColumnCut)
            b.append(a)

        print(len(b))
        print(len(b[0]))

        return b