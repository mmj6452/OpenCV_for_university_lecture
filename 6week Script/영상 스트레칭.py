import numpy as np
import cv2

image = cv2.imread("C:/Users/64527/PycharmProjects/OpenCV_university/6주차 Script/Image/contrast.jpg",
                   cv2.IMREAD_GRAYSCALE)

noimage = np.zeros(image.shape[:2], image.dtype)
avg = cv2.mean(image)[0] / 2.0

dst1 = cv2.scaleAdd(image, 0.5, noimage)
dst2 = cv2.scaleAdd(image, 2.0, noimage)
dst3 = cv2.addWeighted(image, 0.5, noimage, 0, avg)
dst4 = cv2.addWeighted(image, 2.0, noimage, 0, -avg)

cv2.imshow("image", image)
cv2.imshow("dst1 - decrease contrast", dst1)
cv2.imshow("dst2 - decrease contrast", dst2)
cv2.imshow("dst3 - decrease contrast using average", dst3)
cv2.imshow("dst4 - decrease contrast using average", dst4)
cv2.waitKey(0)
