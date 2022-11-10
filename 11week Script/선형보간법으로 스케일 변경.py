import cv2
import numpy as np
from Common import *


# image scale up by Bilnear Interpolation

def bilinear_value(img, pt):
    x, y = np.int32(pt)
    if x >= img.shape[1] - 1: x = x - 1
    if y >= img.shape[0] - 1: y = y - 1

    p1, p2, p3, p4 = np.float32(img[y:y + 2, x:x + 2].flatten())

    alpha, beta = pt[1] - y, pt[0] - x
    M1 = p1 + alpha * (p3 - p1)
    M2 = p2 + alpha * (p4 - p2)
    p = M1 + beta * (M2 - M1)
    return np.clip(p, 0, 255)


def scaling_bilinear(img, size):
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    dst = [[bilinear_value(img, (j / ratioX, i / ratioY))
            for j in range(size[0])]
           for i in range(size[1])]
    return np.array(dst, img.dtype)


image = cv2.imread("images/interpolation.jpg")
if image is None: raise Exception("영상파일 읽기 오류")

size = (350, 400)
dst1 = scaling_bilinear(image, size)
dst3 = cv2.resize(image, size, interpolation=cv2.INTER_LINEAR)
dst4 = cv2.resize(image, size, interpolation=cv2.INTER_NEAREST)

cv2.imshow("image", image)
cv2.imshow("dst1", dst1)
cv2.imshow("dst3", dst3)
cv2.imshow("dst4", dst4)

cv2.waitKey(0)