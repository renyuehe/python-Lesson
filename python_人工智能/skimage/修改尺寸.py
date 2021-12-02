
import cv2
from skimage import data, transform

img = data.camera()
output_shape = (100,200)


dst = transform.resize(img, output_shape,
                        # order=1,
                        # mode="wrap",
                        # cval=0,
                        # clip=True,
                        # preserve_range=False
                       )

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()