import numpy as np
import cv2

image = cv2.imread("image/dog.jpg",cv2.IMREAD_GRAYSCALE)
if image is None:raise Exception("영상파일 읽기 오류")

gaus = cv2.GaussianBlur(image,(7,7),0,0)
dst1 = cv2.Laplacian(gaus,cv2.CV_16S,7)

gaus1 = cv2.GaussianBlur(image,(3,3),0)
gaus2 = cv2.GaussianBlur(image,(9,9),0)
dst2 = gaus1-gaus2
canny = cv2.Canny(image, 80, 200)

cv2.imshow("image",image)
cv2.imshow("dst1-Log",dst1.astype("uint8"))
cv2.imshow("dst2-DoG",dst2)
cv2.imshow("cany",canny)
cv2.waitKey(0)