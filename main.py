# main.py

from program import TokoBuku

# Inisialisasi objek TokoBuku
toko_buku = TokoBuku()

# Loop utama program
while True:
    print("\n===== Blue Book Store =====")
    print("Selamat datang di Blue Book Store!")
    print("Silakan pilih menu:")
    print("1. Pemesanan Buku")
    print("2. Tambah Buku")
    print("3. Tampilkan Daftar Buku")
    print("4. Keluar")
    pilihan_awal = input("Masukkan pilihan (1-4): ")

    # Pilihan menu untuk pemesanan buku
    if pilihan_awal == "1":
        toko_buku.pesan_buku()

    # Pilihan menu untuk menambah buku
    elif pilihan_awal == "2":
        judul = input("Masukkan judul buku: ")
        harga = int(input("Masukkan harga buku: "))
        toko_buku.tambah_buku(judul, harga)

    # Pilihan menu untuk menampilkan daftar buku
    elif pilihan_awal == "3":
        toko_buku.tampilkan_daftar_buku()

    # Pilihan menu untuk keluar dari program
    elif pilihan_awal == "4":
        print("Terima kasih! Program berakhir.")
        break

    # Pilihan tidak valid
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
