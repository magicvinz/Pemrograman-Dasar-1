# Program Tukar_Nilai

# Dideklarasikan variable a dan b dengan tipedata integer
# Nilai variabel a dan b dimasukkan oleh user
# Algoritma menampilkan hasil penukaran nilai variabel a dan b

# Input nilai a
kevin_a = int(input("Nilai a: "))
# Input nilai b
kevin_b = int(input("Nilai b: "))

# Menukar nilai a dan b
kevin_a = kevin_a + kevin_b
kevin_b = kevin_a - kevin_b
kevin_a = kevin_a - kevin_b

# Menampilkan hasil
print("Nilai a sekarang: ", kevin_a)
print("Nilai b sekarang: ", kevin_b)
