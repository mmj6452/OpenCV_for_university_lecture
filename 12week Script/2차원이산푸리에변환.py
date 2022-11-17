import numpy as np
import cv2
from Common.filters import *
from Common.filters import dft2, idft2


image = cv2.imread("C:/Users/64527/Desktop/Smart_CCTV/humen_detect_test/OpenCV_university/12week Script/images/dft_240.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

ck_time(0)
dft = dft2(image)
spectrum1 = calc_spectrum(dft)
spectrum2 = fttshift(spectrum1)
idft = idft2(dft).real
ck_time(1)

cv2.imshow("image", image)
cv2.imshow("spectrum1", spectrum1)
cv2.imshow("spectrum2", spectrum2)
cv2.imshow("idft", cv2.convertScaleAbs(idft))
cv2.waitKey(0)
