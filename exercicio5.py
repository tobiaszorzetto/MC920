import matplotlib.pyplot as plt
import imageio

img1=imageio.imread("baboon.png")
img2=imageio.imread("baboon.png")
img3=imageio.imread("baboon.png")

def gama(value,img):
    return img**(1/value)

img1 = gama(1.5,img1)
img2 = gama(2.5,img2)
img3 = gama(3.5,img3)


plt.imsave("resultados\exercicio5\\result1.png", img1, cmap = "gray")
plt.imsave("resultados\exercicio5\\result2.png", img2, cmap = "gray")
plt.imsave("resultados\exercicio5\\result3.png", img3, cmap = "gray")
