# LAB 5 | Dasar-Dasar Pemrograman 1
# Nama: Muhammad Fazil Tirtana
# Jurusan: Ilmu Komputer
# Kode Asdos: MON
# Kelas: D
# NPM: 2306274983


def print_menu():
    """
    Mencetak menu utama program.
    """

    print("Selamat datang di Database Nilai Dek Depe")
    print("1. Tambah data ke database")
    print("2. Baca data dari database")
    print("3. Update data di database")
    print("4. Hapus data dari database")
    print("5. Keluar")


def tambah_data(database: list):
    """
    Menambahkan data ke database berdasarkan input pengguna.

    Parameters:
    database (list): Database yang akan diisi dengan data.
    """

    name = input("Masukkan nama: ")  # Meminta input nama dari pengguna
    if name.lower() not in (data[0] for data in database):  # Mengecek apakah nama sudah ada di database
        grades = []
        n = 0
        while True:  # Loop untuk meminta input nilai lab dari pengguna
            n += 1  # Menambahkan nilai n untuk menghitung nomor lab berikutnya
            while True:  # Loop untuk mengecek validasi input
                grade = input(f"Masukkan nilai Lab {n} (ketik STOP untuk selesai): ")  # Mengambil input nilai lab dari pengguna
                try:
                    if grade.upper() == "STOP":  # Jika pengguna mengetikkan "STOP", maka keluar dari loop
                        break
                    elif (0 <= float(grade) <= 100):  # Memeriksa apakah nilai lab berada dalam rentang 0 sampai 100
                        break
                    else:
                        print(f"Masukkan bilangan riil sebagai nilai lab ke-{n} dalam range 0 sampai 100 (inklusif)")  # Pesan kesalahan jika nilai tidak sesuai
                except ValueError:
                    # Pesan kesalahan jika input tidak dapat diubah menjadi bilangan riil
                    print(f"Masukkan bilangan riil sebagai nilai lab ke-{n} dalam range 0 sampai 100 (inklusif)")
                    print("Atau ketik STOP untuk selesai")
            if grade.upper() == "STOP":  # Jika pengguna mengetik 'STOP', loop akan berhenti
                break
            else:
                # Menambahkan nilai lab ke list grades
                grades.append(float(grade))
        # Menambahkan nama dan nilai lab ke database
        database.append([name.lower()] + grades)
        print(f"Berhasil menambahkan {len(grades)} nilai untuk {name} ke database\n")
    else:
        print("Nama sudah terdapat di dalam database\n")


def baca_data(database: list):
    """
    Membaca data dari database berdasarkan input pengguna.

    Parameters:
    database (list): Database yang akan dibaca.
    """

    # Meminta input nama dari pengguna
    name = input("Masukkan nama: ")
    if name.lower() in (data[0] for data in database):
        for data in database:
            if data[0] == name.lower():
                # Meminta input nomor lab yang ingin dilihat nilainya
                lab = int(input("Masukkan nilai Lab ke berapa yang ingin dilihat: "))
                if lab > 0 and lab < len(data) and data[lab] != None:
                    # Mencetak nilai lab yang diminta
                    print(f"Nilai Lab {lab} {name} adalah {data[lab]}\n")
                else:
                    print(f"Tidak terdapat nilai untuk Lab {lab}\n")
                break
    else:
        print("Nama tidak ada dalam database\n")


def update_data(database: list):
    """
    Mengupdate data dalam database berdasarkan input pengguna.

    Parameters:
    database (list): Database yang akan diupdate.
    """

    name = input("Masukkan nama: ")  # Meminta input nama dari pengguna
    if name.lower() in (data[0] for data in database):
        for data in database:
            if data[0] == name.lower():
                lab = int(input("Masukkan nilai Lab ke berapa yang ingin diupdate: "))  # Meminta input nomor lab yang ingin diupdate nilainya
                if lab > 0 and lab < len(data) and data[lab] != None:
                    old_grade = data[lab]
                    # Meminta input nilai baru untuk lab tersebut
                    while True:  # Loop untuk mengecek validasi input
                        new_grade = input(f"Masukkan nilai baru untuk Lab {lab}: ")  # Mengambil input nilai lab dari pengguna
                        try:
                            if (0 <= float(new_grade) <= 100):  # Memeriksa apakah nilai lab berada dalam rentang 0 sampai 100
                                new_grade = float(new_grade)
                                break
                            else:
                                print(f"Masukkan bilangan riil sebagai nilai lab ke-{lab} dalam range 0 sampai 100 (inklusif)")  # Pesan kesalahan jika nilai tidak sesuai
                        except ValueError:
                            print(f"Masukkan bilangan riil sebagai nilai lab ke-{lab} dalam range 0 sampai 100 (inklusif)")  # Pesan kesalahan jika input tidak dapat diubah menjadi bilangan riil
                    # Mengupdate nilai lab di database dengan nilai baru
                    data[lab] = new_grade
                    print(
                        f"Berhasil mengupdate nilai Lab {lab} {name} dari {old_grade} ke {new_grade}\n"
                    )
                else:
                    print(f"Tidak terdapat nilai untuk Lab {lab}\n")
                break
    else:
        print("Nama tidak ada dalam database\n")


def hapus_data(database: list):
    """
    Menghapus data dari database berdasarkan input pengguna.

    Parameters:
    database (list): Database dari mana data akan dihapus.
    """

    name = input("Masukkan nama: ")  # Meminta input nama dari pengguna
    if name.lower() in (data[0] for data in database):
        for data in database:
            if data[0] == name.lower():
                # Meminta input nomor lab yang ingin dihapus nilainya
                lab = int(input("Masukkan nilai Lab ke berapa yang ingin dihapus: "))
                if lab > 0 and lab < len(data) and data[lab] != None:
                    # Menghapus nilai lab dari database
                    data[lab] = None
                    print(f"Berhasil menghapus nilai Lab {lab} {name} dari database\n")
                else:
                    print(f"Tidak terdapat nilai untuk Lab {lab}\n")
                break
    else:
        print("Nama tidak ada dalam database\n")


if __name__ == "__main__":
    database = []  # Membuat list kosong sebagai database awal
    while True:  # Loop utama untuk menjalankan program
        print_menu()
        pilihan = int(input("Masukkan kegiatan yang ingin dilakukan: "))
        # Menjalankan fungsi berdasarkan pilihan pengguna
        if pilihan == 1:
            tambah_data(database)
        elif pilihan == 2:
            baca_data(database)
        elif pilihan == 3:
            update_data(database)
        elif pilihan == 4:
            hapus_data(database)
        elif pilihan == 5:
            # Mengakhiri program
            print("Terimakasih telah menggunakan Database Nilai Dek Depe")
            break
        else:
            print("Perintah tidak diketahui!")  # Pesan kesalahan jika input tidak sesuai
