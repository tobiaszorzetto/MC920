import numpy as np
import matplotlib.pyplot as plt
import imageio.v3 as iio


img=iio.imread("baboon.png")

def bitPlane(bit,img):
    return np.bitwise_and(img,2**bit)

for i in range(8):
    img=iio.imread("baboon.png")
    img = bitPlane(i,img)
    plt.imsave("resultados\exercicio7\\bit{}.png".format(i), img, cmap = "gray")
