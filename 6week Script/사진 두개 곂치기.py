import numpy as np
import cv2

image1 = cv2.imread("Image/add1.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("Image/add2.jpg", cv2.IMREAD_GRAYSCALE)

alpha, beta = 0.6, 0.7
add_img1 = cv2.add(image1, image2)
add_img2 = cv2.add(image1 * alpha, image2 * beta)
add_img2 = np.clip(add_img2, 0, 255).astype('uint8')
add_img3 = cv2.addWeighted(image1, alpha, image2, beta, 0)

titles = ['image1', 'image2', 'add_img1', 'add_img2', 'add_img3']
for t in titles: cv2.imshow(t, eval(t))
cv2.waitKey(0)
