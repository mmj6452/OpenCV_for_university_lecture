import numpy as np
import cv2
from Common.filters import minmax_filter

image = cv2.imread("image/min_max.jpg",cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

minfilter_img = minmax_filter(image,3,0)
maxfilter_img = minmax_filter(image,3,1)

edge =maxfilter_img-minfilter_img

cv2.imshow("image",image)
cv2.imshow("min",minfilter_img)
cv2.imshow("max",maxfilter_img)
cv2.imshow("edge",edge)
cv2.waitKey(0)
