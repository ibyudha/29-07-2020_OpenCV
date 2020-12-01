# -*- coding: utf-8 -*-
"""
Created on 14/11/2020

@author: Gus Yudha
"""

import cv2 as c
import numpy as n
import math as m

def Convert_Ukuran_Citra(a, lebar, panjang):
    ukuran = (panjang, lebar)
    return c.resize(citra, ukuran, interpolation = c.INTER_AREA)

citra = c.imread ("1815051012.jpeg", 1)
citra = c.cvtColor (citra, c.COLOR_RGB2GRAY)
citra = Convert_Ukuran_Citra(citra, 250, 250)

# Robert Cross
kernelV = n.array([[1,  0],[0,  -1]])
kernelH = n.array([[1,  0],[0,  -1]])
kV = c.filter2D(citra, -1, kernelV)
kH = c.filter2D(citra, -1, kernelH)
kV = kV.astype(n.uint64)
kH = kH.astype(n.uint64)
robert = n.sqrt(n.power(kV,2) + n.power(kH,2))
robert = n.hstack((citra, robert.astype(n.uint8)))

# Compass
cNorth = n.array([[-1,0,1],[-2,0,2],[-1,0,1]])
CompassNorth = c.filter2D(citra, -1, cNorth)
cNorthWest = n.array([[0,1,2],[-1,0,1],[-2,-1,0]])
CompassNorthWest = c.filter2D(citra, -1, cNorthWest) + CompassNorth
cWest = n.array([[1,2,1],[0,0,0],[-1,-2,-1]])
CompassWest = c.filter2D(citra, -1, cWest) + CompassNorthWest
cSouthWest = n.array([[2,1,0],[1,0,-1],[0,-1,-2]])
CompassSouthWest = c.filter2D(citra, -1, cSouthWest) + CompassWest
cSouth = n.array([[1,0,-1],[2,0,-2],[1,0,-1]])
CompassSouth = c.filter2D(citra, -1, cSouth) + CompassSouthWest
cSouthEast = n.array([[0,-1,-2],[1,0,-1],[2,1,0]])
CompassSouthEast = c.filter2D(citra, -1, cSouthEast) + CompassSouth
cEast = n.array([[-1,-2,-1],[0,0,0],[1,2,1]])
CompassEast = c.filter2D(citra, -1, cEast) + CompassSouthEast
cNorthEast = n.array([[-2,-1,0],[-1,0,1],[0,1,2]])
CompassNorthEast = c.filter2D(citra, -1, cNorthEast) + CompassEast
compass = n.hstack((citra, CompassNorthEast))

# Canny
canny1 = c.Canny(citra, 50, 130, L2gradient=False)
canny2 = c.Canny(citra, 100, 150, L2gradient=True)
canny = n.hstack((citra, canny1, canny2))

# Sobel
sobelX = c.Sobel(citra, -1, dx=1, dy=0, ksize=1, scale=1, delta=0, borderType=c.BORDER_DEFAULT)
sobelY = c.Sobel(citra, -1, dx=0, dy=1, ksize=1, scale=1, delta=0, borderType=c.BORDER_DEFAULT)
sobel = n.hstack((citra, sobelX + sobelY))

# Prewitt
x = n.array([[1,1,1],[0,0,0],[-1,-1,-1]])
y = n.array([[-1,0,1],[-1,0,1],[-1,0,1]])
prewittX = c.filter2D(c.GaussianBlur(citra, (15, 15), 0), -1, x)
prewittY = c.filter2D(c.GaussianBlur(citra, (15, 15), 0), -1, y)
prewitt = n.hstack((citra, prewittX + prewittY))

# Gaussian
gaussian = n.hstack((citra, c.GaussianBlur(citra, (15, 15), 0)))

# Kirsch
pNorth = n.array([[-3,-3,5],[-3,0,5],[-3,-3,5]])
kirschNorth = c.filter2D(citra, -1, pNorth)
pNorthWest = n.array([[-3,5,5],[-3,0,5],[-3,-3,-3]])
kirschNorthWest = c.filter2D(citra, -1, pNorthWest) + kirschNorth
pWest = n.array([[5,5,5],[-3,0,-3],[-3,-3,-3]])
kirschWest = c.filter2D(citra, -1, pWest) + kirschNorthWest
pSouthWest = n.array([[5,5,-3],[5,0,-3],[-3,-3,-3]])
kirschSouthWest = c.filter2D(citra, -1, pSouthWest) + kirschWest
pSouth = n.array([[5,-3,-3],[5,0,-3],[5,-3,-3]])
kirschSouth = c.filter2D(citra, -1, pSouth) + kirschSouthWest
pSouthEast = n.array([[-3,-3,-3],[5,0,-3],[5,5,-3]])
kirschSouthEast = c.filter2D(citra, -1, pSouthEast) + kirschSouth
pEast = n.array([[-3,-3,-3],[-3,0,-3],[5,5,5]])
kirschEast = c.filter2D(citra, -1, pEast) + kirschSouthEast
pNorthEast = n.array([[-3,-3,-3],[-3,0,5],[-3,5,5]])
kirschNorthEast = c.filter2D(citra, -1, pNorthEast) + kirschEast
kirsch = n.hstack((citra, kirschNorthEast))

# LoG
LoG = n.hstack((citra, c.Laplacian(citra, -1, ksize=3, scale=1, delta=0, borderType=c.BORDER_DEFAULT)))

# Frei-Chen
FChenX = c.Sobel(citra, -1, dx=1, dy=0, ksize=int(m.sqrt(3)), scale=1, delta=0, borderType=c.BORDER_DEFAULT)
FChenY = c.Sobel(citra, -1, dx=1, dy=0, ksize=int(m.sqrt(3)), scale=1, delta=0, borderType=c.BORDER_DEFAULT)
FreiChen = n.hstack((citra, FChenX + FChenY))

# Image Gradient
kernely = n.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernelx = n.array([[1,0,-1],[1,0,-1],[1,0,-1]])
titikX = c.filter2D(citra, c.CV_8U, kernelx)
titikY = c.filter2D(citra, c.CV_8U, kernely)
image_gradient = n.hstack((citra, titikX + titikY))

# Emboss
f = n.float32([[-2,0,0],[0,0,0],[0,0,2]])
emboss = c.filter2D(citra,-1,f)
emboss = n.hstack((citra,emboss))

# Highboost
kA = n.float32([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
kB = n.float32([[-1,-1,-1],[-1,10,-1],[-1,-1,-1]])
kC = n.float32([[-1,-1,-1],[-1,13,-1],[-1,-1,-1]])
fA = c.filter2D(citra, -1, kA)
fB = c.filter2D(citra, -1, kB)
fC = c.filter2D(citra, -1, kC)
r1 = n.hstack((citra, fA))
r2 = n.hstack((fB, fC))
highboost = n.vstack((r1, r2))

c.imwrite("Robert Cross.jpeg", robert)
c.imwrite("Compass.jpeg", compass)
c.imwrite("Canny.jpeg", canny)
c.imwrite("Sobel.jpeg", sobel)
c.imwrite("Prewitt.jpeg", prewitt)
c.imwrite("Gaussian.jpeg", gaussian)
c.imwrite("Kirsch.jpeg", kirsch)
c.imwrite("LoG.jpeg", LoG)
c.imwrite("Frei-Chen.jpeg", FreiChen)
c.imwrite("Image Gradient.jpeg", image_gradient)
c.imwrite("Emboss.jpeg", emboss)
c.imwrite("Highboost.jpeg", highboost)

c.waitKey(0)
c.destroyAllWindows()
