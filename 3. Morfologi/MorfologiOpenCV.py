# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 07:14:08 2020

@author: Gus Yudha

Code ini telah di upload di GitHub: https://github.com/ibyudha/29-07-2020_OpenCV
"""

import cv2 as c
import matplotlib.pyplot as p
from skimage import io
import numpy as n

link = 'https://bit.ly/GusYudhaProfile'

def Convert_Ukuran_Citra(citra, lebar, panjang):
    ukuran = (panjang, lebar)
    return c.resize(citra, ukuran, interpolation = c.INTER_AREA)

def textnya(citra, judul, x, y, r, g, b, ukuran, border):
    font = c.FONT_HERSHEY_SIMPLEX
    return c.putText (citra, judul, (x, y), font, ukuran, (r,g,b), border, c.LINE_AA)
    
def labelnya(citra, tipe):
    if (tipe == 1):
        textnya(citra, 'Created by', 10, 350, 0, 0, 0, 1, 1)
        textnya(citra, 'Gus Yudha', 10, 390, 0, 0, 0, 1, 1)
        textnya(citra, '1815051012', 10, 40, 0, 0, 0, 0.8, 1)
    else:
        textnya(citra, 'Created by', 10, 350, 255, 255, 255, 1, 1)
        textnya(citra, 'Gus Yudha', 10, 390, 255, 255, 255, 1, 1)
        textnya(citra, '1815051012', 10, 40, 255, 255, 255, 0.8, 1)
        
def Tampilkan(judulnya, citraOri, citra, iniHanyaComentar):
    p.subplot(1, 2, 1)
    labelnya(citraOri, 1)
    p.imshow(citraOri); p.title('Gambar Original'); p.axis('off')
    p.subplot(1, 2, 2)
    p.imshow(citra, cmap='gray'); p.title('Gambar ' 
                                          + judulnya); p.axis('off')
    labelnya(citra, 2)
    p.show(); print(iniHanyaComentar)

def ExtraksCitraDariURL(link): 
    citra = io.imread(link)
    citra = c.cvtColor(citra, c.COLOR_RGB2BGR)
    citra = Convert_Ukuran_Citra(citra, 500, 500)
    c.imwrite('GusYudha.jpeg', citra)
    
def fungsinya(mode, ukuran):
    return c.getStructuringElement(mode, (ukuran, ukuran))
    
def StrukturKernelnya(tipe, ukurannya):
    if (tipe == 1):
        return n.ones((ukurannya, ukurannya), n.uint8)
    elif (tipe == 2):
        return fungsinya(c.MORPH_RECT, ukurannya)
    elif (tipe == 3):
        return fungsinya(c.MORPH_ELLIPSE, ukurannya)
    else:
        return fungsinya(c.MORPH_CROSS, ukurannya)
    
ExtraksCitraDariURL(link); imgOri = p.imread('GusYudha.jpeg')

img = c.imread('GusYudha.jpeg', 0); th = 0; nilaiMax = 255
ret, citraBiner = c.threshold(img, th, nilaiMax, c.THRESH_BINARY_INV 
                              + c.THRESH_OTSU )
Tampilkan('Threshold', imgOri, citraBiner, 'Created by Gus Yudha')

Kernel = StrukturKernelnya( 'nim : ' + '1815051012', 5); print(Kernel)

erosion = c.erode(citraBiner, Kernel, iterations = 1)
Tampilkan('Erosi', imgOri, erosion, 'Ini Contoh Erosi')

dilation = c.dilate(citraBiner, Kernel, iterations = 1)
Tampilkan('Dilasi', imgOri, dilation, 'Ini Contoh Dilasi')

opening = c.morphologyEx(citraBiner, c.MORPH_OPEN, Kernel)
Tampilkan('Opening', imgOri, opening, 'Ini Contoh Opening, ' 
          + 'Dilasi dulu baru erosi')

closing = c.morphologyEx(citraBiner, c.MORPH_CLOSE, Kernel)
Tampilkan('Closing', imgOri, closing, 'Ini Contoh Closing, ' 
          + 'Erosi dulu baru dilasi')

"""
Operasi tambahan yang tidak umum digunakan
"""

gradient = c.morphologyEx(citraBiner, c.MORPH_GRADIENT, Kernel)
Tampilkan('Gradient', imgOri, gradient, 'Ini Contoh Gradient, ' 
          + 'Perbedaan dilasi dan erosi')

tophat = c.morphologyEx(citraBiner, c.MORPH_TOPHAT, Kernel)
Tampilkan('TopHat', imgOri, tophat, 'Ini Contoh Tophat, ' 
          + 'Perbedaan input citra dengan opening')

blackhat = c.morphologyEx(citraBiner, c.MORPH_BLACKHAT, Kernel)
Tampilkan('BlackHat', imgOri, blackhat, 'Ini Contoh Blackhat, ' 
          + 'Perbedaan input citra dengan closing')




