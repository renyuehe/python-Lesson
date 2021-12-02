
from skimage.transform import rotate
import cv2
img = cv2.imread(r"small_sea.jpg")

rotate_img = rotate(img,30)#逆时针旋转30°

cv2.imshow("rotate_img", rotate_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
