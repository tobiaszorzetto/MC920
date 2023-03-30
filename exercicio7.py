from scipy import misc
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt
import imageio

img=imageio.imread("baboon.png")

lvl = 7

newImg = np.bitwise_and(img,2**lvl)

plt.imshow(newImg, cmap = "gray")
plt.show()