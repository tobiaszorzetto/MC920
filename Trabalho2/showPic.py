import cv2
import numpy as np
import imageio.v3 as iio
import matplotlib.pyplot as plt
#reading images used
img=iio.imread("D:\GitHub\MC920\Trabalho2\\fiducial.pgm")



plt.imshow(img, cmap= "gray",vmin=0,vmax=255)
plt.show()
bins = np.arange(257) - 0.5
plt.hist(img, bins, ec="k")
plt.xticks(range(256))
plt.show()
