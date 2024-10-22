def tampilkan_harga(nama_barang):
    match nama_barang.lower():
        case 'apel':
            harga = 5000
        case 'jeruk':
            harga = 7000
        case 'mangga':
            harga = 6000
        case 'pisang':
            harga = 4000
        case _:
            return "Barang tidak ditemukan"

    return f"Harga {nama_barang.capitalize()} adalah Rp {harga}"

if __name__ == "__main__":
    # Input dari pengguna
    nama_barang = input("Masukkan nama barang: ")
    harga_barang = tampilkan_harga(nama_barang)
    print(harga_barang)