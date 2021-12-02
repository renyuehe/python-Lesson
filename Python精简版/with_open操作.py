import os
import PIL.Image as Image

import cv2

'''
with open 只是对 只是对 open有效, 并不是 别名的意思

'''

# for i in os.listdir(r"img_path"):
#     with Image.open(os.path.join(r"img_path", i)) as im:  # 打开图片
#         im.show()

for i in os.listdir(r"img_path"):
    with cv2.imread(os.path.join(r"img_path", i)) as im:  # 打开图片
        cv2.imshow("img",im)
        cv2.waitKey(0)