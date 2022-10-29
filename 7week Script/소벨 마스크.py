import numpy as np
import cv2
from Common.filters import diffrential

image = cv2.imread("image/edge.jpg",cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

data1 = [-1,0,1,
         -2,0,2,
         -1,0,1]
data2 =[-1,-2,-1,
        0,0,0,
        1,2,1]
dst,dst1,dst2 = diffrential(image,data1,data2)

dst3 = cv2.Sobel(np.float32(image),cv2.CV_32F,1,0,3)
dst4 = cv2.Sobel(np.float32(image),cv2.CV_32F,0,1,3)
dst3 = cv2.convertScaleAbs(dst3)
dst4 = cv2.convertScaleAbs(dst4)

cv2.imshow("dst1-vertical",dst1)
cv2.imshow("dst1-horizon",dst2)
cv2.imshow("dst1-vertical_opencv",dst3)
cv2.imshow("dst1-horizon_opencv",dst4)
cv2.waitKey(0)
