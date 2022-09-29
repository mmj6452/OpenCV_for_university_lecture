import numpy as np, cv2

image = cv2.imread("Img/minMax.jpg", cv2.IMREAD_GRAYSCALE)

min_val, max_val, _, _ = cv2.minMaxLoc(image)

ratio = 255 / (max_val - min_val)
dst = np.round((image - min_val) * ratio).astype(('uint8'))
min_dst, max_dst, _, _ = cv2.minMaxLoc(dst)

print("원본영상 최솟값= %d, 최댓값= %d" % (min_val, max_val))
print("수정영상 최솟값= %d, 최댓값= %d" % (min_dst, max_dst))
cv2.imshow("image", image)
cv2.imshow("dst", dst)
cv2.waitKey(0)
