import cv2
from skimage import data, transform
from skimage.io import imread,imshow


img = imread(r'./small_sea.jpg') # (h, w, c),(rgb)

vertical_flip = img[::-1, :, :] #垂直翻转 h
horizatal_flip = img[:, ::-1 ,:] #水平翻转 h
channel_flip = img[:, :, ::-1] #通道翻转 h
imshow(horizatal_flip)

cv2.imshow("horizatal_flip", horizatal_flip)
cv2.imshow("vertical_flip", vertical_flip)
cv2.imshow("channel_flip", channel_flip)

cv2.waitKey(0)
cv2.destroyAllWindows()
