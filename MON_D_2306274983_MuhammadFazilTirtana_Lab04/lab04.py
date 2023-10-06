# LAB 4 | Dasar-Dasar Pemrograman 1
# Nama: Muhammad Fazil Tirtana
# Jurusan: Ilmu Komputer
# Kode Asdos: MON
# Kelas: D
# NPM: 2306274983

import sys


def print_headers():
    """
    Mencetak header tabel dengan kolom-kolom yang sesuai.
    """
    print(
        "| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format(
            "No", "Smartphone", "Price", "Screensize", "RAM"
        )
    )
    print("================================================================")


def print_table(filename: str):
    """
    Mencetak seluruh informasi dalam file dengan format tabel rapi ke layar.

    Parameters:
        filename (string): Nama file yang akan dicetak seluruh informasinya.
    """
    print_headers()
    data = read_data(filename)

    # Menggunakan enumerate untuk mendapatkan nomor urut (n) dan baris dari list data
    for n, row in enumerate(data, start=1):
        print(
            f"| {n: <2} | {row[0]: <25} | {row[1]: <8} | {row[2]: <10} | {row[3]: <3} |"
        )
    print()


def search_phone(filename: str, keyword: str):
    """
    Mencari baris data yang nama smartphonenya mengandung kata kunci (case insensitive) dan mencetaknya dalam format tabel.

    Parameters:
        filename (string): Nama file yang berisi informasi untuk dicetak.
        keyword (str): Kata kunci pencarian.
    """
    print_headers()

    data = read_data(filename)
    matches = []

    for row in data:  # Melakukan iterasi melalui setiap baris dalam data
        # Memeriksa kata kunci (case insensitive) dalam elemen pertama (indeks 0) dari setiap baris
        if keyword.lower() in row[0].lower():
            # Jika kata kunci cocok (dalam lowercase), tambahkan baris ini ke list "matches"
            matches.append(row)

    # Menggunakan enumerate untuk mendapatkan nomor urut (n) dan baris dari list matches
    for n, row in enumerate(matches, start=1):
        print(
            f"| {n: <2} | {row[0]: <25} | {row[1]: <8} | {row[2]: <10} | {row[3]: <3} |"
        )

    # Memeriksa apakah matches memiliki data atau tidak
    if matches:
        row_count = len(matches)
        col_count = len(matches[0])
    else:
        # Jika matches kosong, jumlah baris dan kolom adalah 0
        row_count = 0
        col_count = 0

    print(f"Ukuran data dari hasil pencarian: {row_count} x {col_count}")


def desc_stat(filename: str, column: int):
    """
    Mencetak statistik deskriptif (minimum, maksimum, dan rata-rata) dari data pada kolom yang dipilih.

    Parameters:
        filename (string): Nama file yang berisi informasi untuk dianalisis.
        column (int): indeks kolom (berbasis 0).
    """
    data = read_data(filename)

    # Memeriksa apakah indeks kolom valid
    if column < 0 or column >= len(data[0]):
        print("Kolom tidak valid")
        sys.exit(1)

    values = []

    for row in data:  # Melakukan iterasi melalui setiap baris dalam data
        values.append(float(row[column]))

    print(f"Min data: {min(values)}")
    print(f"Max data: {max(values)}")
    print(f"Rata - rata: {sum(values)/len(values)}")


def read_data(filename: str):
    """
    Membaca data dari file dan mereturn list of list.

    Parameters:
        filename (string): Nama file yang akan dibaca.

    Returns:
        list of list: Data dalam bentuk list of list.
    """
    try:
        # Membuka file dengan mode "r" (membaca) dengan menggunakan konteks "with"
        # Untuk memastikan bahwa file akan ditutup secara otomatis setelah operasi selesai
        with open(filename, "r") as f:
            lines = f.read().splitlines()
            data = []  # List untuk menyimpan data dari file
            for line in lines:  # Melakukan iterasi melalui setiap baris dalam list string
                row = line.split("\t")  # Membagi baris menjadi kolom berdasarkan tab
                data.append(row)
            return data
    except FileNotFoundError:
        print("Maaf, file input tidak ada")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script_name.py <file_path> <search_keyword> <column_num>")
        sys.exit(1)

    file_path = sys.argv[1]
    key = sys.argv[2]
    column_num = int(sys.argv[3])

    # Memanggil function untuk mencetak tabel data, mencari smartphone, dan menghitung statistik
    print_table(file_path)
    search_phone(file_path, key)
    desc_stat(file_path, column_num)
