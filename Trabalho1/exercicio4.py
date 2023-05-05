import numpy as np
import imageio.v3 as iio
import matplotlib.pyplot as plt

img=iio.imread("parrot.png")
newImgA=np.empty(img.shape)

newImgA[:,:,2] = img[:,:,0]*0.393 + img[:,:,1]*0.769 + img[:,:,2]*0.189
newImgA[:,:,1] =img[:,:,0]*0.349 + img[:,:,1]*0.686 + img[:,:,2]*0.168
newImgA[:,:,0] =img[:,:,0]*0.272 + img[:,:,1]*0.534 + img[:,:,2]*0.131

newImgB = img[:,:,2]*0.289 + img[:,:,1]*0.587 + img[:,:,0]*0.114

newImgA = np.round(newImgA).astype(np.uint8)
newImgA[newImgA>255] = 255 
newImgB = np.round(newImgB)
newImgB[newImgB>255] = 255 

plt.imsave("resultados\exercicio4\\resultA.png",newImgA)
plt.imsave("resultados\exercicio4\\resultB.png",newImgB, cmap = "gray")