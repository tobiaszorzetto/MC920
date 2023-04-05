import numpy as np
import cv2

img=cv2.imread("parrot.png")
newImgA=cv2.imread("parrot.png")

newImgA[:,:,2] = img[:,:,2]*0.393 + img[:,:,1]*0.769 + img[:,:,0]*0.189
newImgA[:,:,1] =img[:,:,2]*0.349 + img[:,:,1]*0.686 + img[:,:,0]*0.168
newImgA[:,:,0] =img[:,:,2]*0.272 + img[:,:,1]*0.534 + img[:,:,0]*0.131

newImgB = img[:,:,2]*0.289 + img[:,:,1]*0.587 + img[:,:,0]*0.114

newImgA = np.round(newImgA)
newImgA[newImgA>255] = 255 
newImgB = np.round(newImgB)
newImgB[newImgB>255] = 255 

cv2.imwrite("resultados\exercicio4\\resultA.png",newImgA)
cv2.imwrite("resultados\exercicio4\\resultB.png",newImgB)
