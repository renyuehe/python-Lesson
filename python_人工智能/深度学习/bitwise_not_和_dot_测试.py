import numpy
import cv2
import numpy as np

# a = numpy.array([1,2,3])
# b = numpy.array([4,5,6])
# c = numpy.array([[4],[5],[6]])
# print(numpy.sum(a*b))
#
# print(a.dot(b))
# print(a.dot(c))
#
# print(a * b)

b = numpy.array([4,5,6], dtype=np.uint8)
a = numpy.arange(24).reshape(24)

print(a)
c = np.bitwise_not(a)
print(c.shape)

d = cv2.bitwise_not(a)
print(d.shape)
