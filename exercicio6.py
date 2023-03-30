from scipy import misc
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt
import imageio

img=imageio.imread("baboon.png")

gama = 3.5

lvl = 6

newImg = img >>lvl

plt.imshow(newImg, cmap = "gray")
plt.show()