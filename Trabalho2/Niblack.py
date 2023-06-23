import numpy as np
import imageio.v3 as iio
import matplotlib.pyplot as plt
#reading images used
img=iio.imread("D:\GitHub\MC920\Trabalho2\\fiducial.pgm")

def filter(img,n,k):
    newImg = np.empty(img.shape)
    p = int((n-1)/2)
    imgPadded = np.pad(img, p , "symmetric")
    for i in range(imgPadded.shape[0]):
        for j in range(imgPadded.shape[1]):
            if( i<imgPadded.shape[0]-p and i>=p and j<imgPadded.shape[1]-p and j>=p):
                newImg[i- p][j- p] = setValue(imgPadded,i ,j , n, p ,k)
    newImg.round()
    newImg.clip(0,255)
    return newImg

def setValue(imgPadded, pixel_i, pixel_j, n, p,  k):
    items = imgPadded[pixel_i-p:pixel_i+p, pixel_j-p:pixel_j+p]

    media = np.mean(items)
    desvpad = np.std(items)

    T = media + k * desvpad

    if (imgPadded[pixel_i,pixel_j] < T):
        return 0
    return 1

newImg = filter(img,15,0.2)
plt.imshow(newImg, cmap= "gray",vmin=0,vmax=1)
plt.show()
n,b,p = plt.hist(newImg.flatten(), bins=[-.5,.5,1.5], ec="k")
print("Fração de pixels pretos em relação à quantidade de pixels da imagem: %.2f" % float(n[0]/(n[0]+n[1])))
plt.xticks((0,1))
plt.show()