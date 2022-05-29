import cv2 as cv
from cv2 import threshold
import numpy as np


def detect_squares(img):
    cv.imshow('test0', img)
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('test1', img)
    img = cv.medianBlur(img, 5)
    cv.imshow('test2', img)
    sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    img = cv.filter2D(img, -1, sharpen_kernel)

    cv.imshow('test', img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def detect_1(img):
    template = cv.imread('Assets/template-111.png', 0)
    cv.imshow('t', template)
    # template = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
    img_gs = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('gs', img_gs)

    w, h = template.shape[::-1]

    res = cv.matchTemplate(img_gs, template, cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

    cv.imwrite('res.png', img)


img = cv.imread('Assets/stage-1.png', 1)
# detect_squares(img)
detect_1(img)

cv.imshow('0', img)
# img2 = cv.imread('Assets/template-1.png', 1)
# cv.imshow('test', img2)
# img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
# cv.imshow('0', img2)
cv.waitKey(0)
cv.destroyAllWindows()

