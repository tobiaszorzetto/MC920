from scipy import misc
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt
import imageio

img=imageio.imread("baboon.png")
newImg = img
lvl = 7

for i in range(img.shape[0]-1):
    for j in range(img.shape[1]-1):
        if(i == 0):
            if (j == 0):
                newImg[i][j] = img[i+1][j]+img[i][j+1]+img[i+1][j+1]
            else:
                newImg[i][j] = img[i+1][j]+img[i][j+1]+img[i+1][j+1] - img[i][j-1]
        else:
            if(j == 0):
                newImg[i][j] = img[i+1][j]+img[i][j+1]+img[i+1][j+1] - img[i-1][j]
            else:
                newImg[i][j] = img[i+1][j]+img[i][j+1]+img[i+1][j+1] - img[i-1][j] - img[i][j-1] - img[i - 1][j-1]

newImg[newImg>255] = 255
newImg[newImg<0] = 0

plt.imshow(newImg, cmap = "gray")
plt.show()