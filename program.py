# program.py

# Mengimpor modul datetime dari library Python
from datetime import datetime

# Definisikan kelas TokoBuku untuk mengelola operasi-operasi toko buku
class TokoBuku:
    # Metode konstruktor untuk inisialisasi objek kelas
    def __init__(self):
        # Inisialisasi daftar buku sebagai atribut kelas
        self.daftar_buku = []

    # Metode untuk menambahkan buku ke dalam daftar
    def tambah_buku(self, judul, harga):
        buku_baru = {"judul": judul, "harga": harga}
        self.daftar_buku.append(buku_baru)
        # Mencetak pesan bahwa buku telah ditambahkan
        print(f"Buku '{judul}' telah ditambahkan ke dalam toko.")

    # Metode untuk menampilkan daftar buku yang tersedia
    def tampilkan_daftar_buku(self):
        # Mencetak header daftar buku
        print("\n=== Daftar Buku ===")
        # Memeriksa apakah daftar buku kosong
        if not self.daftar_buku:
            print("Tidak ada buku saat ini.")
        else:
            # Menampilkan setiap buku dalam daftar dengan nomor urut
            for i, buku in enumerate(self.daftar_buku, 1):
                print(f"{i}. {buku['judul']} - Harga: {buku['harga']}")

    # Metode untuk melakukan pemesanan buku
    def pesan_buku(self):
        # Memeriksa apakah daftar buku kosong
        if not self.daftar_buku:
            print("Tidak ada buku yang tersedia untuk dipesan.")
            return

        # Menampilkan daftar buku
        self.tampilkan_daftar_buku()

        # Meminta input nomor buku yang ingin dipesan
        nomor_buku = int(input("Masukkan nomor buku yang ingin dipesan (masukkan 0 untuk membatalkan): "))

        # Memeriksa apakah pemesanan dibatalkan
        if nomor_buku == 0:
            print("Pemesanan dibatalkan.")
            return

        # Memeriksa apakah nomor buku valid
        if 1 <= nomor_buku <= len(self.daftar_buku):
            buku_dipesan = self.daftar_buku[nomor_buku - 1]
            # Meminta input jumlah pesanan
            jumlah_pesanan = int(input(f"Masukkan jumlah pesanan untuk buku '{buku_dipesan['judul']}': "))
            total_harga = buku_dipesan["harga"] * jumlah_pesanan

            # Menampilkan informasi pemesanan
            print(f"Pemesanan untuk buku '{buku_dipesan['judul']}' sejumlah {jumlah_pesanan} berhasil.")
            print(f"Total harga: {total_harga}")

            # Meminta input jumlah uang yang dibayarkan
            uang_pembayaran = float(input("Masukkan jumlah uang yang dibayarkan: "))

            # Melakukan validasi pembayaran
            while uang_pembayaran < total_harga:
                print("Jumlah uang yang dibayarkan kurang dari total harga. Silakan masukkan jumlah uang yang cukup.")
                uang_pembayaran = float(input("Masukkan jumlah uang yang dibayarkan: "))

            # Menghitung kembalian
            kembalian = uang_pembayaran - total_harga

            # Mendapatkan tanggal dan waktu sekarang
            tanggal_sekarang = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            # Membuat nama file struk
            nama_file_struk = f"Struk_{tanggal_sekarang}.txt"

            # Menyimpan struk dalam file teks
            with open(nama_file_struk, "w") as file_struk:
                file_struk.write("=== Struk Pembayaran ===\n")
                file_struk.write(f"Tanggal: {tanggal_sekarang}\n")
                file_struk.write("=======================\n")
                file_struk.write(f"{buku_dipesan['judul']} - Jumlah: {jumlah_pesanan} - Harga: {total_harga / jumlah_pesanan}\n")
                file_struk.write("=======================\n")
                file_struk.write(f"Total Harga: {total_harga}\n")
                file_struk.write(f"Uang Pembayaran: {uang_pembayaran}\n")
                file_struk.write(f"Kembalian: {kembalian}\n")

            # Menampilkan informasi struk dan pembayaran
            print(f"Struk pembayaran telah disimpan dalam file: {nama_file_struk}")
            if kembalian >= 0:
                print(f"Pembayaran berhasil. Kembalian Anda: {kembalian}")
            else:
                print("Jumlah uang yang dibayarkan kurang. Pembayaran dibatalkan.")

        # Menampilkan pesan jika nomor buku tidak valid
        else:
            print(f"Nomor buku {nomor_buku} tidak valid.")
