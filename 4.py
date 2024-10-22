# Mengubah nama variabel
nama_kevin = "Kevin"
umur_kevin = 17
program_studi_kevin= "Sistem Informasi"
jenis_kelamin_kevin = "Laki-laki"
tinggi_kevin = 170
kelas_kevin = "SI-3B"
lulus = False

nama_nichol = "Nichol"
umur_nichol = 18
tinggi_nichol = 175
kelas_nichol = "SI-3C"
lulus = True

print("Nama:", nama_kevin)
print("Umur:", umur_kevin, "tahun")
print("Tinggi Badan:", tinggi_kevin, "cm") 
print("Program Studi:", program_studi_kevin) 
print("Kelas:", kelas_kevin)
print("Jenis Kelamin: ", jenis_kelamin_kevin)

if lulus: # Terjadi error karena tidak ada titik 2 di line 23 ":"
    print("Status: Alumni")
else:
    print("Status: Mahasiswa aktif")