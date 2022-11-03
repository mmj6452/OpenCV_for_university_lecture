import numpy as np
import cv2
from Common.filters import median_filter
from Common.filters import salt_pepper_noise

image = cv2.imread("image/median.jpg",cv2.IMREAD_GRAYSCALE)
if image is None: raise  Exception("영상파일 읽기 오류")

noise = salt_pepper_noise(image,500)
med_img1 = median_filter(noise,5)
med_img2 = cv2.medianBlur(noise,5)

cv2.imshow("image",image)
cv2.imshow("noise",noise)
cv2.imshow("med_img1",med_img1)
cv2.imshow("med_img2",med_img2)
cv2.waitKey(0)

