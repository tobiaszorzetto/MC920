import numpy as np
import imageio.v3 as iio
import matplotlib.pyplot as plt
import cv2
from scipy.optimize import fsolve
#reading images used
img=iio.imread("baboon_perspectiva.png")

new_img = np.empty(img.shape)


m = [[ 4.72431184e-01,  4.25679289e-02,  37],
 [-3.28943473e-02,  4.98695559e-01,  51],
 [-3.63852926e-04, -3.81947519e-04,  1]]

m = np.asarray(m, dtype=np.float32)
#new_img = cv2.warpPerspective(img, m, (512,512))


for x in range(len(img)):
    for y in range(len(img[0])):
        
        yy = (m[1,0]*x + m[1,1]*y + m[1,2])/(m[2,0]*x + m[2,1]*y + 1 )
        xx = (m[0,0]*x + m[0,1]*y + m[0,2])/(m[2,0]*x + m[2,1]*y + 1) 
    
        new_img[int(y)][int(x)] = img[round(yy),round(xx),0]


plt.imsave("baboonProjecao.png",new_img[:, :, 0], cmap = "gray",vmin = 0, vmax = 255)
plt.imshow(new_img[:, :, 0], cmap= "gray",vmin=0,vmax=255)
plt.show()
