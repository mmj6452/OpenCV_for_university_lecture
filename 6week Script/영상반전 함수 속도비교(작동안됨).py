import time
import numpy as np
import cv2


def pixel_access1(image):
    image1 = np.zeros(image.shape[:2], image.dtype)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            k = image[i, j]
            image1[i, j] = 255 - k
    return image1


def pixel_access2(image):
    image2 = np.zeros(image.shape[:2], image.dtype)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            k = image[i, j]
            image2.itemset((i, j), 255 - k)
    return image2


def pixel_access3(image):
    lut = [255 - i for i in range(256)]
    lut = np.array(lut, np.uint8)
    image3 = lut[image]
    return image3


def pixel_access4(image):
    image4 = cv2.subtract(255, image)
    return image4


def pixel_access5(image):
    image5 = 255 - image
    return image5


image = cv2.imread("C:/Users/64527/PycharmProjects/OpenCV_university/6주차 Script/Image/bright.jpg", cv2.IMREAD_GRAYSCALE)


def time_check(func, msg):
    start_time = time.perf_counter()
    ret_img = func(image)
    elapsed = (time.perf_counter() - start_time) * 1000
    print(msg, "수행시간 : %0.2f ms" % elapsed)
    return ret_img


image1 = time_check(pixel_access1, "방법1 직접 접근방식")
image2 = time_check(pixel_access2, "방법2 item()함수 접근")
image3 = time_check(pixel_access3, "방법3 룩업테이블")
image4 = time_check(pixel_access4, "방법4 opencv함수")
image5 = time_check(pixel_access5, "방법5 ndarry 연산")
