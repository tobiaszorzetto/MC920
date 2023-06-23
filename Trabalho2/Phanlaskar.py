import numpy as np
import imageio.v3 as iio
import matplotlib.pyplot as plt
#reading images used
img=iio.imread("D:\GitHub\MC920\Trabalho2\\fiducial.pgm")

def filter(img,n,k,R, p, q):
    newImg = np.empty(img.shape)
    padding = int((n-1)/2)
    imgPadded = np.pad(img, padding , "symmetric")
    for i in range(imgPadded.shape[0]):
        for j in range(imgPadded.shape[1]):
            if( i<imgPadded.shape[0]-padding and i>=padding and j<imgPadded.shape[1]-padding and j>=padding):
                newImg[i- padding,j- padding] = setValue(imgPadded,i ,j , n, padding, k,R, p, q)
    return newImg

def setValue(imgPadded, pixel_i, pixel_j, n, padding, k,R, p, q):
    items = imgPadded[pixel_i-padding:pixel_i+padding, pixel_j-padding:pixel_j+padding]

    media = np.mean(items)
    desvpad = np.std(items)

    T = media * ( 1 + p * np.exp( -q * media) + k * (desvpad/R - 1) )

    if (imgPadded[pixel_i][pixel_j] < T):
        return 0
    return 1

newImg = filter(img,29,0.25,128, 0.5, 10)

plt.imshow(newImg, cmap= "gray",vmin=0,vmax=1)
plt.show()
n,b,p = plt.hist(newImg.flatten(), bins=[-.5,.5,1.5], ec="k")
print("Fração de pixels pretos em relação à quantidade de pixels da imagem: %.2f" % float(n[0]/(n[0]+n[1])))
plt.xticks((0,1))
plt.show()