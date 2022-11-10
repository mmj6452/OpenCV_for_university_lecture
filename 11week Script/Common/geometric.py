import cv2
import numpy as np
import time



def scaling(img, size):
    dst = np.zeros(size[::-1],img.dtype)
    ratioY,ratioX = np.divide(size[::-1],img.shape[:2])
    y = np.arange(0,img.shape[0],1)
    x = np.arange(0,img.shape[1],1)
    y,x = np.meshgrid(y,x)
    i,j=np.int32(y*ratioY),np.int32(x*ratioX)
    dst[i,j] = img[y,x]
    return dst

def scaling2(img, size):
    dst = np.zeros(size[::-1],img.dtype)
    ratioY,ratioX = np.divide(size[::-1],img.shape[:2])
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            i,j = int(y*ratioY),int(x*ratioX)
            dst[i,j] = img[y,x]
    return dst

def time_check(func, img, size , title):
    start = time.time()
    func(img, size)
    end = time.time()
    print(title,"수행시간 = %0.2f ms"%(1000*(end-start)))
    return end-start

