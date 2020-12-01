# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 13:58:54 2020

@author: Gus Yudha
"""


"""
TINGGAL DI RUN SELURUH CODENYA

HASILNYA BISA DILIHAT DI JENDELA PLOTS
"""

# Import library
import cv2
import numpy as np
from PIL import Image
from skimage import io
import matplotlib.pyplot as plt

def Convert_Ukuran_Citra(a, lebar, panjang):
    ukuran = (panjang, lebar)
    return cv2.resize(a, ukuran, interpolation = cv2.INTER_AREA)

def Property_Citra_Numpy(citra):
    print("Median Citra = ", np.median(citra))
    print("Average Citra = ", np.average(citra))
    print("Mean Citra = ", np.mean(citra))
    print("Std Citra = ", np.std(citra))
    print("Var Citra = ", np.var(citra))

link1 = 'https://lh3.googleusercontent.com/DYWAWqb3s0vGQnM9LUcifqcvgU2-Auu-V3JVzeYVIu3h1nt1FlMSBaerncfctHaa58YDydeOfgB_Lr0tBc_Le7Yb_hf7k3HbdXV7Um2U3LGG1ixXBoxGKN1gctUdzlXNNo1O6Ewemg=w2400'
link2 = 'https://lh3.googleusercontent.com/J4CUrHkDB9udOxmTbXVZGTJDE3yw6NN2l864GbiNhMR3GP5ZNtiBDeoKcNBKhXRfRcSl0ydJAE2h7RkN6Md-XNFa08tlhe9dJrhW1HVgTioZN6pg2qOhNS35klzVTz3-N25oPJPeuQ=w2400'

temp1 = io.imread(link1)
temp2 = io.imread(link2)
temp1 = cv2.cvtColor(temp1, cv2.COLOR_RGB2BGR)
temp2 = cv2.cvtColor(temp2, cv2.COLOR_RGB2BGR)
temp1 = Convert_Ukuran_Citra(temp1, 500, 500)
temp2 = Convert_Ukuran_Citra(temp2, 500, 500)
cv2.imwrite('DayuLydia.jpeg', temp1)
cv2.imwrite('GusYudha.jpeg', temp2)
# Import Citra Digital
citra1 = Image.open('DayuLydia.jpeg')
citra2 = Image.open('GusYudha.jpeg')
# Converting ke numpy array
npCitra1 = np.array(citra1)
# Property_Citra_Numpy(npCitra1)
npCitra2 = np.array(citra2)
# Property_Citra_Numpy(npCitra2)

img1 = plt.imread('DayuLydia.jpeg')
img2 = plt.imread('GusYudha.jpeg')

plt.subplot(1, 2, 1)
plt.imshow(img1)
plt.title('Original Image 1')
plt.subplot(1, 2, 2)
plt.imshow(img2)
plt.title('Original Image 2')
plt.show()

# ===================
# Operasi Aritmatika
# ===================

# Penjumlahan
plt.subplot(2, 3, 1)
plt.imshow(img1 + img2)
plt.title('Penjumlahan')
plt.axis('off')
# Pengurangan
plt.subplot(2, 3, 2)
plt.imshow(img1 - img2)
plt.title('Pengurangan')
plt.axis('off')
# Perkalian
plt.subplot(2, 3, 3)
plt.imshow(img1 * img2)
plt.title('Perkailan')
plt.axis('off')
# pembagian
plt.subplot(2, 3, 4)
plt.imshow(img1 / img2)
plt.title('Pembagian')
plt.axis('off')
# modulus
plt.subplot(2, 3, 5)
plt.imshow(img1 % img2)
plt.title('Modulus')
plt.axis('off')
# pangkat
plt.subplot(2, 3, 6)
plt.imshow(img1 ^ img2)
plt.title('Pangkat')
plt.axis('off')
plt.show()

# ===================
# End of Operasi Aritmatika
# ===================


# ===================
# Fliping
# ===================

plt.subplot(2, 3, 1)
plt.imshow(np.flip(img1, -1))
plt.title('Flip x -1')
plt.axis('off')
plt.subplot(2, 3, 2)
plt.imshow(np.flip(img1, -2))
plt.title('Flip x -2')
plt.axis('off')
plt.subplot(2, 3, 3)
plt.imshow(np.flip(img1, 0))
plt.title('Flip x 0')
plt.axis('off')
plt.subplot(2, 3, 4)
plt.imshow(np.flip(img1, 1))
plt.title('Flip x 1')
plt.axis('off')
plt.subplot(2, 3, 5)
plt.imshow(np.fliplr(img1))
plt.title('Flip Left to Right')
plt.axis('off')
plt.subplot(2, 3, 6)
plt.imshow(np.flipud(img1))
plt.title('Flip Up to Down')
plt.axis('off')
plt.show()

# ===================
# End of Fliping
# ===================

# ===================
# Rolling
# ===================

plt.subplot(1, 2, 1)
plt.imshow(np.roll(img1, 256))
plt.title('Roll 256')
plt.subplot(1, 2, 2)
plt.imshow(np.roll(img1, 2048))
plt.title('Roll 2048')
plt.show()

# ===================
# End of Rolling
# ===================


# ===================
# Transpose
# ===================

plt.imshow(np.rot90(img1, 2))
plt.title('Rotate 90 CCW')
plt.show()

# ===================
# End of Transpose
# ===================


# ===================
# Operasi Logika
# ===================

plt.subplot(2, 3, 1)
plt.imshow(img1)
plt.axis('off')
plt.title('IMG 1')
plt.subplot(2, 3, 2)
plt.imshow(img2)
plt.axis('off')
plt.title('IMG 2')
plt.subplot(2, 3, 3)
plt.imshow(np.bitwise_and(img1, img2))
plt.axis('off')
plt.title('AND')
plt.subplot(2, 3, 4)
plt.imshow(np.bitwise_or(img1, img2))
plt.axis('off')
plt.title('OR')
plt.subplot(2, 3, 5)
plt.imshow(np.bitwise_xor(img1, img2))
plt.axis('off')
plt.title('XOR')
plt.subplot(2, 3, 6)
plt.imshow(np.bitwise_not(img1))
plt.axis('off')
plt.title('NOT')
plt.show()

# ===================
# End of Operasi Logika
# ===================


# ============
# Thresholding
# ============

imgForTh = cv2.imread('GusYudha.jpeg', 0)
th = 127
max_val = 255
ret, o1 = cv2.threshold(imgForTh, th, max_val, cv2.THRESH_BINARY)
ret, o2 = cv2.threshold(imgForTh, th, max_val, cv2.THRESH_BINARY_INV)
ret, o3 = cv2.threshold(imgForTh, th, max_val, cv2.THRESH_TOZERO)
ret, o4 = cv2.threshold(imgForTh, th, max_val, cv2.THRESH_TOZERO_INV)
ret, o5 = cv2.threshold(imgForTh, th, max_val, cv2.THRESH_TRUNC)
output = [imgForTh, o1, o2, o3, o4, o5]
judul = ['Original', 'Binary', 'Binary Inv', 'Zero', 'Zero Inv', 'Trunc']

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(output[i], cmap = 'gray')
    plt.title(judul[i])
    plt.xticks([])
    plt.yticks([])
plt.show()

imgForTh = cv2.imread('GusYudha.jpeg', 1)
imgForTh = cv2.cvtColor(imgForTh, cv2.COLOR_BGR2RGB)
th = 127
max_val = 255
ret, o1 = cv2.threshold(imgForTh, th, max_val, cv2.THRESH_BINARY)
ret, o2 = cv2.threshold(imgForTh, th, max_val, cv2.THRESH_BINARY_INV)
ret, o3 = cv2.threshold(imgForTh, th, max_val, cv2.THRESH_TOZERO)
ret, o4 = cv2.threshold(imgForTh, th, max_val, cv2.THRESH_TOZERO_INV)
ret, o5 = cv2.threshold(imgForTh, th, max_val, cv2.THRESH_TRUNC)
output = [imgForTh, o1, o2, o3, o4, o5]
judul = ['Original', 'Binary', 'Binary Inv', 'Zero', 'Zero Inv', 'Trunc']

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(output[i], cmap = 'gray')
    plt.title(judul[i])
    plt.xticks([])
    plt.yticks([])
plt.show()


# ==================
# End of Thresholding
# ==================


# ==================
# Translasi
# ==================

imgForTr = cv2.imread('DayuLydia.jpeg', 1)
imgForTr = cv2.cvtColor(imgForTr, cv2.COLOR_BGR2RGB)
baris, kolom, kanal = imgForTr.shape
T = np.float32([[1, 0, 150], [0, 1, 50]])
# print(T)
output = cv2.warpAffine(imgForTr, T, (kolom, baris))
plt.imshow(output)
plt.title('Hasil Translasi')
plt.show()

# ==================
# End of Translasi
# ==================

# ==================
# Transform
# ==================

imgForTrf = cv2.imread('GusYudha.jpeg', 1)
imgForTrf = cv2.cvtColor(imgForTrf, cv2.COLOR_BGR2RGB)
baris, kolom, kanal = imgForTrf.shape
p1 = np.float32([[50, 50], [300, 100], [100, 300]])
p2 = np.float32([[200, 150], [400, 150], [200, 400]])
T = cv2.getAffineTransform(p1, p2)
output = cv2.warpAffine(imgForTrf, T, (kolom, baris))
plt.imshow(output)
plt.title('Hasil Transform')
plt.show()

# ==================
# End of Translasi
# ==================

# ==================
# Zoom Rotate
# ==================

imgForR = cv2.imread('GusYudha.jpeg', 1)
imgForR = cv2.cvtColor(imgForR, cv2.COLOR_BGR2RGB)
baris, kolom, kanal = imgForR.shape
R1 = cv2.getRotationMatrix2D((kolom/2, baris/2), 50, 1)
R2 = cv2.getRotationMatrix2D((0, 0), 50, 1)
plt.subplot(1, 2, 1)
plt.imshow(cv2.warpAffine(imgForR, R1, (kolom, baris)))
plt.title('Rotate 1')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(cv2.warpAffine(imgForR, R2, (kolom, baris)))
plt.title('Rotate 2')
plt.axis('off')
plt.show()

# ==================
# End of Rotate
# ==================

# ==================
# Zoom In/Out
# ==================

imgForZ = cv2.imread('DayuLydia.jpeg', 1)
imgForZ = cv2.cvtColor(imgForZ, cv2.COLOR_BGR2RGB)
baris, kolom, kanal = imgForZ.shape
p1 = np.float32([[0, 0], [400, 0], [400, 400]])
p2 = np.float32([[0, 0], [500, 0], [500, 500]])
p3 = np.float32([[0, 0], [300, 0], [300, 300]])
zIn = cv2.getAffineTransform(p1, p2)
zOut = cv2.getAffineTransform(p1, p3)
plt.subplot(1, 2, 1)
plt.imshow(cv2.warpAffine(imgForZ, zIn, (kolom, baris)))
plt.title('Zoom In')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(cv2.warpAffine(imgForZ, zOut, (kolom, baris)))
plt.title('Zoom Out')
plt.axis('off')
plt.show()

# ==================
# End of Zoom In/Out
# ==================


# ==================
# Scaling
# ==================

imgForSc = cv2.imread('GusYudha.jpeg', 1)
output = cv2.resize(imgForSc, None, fx = 0.5, fy = 1.2, interpolation = cv2.INTER_AREA)
cv2.imshow('Hasil Scalling', output)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ==================
# End of Scaling
# ==================
