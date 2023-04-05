import numpy as np
import cv2

img=cv2.imread("city.png")

def invertOdds(img):
    img[1::2, :] = img[1::2, ::-1]

def negative(img):
    return np.add(255, - img)

def transform(img):
    img = np.multiply(100/255, img)
    img = np.add(100, img)
    return np.int16(img)

def reflectRows(img):
    rows = img.shape[0]
    img[int(rows/2)-1::] = img[int(rows/2)::-1]

def verticalMirrowing(img):
    img[:,:] = img[::-1,:]

invertedOddRows = cv2.imread("city.png")
reflectedRows = cv2.imread("city.png")
verticallyMirrowed = cv2.imread("city.png")

invertOdds(invertedOddRows)
reflectRows(reflectedRows)
verticalMirrowing(verticallyMirrowed)

cv2.imwrite("resultados\exercicio3\\negative.png",negative(img))
cv2.imwrite("resultados\exercicio3\\transformed.png",transform(img))
cv2.imwrite("resultados\exercicio3\\invertedOddRows.png",invertedOddRows)
cv2.imwrite("resultados\exercicio3\\reflectedRows.png",reflectedRows)
cv2.imwrite("resultados\exercicio3\\verticallyMirrored.png",verticallyMirrowed)

