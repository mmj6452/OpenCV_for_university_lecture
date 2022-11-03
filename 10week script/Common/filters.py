import numpy as np
import cv2

def filter(image , mask):
    rows,cols = image.shape[:2]
    dst = np.zeros((rows,cols),np.float32)
    ycenter , xcenter = mask.shape[0]//2 , mask.shape[1]//2
    for i in range(ycenter, rows-ycenter):
        for j in range(xcenter,cols-xcenter):
            y1,y2 = i-ycenter,i+ycenter+1
            x1, x2 = j - xcenter, j + xcenter + 1
            roi = image[y1:y2, x1:x2].astype("float32")
            tmp = cv2.multiply(roi, mask)
            dst[i, j] = cv2.sumElems(tmp)[0]
    return dst

def minmax_filter(image, ksize, mode):
    rows,cols = image.shape[:2]
    dst = np.zeros((rows,cols),np.uint8)
    center = ksize //2
    for i in range(center,rows-center):
        for j in range(center,cols-center):
            y1,y2 = i - center,i+center+1
            x1,x2 = j-center, j+center+1
            mask = image[y1:y2,x1:x2]
            dst[i,j] = cv2.minMaxLoc(mask)[mode]
    return dst


def diffrential(image,data1,data2):
    mask1 = np.array(data1,np.float32).reshape(3,3)
    mask2 = np.array(data2, np.float32).reshape(3, 3)

    dst1= filter(image,mask1)
    dst2 = filter(image,mask2)
    dst1,ds2 = np.abs(dst1),np.abs(dst2)
    dst = cv2.magnitude(dst1,dst2)

    dst = np.clip(dst,0,255).astype('uint8')
    dst1 = np.clip(dst1, 0, 255).astype('uint8')
    dst2 = np.clip(dst2, 0, 255).astype('uint8')

    return dst,dst1,dst2

def salt_pepper_noise(img ,n):
    h,w=img.shape[:2]
    x,y=np.random.randint(0,w,n),np.random.randint(0,h,n)
    noise = img.copy()
    for (x,y) in zip(x,y):
        noise[y,x] = 0 if np.random.rand() <0.5 else 255
        return noise


def median_filter(image, size):
    rows,cols = image.shape[:2]
    dst = np.zeros((rows,cols),np.uint8)
    center = size //2
    for i in range(center,rows-center):
        for j in range(center,cols-center):
            y1,y2 = i - center,i+center+1
            x1,x2 = j-center, j+center+1
            mask = image[y1:y2,x1:x2].flatten()


            sort_mask = cv2.sort(mask,cv2.SORT_EVERY_COLUMN)
            dst[i,j] = sort_mask[sort_mask.size //2]
    return dst