import cv2 as cv
import numpy as np
import imageio.v3 as iio
import matplotlib.pyplot as plt
#reading images used
img=iio.imread("D:\GitHub\MC920\Trabalho2\\fiducial.pgm")

newImgA=np.empty(img.shape)

ret,newImg = cv.threshold(img,0,1,cv.THRESH_BINARY+cv.THRESH_OTSU)

plt.imshow(newImg, cmap= "gray",vmin=0,vmax=1)
plt.show()
n,b,p = plt.hist(newImg.flatten(), bins=[-.5,.5,1.5], ec="k")
print("Fração de pixels pretos em relação à quantidade de pixels da imagem:", n[0]/(n[0]+n[1]))
plt.xticks((0,1))
plt.show()

