import cv2

image = cv2.imread("Img/write_test1.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류")
if image.ndim != 3: raise Exception("영상파일 아님")

brg = cv2.split(image)

print("brg 자료형", type(brg), type(brg[0]), type(brg[0][0][0]))
print("brg 원소 갯수", len(brg))

cv2.imshow("image", image)
cv2.imshow("blue channel", brg[0])
cv2.imshow("green channel", brg[1])
cv2.imshow("red channel", brg[2])

cv2.waitKey(0)
