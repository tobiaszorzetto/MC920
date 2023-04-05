import cv2
import numpy as np
import imageio
#reading images used
img1=imageio.imread("baboon.png")
img2=imageio.imread("butterfly.png")
#combining images by adding pixel values
combined1 = np.add(0.2*img1,0.8*img2)
combined2 = np.add(0.5*img1,0.5*img2)
combined3 = np.add(0.8*img1,0.2*img2)
#writing images
cv2.imwrite("resultados\exercicio2\combined1.png",combined1)
cv2.imwrite("resultados\exercicio2\combined2.png",combined2)
cv2.imwrite("resultados\exercicio2\combined3.png",combined3)