from scipy import misc
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt
import cv2

img1=cv2.imread("baboon.png")
img2=cv2.imread("butterfly.png")
img3=cv2.imread("city.png")

def invertOdds(img):
    img[1::2, :] = img[1::2, ::-1]

def negative(img):
    return np.add(255, - img)

def transform(img):
    print("normal")
    print(img)
    img = np.multiply(100/255, img)
    print("multiplied")
    print(img)
    img = np.add(100, img)
    print("sum 100")
    print(img)
    return np.int16(img)

def reflectRows(img):
    rows = img.shape[0]
    img[int(rows/2)-1::] = img[int(rows/2)::-1]

def verticalMirrowing(img):
    img[:,:] = img[::-1,:]

#img3 = negative(img3)
#img3 = transform(img3)
#reflectRows(img3)
verticalMirrowing(img3)
plt.imshow(img3, cmap = "gray")

plt.show()