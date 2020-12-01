# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 13:33:51 2020

@author: Gus Yudha
"""

# =====================
# Task 1: Import OpenCV
# =====================

# Import library OpenCV
import cv2

# =====================
# End of Task 1
# =====================

# Check function object
# dir(cv2)

# Check versi OpenCV
# print(cv2.__version__)

import sys
import numpy as np
from PIL import Image
from skimage import io

def Convert_Ukuran_Citra(a, lebar, panjang):
    ukuran = (panjang, lebar)
    return cv2.resize(temp, ukuran, interpolation = cv2.INTER_AREA)
    
Paste_linknya_disini = 'https://lh3.googleusercontent.com/tEEfPwG2AI8v3csI1ujDe30WvF58V6g7JwiXGMLzn3V7BUKKwJ1KBOJYB4I3K270Ax-Sy-3gx0vlty_7LTipoYkyM12RY40_ydtyDUqo96KGSS7B8f5gTuOnwiVjKminhfX3rfvL=w2400'

temp = io.imread(Paste_linknya_disini)
temp = cv2.cvtColor(temp, cv2.COLOR_RGB2BGR)
# temp = Convert_Ukuran_Citra(temp, 500, 500)
cv2.imwrite('Dayu Lydia.jpeg', temp)

# ===================================================
# Task 2: Menerima sebuah nama file dari sebuah citra
# ===================================================

# Import Citra Digital
citraD = Image.open('Dayu Lydia.jpeg')

# Converting ke numpy array
npCitraD = np.array(citraD)

# Menampilkan nama file
print("Nama File Citra = ", citraD.filename)

# ===================================================
# End of Task 2
# ===================================================


# ===================================================
# Task 3: Membaca/meload isi dari file citra tersebut
# ===================================================

# Menampilkan citra digital
citraD.show()

# Menampilkan full size untuk numpy array
np.set_printoptions(threshold=sys.maxsize)
print(npCitraD)

# ===================================================
# End of Task 3
# ===================================================

# dir(citraD)

# ================================================
# Task 4: Menampilkan berapa ukuran citra tersebut
# ================================================

# Inisialisasi Fungsi
def Mengecek_Ukuran_Citra(a):
    if (npCitraD.ndim == 3):
        print("Lebar Citra = ", npCitraD.shape[0])
        print("Tinggi Citra = ", npCitraD.shape[1])
        print("Kanal Citra = ", npCitraD.shape[2])
    else:
        print("Lebar Citra = ", npCitraD.shape[0])
        print("Tinggi Citra = ", npCitraD.shape[1])
        
# Melihat dimensi citra
print("Citra ini berdimensi = ", npCitraD.ndim, "===>>>", npCitraD.shape)

# Melihat rentang ukuran pixel dari citras
Mengecek_Ukuran_Citra(npCitraD)

# Melihat tipe dari citra
print("Tipe Data Citra = ", npCitraD.dtype)

# Menghitung jumlah bytes pada citra
print("Ukuran Citra = ", sys.getsizeof(citraD.tobytes()), "bytes")

# ================================================
# End of Task 4
# ================================================

# ====================================================================
# Task 5: Menampilkan jenis citra/color depth citra (binary/gray/color)
# ====================================================================

# Inisialisasi Fungsi
def Mengecek_Jenis_Citra(a):
    if (a.ndim == 2):
        if (2 in a):
            print("GRAY")
        else:
            print("BINER")
    else:
        print("COLOR")
        
# Inisialisasi Label
depthnya = {'1':1, 'L':8, 'P':8, 'RGB':24, 'RGBA':32, 'CMYK':32, 'YCbCr':24, 'I':32, 'F':32}

print("Bit-depth Citra = ", depthnya[citraD.mode], "bit")
print("Kode Citra = ", citraD.mode, "| Berjenis = ", end="")
Mengecek_Jenis_Citra(npCitraD)
    
# ====================================================================
# End of Task 5
# ====================================================================

# ==============================================================================
# Task 6: Menampilkan nilai pixel warna dari citra di satu titik posisi tertentu
# ==============================================================================


# Inisialisasi Fungsi
def Mengecek_Pixel_Citra(a, baris, kolom):
    if (a.ndim == 2):
        if (2 in a):
            print("Nilai Pixel [",baris,",",kolom,"] = ", npCitraD[baris,kolom])
        else:
            print("Nilai Pixel [",baris,",",kolom,"] = ", npCitraD[baris,kolom])
    else:
        print("Nilai Pixel [",baris,",",kolom,"] = ", npCitraD[baris,kolom])
        print("Nilai Merah [",baris,",",kolom,"] = ", npCitraD[baris,kolom,0])
        print("Nilai Hijau [",baris,",",kolom,"] = ", npCitraD[baris,kolom,1])
        print("Nilai Biru  [",baris,",",kolom,"] = ", npCitraD[baris,kolom,2])
        
Mengecek_Pixel_Citra(npCitraD, 1, 12)

# ==============================================================================
# End of Task 6
# ==============================================================================

# =================================================================
# Task 7: Menyimpan kembali citra tersebut dengan nama file berbeda
# =================================================================

# Menyimpan citra dengan nama yang berbeda
cv2.imwrite('Hasil Sebelum Covert ke BGR.jpg', npCitraD)

# =================================================================
# End of Task 7
# =================================================================


# Remake Semua Pertanyaan
# print("Nama File Citra = ", citraD.filename)
# citraD.show()
# print("Citra ini berdimensi = ", npCitraD.ndim, "===>>>", npCitraD.shape)
# Mengecek_Ukuran_Citra(npCitraD)
# print("Tipe Data Citra = ", npCitraD.dtype)
# print("Ukuran Citra = ", sys.getsizeof(citraD.tobytes()), "bytes")
# Mengecek_Pixel_Citra(npCitraD, 1, 12)
# cv2.imwrite('Hasil Sebelum Covert ke BGR.jpg', npCitraD)

