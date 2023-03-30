from scipy import misc
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt
import cv2

img=cv2.imread("parrot.png")
print("imagem",img)


newImg = img[:,:,2]*0.289 + img[:,:,1]*0.587 + img[:,:,0]*0.114

newImg = np.round(newImg)
newImg[newImg>255] = 255 

print("nova imagem",img)
plt.imshow(newImg, cmap = "gray")
#plt.imshow(img, cmap = "gray")

plt.show()