import matplotlib.pyplot as plt
import imageio

def lvl(value,img):
    return img >> value

for i in [1,2,3,4,5,6,7]:
    img=imageio.imread("baboon.png")
    img = lvl(i,img)
    plt.imsave("resultados\exercicio6\\lvl{}.png".format(i), img, cmap = "gray")
