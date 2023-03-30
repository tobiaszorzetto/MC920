from scipy import misc
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt
import imageio

img1=imageio.imread("baboon.png")
img2=imageio.imread("butterfly.png")



combined = np.add(0.5*img1,0.5*img2)

plt.imshow(combined, cmap = "gray")
plt.show()