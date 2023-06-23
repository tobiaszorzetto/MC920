import cv2
import numpy as np
import imageio.v3 as iio
import matplotlib.pyplot as plt
#reading images used
img=iio.imread("D:\GitHub\MC920\Trabalho2\\fiducial.pgm")

newImg=np.empty(img.shape)

newImg[img>128] = 1
newImg[img<=128] = 0


plt.imshow(newImg, cmap= "gray",vmin=0,vmax=1)
plt.show()
n,b,p = plt.hist(newImg.flatten(), bins=[-.5,.5,1.5], ec="k")
print("Fração de pixels pretos em relação à quantidade de pixels da imagem: %.2f" % float(n[0]/(n[0]+n[1])))
plt.xticks((0,1))
plt.show()
