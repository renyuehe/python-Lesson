import tools
import cv2
import math
import numpy

# r2 = ((122, 239), (4, 4), 50)
boxes1 = numpy.array([100, 100, 200, 150, 0], numpy.float32)
boxes2 = numpy.array([100, 100, 200, 150, 30], numpy.float32)

img = numpy.zeros((400, 400, 3))
cv2.imshow("img", img)
cv2.waitKey(0)

tools.drawRotateRect(img, 100, 100, 200, 150, 0)
tools.drawRotateRect(img, 100, 100, 200, 150, 30 * (math.pi / 180))

cv2.imshow("img2", img)
cv2.waitKey(0)

# boxes1 = (((boxes1[0]+boxes1[2])/2,(boxes1[1]+boxes1[3])/2), (100,50), boxes1[4])
# boxes2 = (((boxes2[0]+boxes2[2])/2,(boxes2[1]+boxes2[3])/2), (100,50), boxes2[4])

boxes1 = ((boxes1[0], boxes1[1]), (boxes1[2], boxes1[3]), boxes1[4])
boxes2 = ((boxes2[0], boxes2[1]), (boxes2[2], boxes2[3]), boxes2[4])

print(boxes1)
print(boxes2)
order_pts = cv2.rotatedRectangleIntersection(boxes1, boxes2)[1]
order_pts = numpy.squeeze(order_pts).astype(numpy.int32)

print(order_pts)
cv2.polylines(img, [order_pts], isClosed=True, color=(0, 255, 0), thickness=2)
cv2.imshow("img3", img)
cv2.waitKey(0)
cv2.destroyAllWindows()