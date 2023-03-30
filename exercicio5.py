from scipy import misc
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt
import imageio

img=imageio.imread("baboon.png")

gama = 3.5

newImg = img**(1/gama)

plt.imshow(newImg, cmap = "gray")
plt.show()