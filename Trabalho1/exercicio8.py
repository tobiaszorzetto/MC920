import cv2
import numpy as np
import matplotlib.pyplot as plt
import imageio.v3 as iio

h1 = [
    [ 0, 0,-1, 0, 0],
    [ 0,-1,-2,-1, 0],
    [-1,-2,16,-2,-1],
    [ 0,-1,-2,-1, 0],
    [ 0, 0,-1, 0, 0]
    ]

h2 = [
    [ 1, 4, 6, 4, 1],
    [ 4,16,24,16, 4],
    [ 6,24,36,24, 6],
    [ 1, 4, 6, 4, 1],
    [ 4,16,24,16, 4],
]

h3 = [
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1],
]

h4 = [
    [-1,-2,-1],
    [ 0, 0, 0],
    [ 1, 2, 1],
]
h5 = [
    [-1,-1,-1],
    [-1, 8,-1],
    [-1,-1,-1],
]
h6 = [
    [ 1, 1, 1],
    [ 1, 1, 1],
    [ 1, 1, 1]
    ]
h7 = [
    [-1,-1, 2],
    [-1, 2,-1],
    [ 2,-1,-1],
    ]
h8 = [
    [ 2,-1,-1],
    [-1, 2,-1],
    [-1,-1, 2],
    ]
h9 = [
    [ 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 1],
]
h10 = [
    [-1,-1,-1,-1,-1],
    [-1, 2, 2, 2,-1],
    [-1, 2, 8, 2,-1],
    [-1, 2, 2, 2,-1],
    [-1,-1,-1,-1,-1],
]
h11 = [
    [-1,-1, 0],
    [-1, 0, 1],
    [ 0, 1, 1],
]

filters = [h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11]
dividers = [1,256,1,1,1,9,1,1,9,8,1]

def filter(img,mask,divider):
    newImg = np.empty(img.shape)
    pad = int((len(mask) - 1)/2)
    imgPadded = np.pad(img,pad, "symmetric")
    for i in range(imgPadded.shape[0]):
        for j in range(imgPadded.shape[1]):
            if( i<imgPadded.shape[0]-pad and i>=pad and j<imgPadded.shape[1]-pad and j>=pad):
                newImg[i-pad][j-pad] = setValue(mask,divider,imgPadded,i - pad,j - pad)
    newImg.round()
    newImg.clip(0,255)
    return newImg

def setValue(matrix, divider, imgPadded, pixel_i, pixel_j):
    value = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            value+= matrix[i][j]*imgPadded[pixel_i+i][pixel_j+j]
    return value/divider

for f in range(len(filters)):
    img=iio.imread("baboon.png")
    newImg = filter(img,filters[f],dividers[f])
    print("loaded",f+1)
    plt.imsave("resultados\exercicio8\\h{}.png".format(f+1), newImg, cmap = "gray",vmin = 0, vmax = 255)




plt.show()

