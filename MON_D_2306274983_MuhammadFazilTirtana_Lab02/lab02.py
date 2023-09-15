# LAB 2 | Dasar-Dasar Pemrograman 1
# Nama: Muhammad Fazil Tirtana
# Jurusan: Ilmu Komputer
# Kode Asdos: MON
# Kelas: D
# NPM: 2306274983

# Konstanta untuk persentase diskon member
DISCOUNT_PERCENTAGE = 0.8

# Dictionary yang berisi katalog buku beserta harganya
katalog_buku = {  
    "x-man": 7000,
    "doraemoh": 5500,
    "nartoh": 4000
}

# Fungsi untuk mencetak menu utama
def print_menu():
    print("Selamat Datang di Toko Buku Place Anak Chill")
    print("============================================")
    print("1. Pinjam buku")
    print("2. Keluar")
    print("============================================")

# Fungsi untuk memeriksa ID member
def periksa_id(status_membership):
    if status_membership:
        tidak_valid = 0
        while tidak_valid < 3:
            id_membership = input("Masukkan ID anda (5 digit): ")
            if len(id_membership) == 5 and sum(int(n) for n in id_membership) == 23:
                print("Login member berhasil!")
                return True
            else:
                tidak_valid += 1
                print("ID anda salah!")
        else:
            print("Program akan kembali ke menu utama\n")
            return False
    else:
        print("Login non-member berhasil!")
        return True

# Fungsi untuk menghitung total harga peminjaman buku
def hitung_total_harga(judul_buku, durasi, status_membership):
    harga = katalog_buku.get(judul_buku.lower(), 0) * durasi
    if status_membership:
        harga *= DISCOUNT_PERCENTAGE
    return harga

# Fungsi untuk proses peminjaman buku
def pinjam_buku():
    nama = input("Masukkan nama anda: ")
    saldo = int(input("Masukkan saldo anda (Rp): "))
    status_membership = input("Apakah anda member? [Y/N]: ")
    status_membership = True if status_membership == "Y" else False
    if periksa_id(status_membership):
        while True:
            print("\n============================================")
            print("Katalog Buku Place Anak Chill")
            print("============================================")
            for judul, harga in katalog_buku.items():
                print(f"{judul.capitalize()} (Rp {f'{harga:,.0f}'.replace(',', '.')}/hari)")
            print("============================================")
            print("Exit")
            print("============================================")            
            judul_buku = input("Buku yang dipilih: ")
            if judul_buku == "exit":
                break
            elif judul_buku.lower() in katalog_buku:
                durasi = int(input("Ingin melakukan peminjaman untuk berapa hari: "))
                if durasi <= 0:
                    print("Durasi penyewaan harus lebih dari 0 hari.")
                    continue
                total_harga = hitung_total_harga(judul_buku, durasi, status_membership)
                if saldo >= total_harga:
                    saldo -= total_harga
                    print(f"Berhasil meminjam buku {judul_buku} selama {durasi} hari\nSaldo anda saat ini Rp{saldo}")
                else:
                    selisih_saldo_dan_total_harga = total_harga - saldo
                    print(f"Tidak berhasil meminjam! Saldo anda kurang {selisih_saldo_dan_total_harga}")
            else:
                print("Komik tidak ditemukan. Masukkan kembali judul komik sesuai katalog!")

# Loop utama untuk menjalankan program
while True:
    print_menu()
    pilihan = int(input("Apa yang ingin anda lakukan: "))
    if pilihan == 1:
        pinjam_buku()
    elif pilihan == 2:
        print("Terima kasih telah mengunjungi Toko Buku Place Anak Chill!")
        break
    else:
        print("Perintah tidak diketahui!")
