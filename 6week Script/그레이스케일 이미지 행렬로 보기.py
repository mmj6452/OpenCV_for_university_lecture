import cv2

image = cv2.imread("Image/pixel.jpg", cv2.IMREAD_GRAYSCALE)

(x, y), (w, h) = (180, 37), (15, 10)
roi_img = image[y:y + h, x:x + w]

print("[roi_img] = ")
for row in roi_img:
    for p in row:
        print("%4d" % p, end="")
print("\n")

cv2.rectangle(image, (x, y, w, h), 255, 1)
cv2.imshow("image", image)
cv2.waitKey(0)
