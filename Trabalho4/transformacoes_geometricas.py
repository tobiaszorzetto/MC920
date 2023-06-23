import numpy as np
import imageio.v3 as iio
import matplotlib.pyplot as plt
from math import floor,cos,sin, radians
import argparse
import cv2
#reading images used



def interpolacaoVizinhoMaisProximo(escalaX, escalaY, img):
    new_img = np.empty((int(img.shape[0]*escalaX), int(img.shape[1]*escalaY)))
    for x in range(len(new_img)):
        for y in range(len(new_img[0])):
            new_img[x, y] = img[floor(x/escalaX),floor(y/escalaY)]

    return new_img

def interpolacaoBilinear(escalaX, escalaY, img):
    new_img = np.empty((int(img.shape[0]*escalaX), int(img.shape[1]*escalaY)))
    for x in range(len(new_img)):
        for y in range(len(new_img[0])):
            dx = x/escalaX-floor(x/escalaX)
            dy = y/escalaY-floor(y/escalaY)
            xx =floor(x/escalaX)
            yy = floor(y/escalaY)
            new_img[x, y] = int((1-dx)*(1-dy)*img[xx, yy] + dx*(1-dy)*img[min(xx+1,len(img)-1),yy]+ (1-dx)*dy*(img[xx,min(yy+1, len(img[0])-1)])+ dy*dx*img[min(xx+1,len(img)-1), min(yy+1, len(img[0])-1)])
    return new_img.astype(np.uint8)

def P(t):
    if(t<=0):
        return 0
    return t

def R(s):
    return (1/6)*(P(s+2)**3-4*P(s+1)**3+6*P(s)**3-4*P(s-1)**3)

def interpolacaoBicubica(escalaX, escalaY, img):
    new_img = np.empty((int(img.shape[0]*escalaX), int(img.shape[1]*escalaY)))
    for x in range(len(new_img)):
        for y in range(len(new_img[0])):
            dx = x/escalaX-floor(x/escalaX)
            dy = y/escalaY-floor(y/escalaY)
            xx =floor(x/escalaX)
            yy = floor(y/escalaY)
            sum = 0
            for m in range(-1,3):
                for n in range(-1,3):
                    sum+= float(img[min(xx+m, len(img)-1), min(yy+n, len(img[0])-1)])*R(m-dx)*R(dy-n)
            new_img[x, y] = round(sum)

    return new_img

def L(n,img,xx,yy,dx):
    sum = 0
    sum+= (-dx*(dx-1)*(dx-2)*img[max(xx-1, 0),min(yy+n-2, len(img[0])-1)])/6
    sum+= ((dx+1)*(dx-1)*(dx-2)*img[min(xx, len(img)-1),min(yy+n-2, len(img[0])-1)])/2
    sum+= (-dx*(dx+1)*(dx-2)*img[min(xx+1, len(img)-1),min(yy+n-2, len(img[0])-1)])/2
    sum+= (dx*(dx+1)*(dx-1)*img[min(xx+2, len(img)-1),min(yy+n-2, len(img[0])-1)])/6
    return sum

def interpolacaoLagrange(escalaX, escalaY, img):
    new_img = np.empty((int(img.shape[0]*escalaX), int((img.shape[1])*escalaY)))
    for x in range(len(new_img)):
        for y in range(len(new_img[0])):
            dx = x/escalaX-floor(x/escalaX)
            dy = y/escalaY-floor(y/escalaY)
            xx =floor(x/escalaX)
            yy = floor(y/escalaY)
            sum = 0
            sum+= (-dy*(dy-1)*(dy-2)*L(1,img,xx,yy,dx))/6
            sum+= ((dy+1)*(dy-1)*(dy-2)*L(2,img,xx,yy,dx))/2
            sum+= (-dy*(dy+1)*(dy-2)*L(3,img,xx,yy,dx))/2
            sum+= (dy*(dy+1)*(dy-1)*L(4,img,xx,yy,dx))/6
            new_img[x, y] = sum

    return new_img

def rotacao(grau, img):
    x_center = len(img)/2
    y_center = len(img[0])/2

    new_img = np.empty(img.shape)
    for x in range(len(new_img)):
        for y in range(len(new_img)):
            xx = cos(grau)*(x-x_center) + sin(grau)*(y-y_center) +x_center
            yy = -sin(grau)*(x-x_center) + cos(grau)*(y-y_center) +y_center
            if(0<=int(xx)<len(img) and 0<=int(yy)<len(img[0])):
                new_img[x][y] = img[int(xx)][int(yy)]

    return new_img


def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--a', action = 'store', dest = 'angulo', required=False)
    parser.add_argument('--e', action = 'store', dest = 'escala', required=False)
    parser.add_argument('--d', action = 'store', dest = 'dimensoes', required=False)
    parser.add_argument('--i', action = 'store', dest = 'entrada', required=True)
    parser.add_argument('--o', action = 'store', dest = 'saida', required=True)
    parser.add_argument('--m', action = 'store', dest = 'interpolacao', required=False, choices=['lagrange','bicubica','bilinear','vizinhoMaisProximo'])
    args = parser.parse_args()
    img=iio.imread(args.entrada)
    if(type(img[0][0]) != np.uint8):
        img = img[:,:,0]
    if(args.angulo is not None):
        img = rotacao(radians(float(args.angulo)),img)
    else:
        if(args.dimensoes is not None):
            h,w = args.dimensoes.split()
            escalaX = float(w)/img.shape[0]
            escalaY = float(h)/img.shape[1]
        elif(args.interpolacao is not None):
            escalaX = float(args.escala)
            escalaY = float(args.escala)

        if(args.interpolacao == 'vizinhoMaisProximo'):
            img = interpolacaoVizinhoMaisProximo(escalaX,escalaY,img)
        elif (args.interpolacao == 'bilinear'):
            img = interpolacaoBilinear(escalaX,escalaY,img)
        elif (args.interpolacao == 'bicubica'):
            img = interpolacaoBicubica(escalaX,escalaY,img)
        elif (args.interpolacao == 'lagrange'):
            img = interpolacaoLagrange(escalaX,escalaY,img)

    plt.imsave(args.saida, img, cmap = "gray",vmin = 0, vmax = 255)
    plt.imshow(img, cmap= "gray",vmin=0,vmax=255)
    plt.show()

main()