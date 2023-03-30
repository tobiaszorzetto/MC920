from scipy import misc
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt
import cv2

img=cv2.imread("parrot.png")
newImg=cv2.imread("parrot.png")
print("imagem",img)


newImg[:,:,2] = img[:,:,2]*0.393 + img[:,:,1]*0.769 + img[:,:,0]*0.189
newImg[:,:,1] =img[:,:,2]*0.349 + img[:,:,1]*0.686 + img[:,:,0]*0.168
newImg[:,:,0] =img[:,:,2]*0.272 + img[:,:,1]*0.534 + img[:,:,0]*0.131

newImg = np.round(newImg)
newImg[newImg>255] = 255 

print("nova imagem",img)
plt.imshow(newImg, cmap = "gray")
#plt.imshow(img, cmap = "gray")

plt.show()