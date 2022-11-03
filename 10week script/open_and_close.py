import numpy as np
import cv2

def opening (img,mask):
    tmp = cv2.erode(img,mask)
    dst = cv2.dilate(tmp,mask)
    return dst

def closing (img , mask):
    tmp = cv2.dilate(img, mask)
    dst = cv2.erode(tmp,mask)

    return dst

image = cv2.imread("image/morph.jpg",cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

mask = np.array([[0,1,0],[1,1,1],[0,1,0]]).astype('uint8')
th_img = cv2.threshold(image,128,255,cv2.THRESH_BINARY)[1]

dst1=opening(th_img,mask)
dst2=closing(th_img,mask)
dst3=cv2.morphologyEx(th_img,cv2.MORPH_OPEN,mask)
dst4=cv2.morphologyEx(th_img,cv2.MORPH_CLOSE,mask,iterations = 1)

cv2.imshow("user_open",dst1)
cv2.imshow("user_close",dst2)
cv2.imshow("cv2_open",dst3)
cv2.imshow("cv2_close",dst4)
cv2.waitKey(0)