# LAB 6 | Dasar-Dasar Pemrograman 1
# Nama: Muhammad Fazil Tirtana
# Jurusan: Ilmu Komputer
# Kode Asdos: MON
# Kelas: D
# NPM: 2306274983

import os


def print_spacer():
    print("=====================================================================")


def get_inputs(content: dict):
    data = []

    matkul, id_mahasiswa_1, id_mahasiswa_2 = None, None, None
    nama_mahasiswa_1, nama_mahasiswa_2 = None, None

    # Meminta pengguna untuk memasukkan nama mata kuliah yang ingin diperiksa
    while matkul == None and id_mahasiswa_1 == None and id_mahasiswa_2 == None:
        matkul = input("Masukkan nama mata kuliah yang ingin diperiksa: ")

        if matkul == "EXIT":
            return None, None, None, None, True

        found = False

        # Memeriksa apakah mata kuliah yang dimasukkan ada dalam konten
        for key in content:
            if matkul == key[2]:
                found = True
                break

        # Jika mata kuliah tidak ditemukan, tampilkan pesan kesalahan
        if not found:
            print(f"{matkul} tidak ditemukan\n")
            print_spacer()
            matkul, id_mahasiswa_1, id_mahasiswa_2 = None, None, None
            continue

        # Meminta pengguna untuk memasukkan nama/NPM mahasiswa 1
        id_mahasiswa_1 = input("Masukkan nama/NPM mahasiswa 1: ")
        found = False

        # Memeriksa apakah informasi mahasiswa 1 ada dalam konten
        for key in content:
            if (
                id_mahasiswa_1 == key[0] or id_mahasiswa_1 == key[1]
            ) and matkul.strip() == key[2].strip():
                found = True
                data.append(content[key])
                nama_mahasiswa_1 = key[0]

        # Jika informasi mahasiswa 1 tidak ditemukan, tampilkan pesan kesalahan
        if not found:
            print(f"Informasi mahasiswa tidak ditemukan\n")
            print_spacer()
            matkul, id_mahasiswa_1, id_mahasiswa_2 = None, None, None
            continue

        # Meminta pengguna untuk memasukkan nama/NPM mahasiswa 2
        id_mahasiswa_2 = input("Masukkan nama/NPM mahasiswa 2: ")
        found = False

        # Memeriksa apakah informasi mahasiswa 2 ada dalam konten
        for key in content:
            if (
                id_mahasiswa_2 == key[0] or id_mahasiswa_2 == key[1]
            ) and matkul.strip() == key[2].strip():
                found = True
                data.append(content[key])
                nama_mahasiswa_2 = key[0]

        # Jika informasi mahasiswa 2 tidak ditemukan, tampilkan pesan kesalahan
        if not found:
            print(f"Informasi mahasiswa tidak ditemukan\n")
            print_spacer()
            matkul, id_mahasiswa_1, id_mahasiswa_2 = None, None, None
            continue

    return matkul, nama_mahasiswa_1, nama_mahasiswa_2, data, False


def read_file():
    data = {}  # Membuat dictionary kosong untuk menyimpan data dari file

    # Melakukan iterasi pada setiap entri dalam folder
    for entry in filter(lambda x: x[-4:] == ".txt", os.listdir("./")):
        with open(entry, encoding="utf-8-sig") as f:
            lines = f.read().splitlines()  # Membaca semua baris dalam file
            for i in range(len(lines)):
                if (
                    len(lines[i].split(";")) == 3
                ):  # Memeriksa apakah baris ini memiliki 3 bagian terpisah oleh tanda semicolon
                    # Membuat tuple sebagai key untuk dictionary data
                    data[
                        (
                            lines[i].split(";")[0],  # Nama
                            lines[i].split(";")[1],  # NPM
                            lines[i].split(";")[2],  # Mata kuliah
                        )
                    ] = set(
                        lines[i + 2].split()
                    )  # Membuat set dari 2 line berikutnya
    return data  # Mengembalikan dictionary yang berisi data dari file


def get_similar_keywords(data: list):
    similar_keywords = []  # Membuat list kosong untuk menyimpan kata kunci yang sama

    keywords_1 = data[0]  # Set berisi keywords dari mahasiswa pertama
    keywords_2 = data[1]  # Set berisi keywords dari mahasiswa kedua

    # Membandingkan kata kunci dari kedua mahasiswa dan menyimpan kata kunci yang sama
    for keyword in keywords_1:
        if keyword in keywords_2:
            similar_keywords.append(keyword)

    return similar_keywords  # Mengembalikan list kata kunci yang sama


if __name__ == "__main__":
    print("Selamat datang di program Plagiarism Checker!")  # Pesan selamat datang

    while True:  # Loop utama untuk menjalankan program
        print_spacer()  # Memanggil fungsi untuk mencetak garis pemisah

        content = (
            read_file()
        )  # Membaca data dari file dan menyimpannya dalam variabel content
        matkul, nama_mahasiswa_1, nama_mahasiswa_2, data, exit = get_inputs(
            content
        )  # Meminta input dari pengguna

        if exit:  # Jika pengguna memilih untuk keluar
            print(
                "Terima kasih telah menggunakan program Plagiarism Checker!"
            )  # Menampilkan pesan terima kasih
            break  # Keluar dari loop utama

        similar_keywords = get_similar_keywords(
            data
        )  # Mendapatkan kata kunci yang sama
        percentage = round(
            (len(similar_keywords) / len(data[1])) * 100, 2
        )  # Menghitung persentase kemiripan

        print(
            "============================= Hasil ================================="
        )  # Menampilkan judul hasil

        # Menampilkan tingkat kemiripan dan pesan berdasarkan persentase kemiripan
        print(
            f"Tingkat kemiripan tugas {matkul} {nama_mahasiswa_1} dan {nama_mahasiswa_2} adalah {percentage}%."
        )

        if (
            percentage < 31
        ):  # Jika persentase kurang dari 31, tidak terindikasi plagiarisme
            print(
                f"{nama_mahasiswa_1} dan {nama_mahasiswa_2} tidak terindikasi plagiarisme.\n"
            )
        elif (
            30 < percentage < 71
        ):  # Jika persentase antara 31 dan 70, terindikasi plagiarisme ringan
            print(
                f"{nama_mahasiswa_1} dan {nama_mahasiswa_2} terindikasi plagiarisme ringan.\n"
            )
        else:  # Jika persentase 71 atau lebih, terindikasi plagiarisme
            print(
                f"{nama_mahasiswa_1} dan {nama_mahasiswa_2} terindikasi plagiarisme.\n"
            )
