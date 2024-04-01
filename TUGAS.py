#NAMA : RAFLI NUR IKHWAN ABDILAH_23090089_2A
import numpy as np

VA      = [2, 4, 6, 8]
VB      = [13, 15, 17, 19]
VC      = [[10, 20, 30],[11, 22, 33]]
VD      = [[9, 7, 5],[21, 31, 41]]

vektor_A = np.array(VA)
vektor_B = np.array(VB)
vektor_C = np.array(VC)
vektor_D = np.array(VD)

# Tugas soal Penjumlahan dan pengurangan

Penjumlahan = vektor_A + vektor_B
Penjumlahan = vektor_D + vektor_C
Pengurangan = vektor_B - vektor_A
Pengurangan = vektor_C - vektor_D

print("Hasil Vektor A + Vektor B: " + str(Penjumlahan))
print("Hasil Vektor D + Vektor C: " + str(Penjumlahan))
print("Hasil Vektor B - Vektor A: " , str(Pengurangan))
print("Hasil Vektor C - Vektor D: " , str(Pengurangan))

# Tugas soal Perkalian dan pembagian

Perkalian = vektor_B * vektor_A
Perkalian = vektor_C * vektor_D
Pembagian = vektor_B / vektor_A
Pembagian = vektor_D / vektor_C

print("Hasil Vektor B x Vektor A: " + str(Perkalian))
print("Hasil Vektor C x Vektor D: " + str(Perkalian))
print("Hasil Vektor B : Vektor A: " , str(Pembagian))
print("Hasil Vektor D : Vektor C: " , str(Pembagian))

# Tugas soal Perkalian Dot Vektor

#1
dot_product = vektor_B.dot(vektor_A)
print("Hasil Perkalian Dot (Titik): ", str(dot_product))
#2
dot_product_2 = np.inner(vektor_C, vektor_D)
print("Hasil Perkalian Dot (Titik): ", str(dot_product_2))

# Tugas soal Perkalian Skalar

#1
vektor= np.array (VA)
print("Vektor: " + str(vektor))
skalar = 2
Perkalian_Skalar = vektor * skalar
print("Hasil Perkalian Skalar : ", str(Perkalian_Skalar))

#2
vektor= np.array (VB)
print("Vektor: " + str(vektor))
skalar = 2.5
Perkalian_Skalar = vektor * skalar
print("Hasil Perkalian Skalar : ", str(Perkalian_Skalar))

#3
vektor= np.array (VC)
print("Vektor: " + str(vektor))
skalar = 0.5
Perkalian_Skalar = vektor * skalar
print("Hasil Perkalian Skalar : ", str(Perkalian_Skalar))\

#4
vektor= np.array (VD)
print("Vektor: " + str(vektor))
skalar = 1.5
Perkalian_Skalar = vektor * skalar
print("Hasil Perkalian Skalar : ", str(Perkalian_Skalar))