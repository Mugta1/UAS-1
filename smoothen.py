import cv2 as cv
import numpy as np
img=cv.imread('photos/1.png')
cv.imshow('img', img)
avg= cv.blur(img, (5,5))
cv.imshow('avg', avg)
med=cv.medianBlur(img, 3)
cv.imshow('med', med)
bi=cv.bilateralFilter(img, 50, 50, 50)
cv.imshow('bi', bi)
cv.waitKey(0)