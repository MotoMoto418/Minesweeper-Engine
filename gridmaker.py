import cv2 as cv
import numpy as np
import easyocr as ocr


def convertToGrid(img, n):
    img = img[90:380, 10:305]

    grid = []
    pos_y = 10
    dx, dy = 30, 30

    reader = ocr.Reader(['en'])

    for i in range(n):
        rows = []
        pos_x = 12

        for j in range(n):
            img_o = img[pos_y:pos_y+dx, pos_x:pos_x+dy]
            img_gs_o = cv.cvtColor(img_o, cv.COLOR_BGR2GRAY)

            bfilter = cv.bilateralFilter(img_gs_o, 11, 17, 17)
            edged = cv.Canny(bfilter, 30, 200))

            res = reader.readtext(edged, allowlist='0123456789')

            if len(res) == 0:
                if np.sum(img_gs_o == 255) > 0:
                    rows.append('U')

                else:
                    rows.append('O')

            else:
                res = res[0][1]
                rows.append(res)

            pos_x += 30
        pos_y += 30
        grid.append(rows)

    return grid

if __name__ == '__main__':
    img = cv.imread('Assets/stage-1.png')
    k = convertToGrid(img, 9)
    for i in k:
        print(i)
