import cv2 as cv
import numpy as np
img= cv.imread('photos/1.png')
blank= np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('img', img)
cv.waitKey(0)