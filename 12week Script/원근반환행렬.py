import numpy as np
import cv2

image = cv2.imread("C:/Users/64527/Desktop/Smart_CCTV/humen_detect_test/OpenCV_university/12week Script/images/perspective.jpg",cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류")

pts1 = np.float32([(80,40),(315,133),(75,300),(335,300)])
pts2 = np.float32([(50,60),(340,60),(50,320),(340,320)])

perspect_mat = cv2.getPerspectiveTransform(pts1,pts2)
dst1 = cv2.warpPerspective(image,perspect_mat,image.shape[1::-1],cv2.INTER_LINEAR)
print("[perspect_mat] = \n%s\n",perspect_mat)
dst2 = cv2.warpPerspective(image,perspect_mat,image.shape[1::-1],cv2.INTER_CUBIC)

ones = np.ones((4,1),np.float64)
pts3 = np.append(pts1,ones,axis=1)
pts4 = cv2.gemm(pts3,perspect_mat.T,1,None,1)

print("원본영상 좌표 \t 목적영상 좌표 \t\t 동차좌표 \t\t 변환결과좌표")
for i in range(len(pts4)):
    pts4[i] /= pts4[i][2]
    print("%i : %-14s %-14s %-18s %-18s"%(i,pts1[i],pts2[i],pts3[i],pts4[i]))
    
cv2.imshow("image",image)
cv2.imshow("dst_perspecteive_liner",dst1)
cv2.imshow("dst_perspecteive_cubic",dst2)
cv2.waitKey(0)