import cv2
import numpy as np

def calc_histo(image,histSize,ranges=[0,256]):
    hist = np.zeros((histSize,1),np.float32)
    gap = ranges[1]/histSize

    for row in image:
        for pix in row:
            idx = int(pix/gap)
            hist[idx] += 1
    return hist

def draw_histo(hist, shape=(200, 256)):
    hist_img = np.full(shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)
    gap = hist_img.shape[1]/hist.shape[0]

    for i, h in enumerate(hist):
        x = int(round(i * gap))
        w = int(round(gap))
        cv2.rectangle(hist_img, (x, 0, w, int(h)), 0, cv2.FILLED)

        return cv2.flip(hist_img, 0)