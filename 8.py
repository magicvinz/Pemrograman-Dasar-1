# Input
kevin_gaji_pokok = int(input("Masukkan gaji pokok: "))

# Kamus
kevin_pajak = 0.1 # 10% dari gaji pokok sebelum ditambah tunjangan
kevin_tunjangan = 0.2 # 20% dari gaji pokok 

# Proses
kevin_detail_pajak = kevin_gaji_pokok * kevin_pajak
kevin_detail_tunjangan = kevin_gaji_pokok * kevin_tunjangan
kevin_gaji_bersih = kevin_gaji_pokok + kevin_detail_tunjangan - kevin_detail_pajak

# Output
print("Gaji bersih karyawan: ", kevin_gaji_bersih)
print("Detail pajak: ", kevin_detail_pajak)
print("Detail tunjangan", kevin_detail_tunjangan)