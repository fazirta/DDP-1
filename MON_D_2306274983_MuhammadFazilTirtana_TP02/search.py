# TP 2 | Dasar-Dasar Pemrograman 1
# Nama: Muhammad Fazil Tirtana
# Jurusan: Ilmu Komputer
# Kode Asdos: MON
# Kelas: D
# NPM: 2306274983

import os
import sys
import time


def get_property(file):
    """
    Function untuk mendapatkan property dari suatu file.

    Args:
        file (str): Path ke file yang akan dibaca.

    Returns:
        tuple: Mengembalikan tuple yang berisi lines dan property.
    """
    with open(file) as f:
        lines = f.read().splitlines()
        property = {}
        for prop in lines[0][1:-1].split()[1:]:
            if "=" in prop:
                key, value = prop.split("=")
                property[key] = value.strip('""')
        return lines, property


def check_all(file, keyword):
    """
    Function untuk mengecek semua section dari file.

    Args:
        file (str): Path ke file yang akan dibaca.
        keyword (list): List yang berisi keyword yang akan dicari.

    Returns:
        tuple: Mengembalikan tuple yang berisi property dan hasil pencarian keyword.
    """
    check_keyword = [False, False]
    lines, property = get_property(file.path)
    check_keyword[0] = keyword[0] in " ".join(lines)
    check_keyword[1] = keyword[1] in " ".join(lines)
    return property, check_keyword


def check_section(file, section, keyword):
    """
    Function untuk mengecek section tertentu dari file.

    Args:
        file (str): Path ke file yang akan dibaca.
        section (str): section dari file yang akan dicari.
        keyword (list): List yang berisi keyword yang akan dicari.

    Returns:
        tuple: Mengembalikan tuple yang berisi property dan hasil pencarian keyword.
    """
    check_keyword = [False, False]
    lines, property = get_property(file.path)
    check = False
    for lines in lines:
        if check:
            if keyword[0] in lines:
                check_keyword[0] = True
            elif keyword[1] in lines:
                check_keyword[1] = True
            # Keluar dari loop jika sudah menemukan kedua keyword atau menemukan penutup section
            elif check_keyword[0] and check_keyword[1] or f"</{section}>" in lines:
                break
        elif f"<{section}>" in lines:
            check = True
    return property, check_keyword


def print_hasil(entry, property):
    """
    Function untuk menampilkan hasil pencarian.

    Args:
        entry (str): Nama file yang telah dicari.
        property (dict): Dictionary yang berisi property dari file.

    Returns:
        None
    """
    # Menampilkan hasil pencarian dalam format yang terstruktur
    print(f"{entry.name} {property.get('provinsi', '')[:15].rjust(15)} {property.get('klasifikasi', '')[:15].rjust(15)} {property.get('sub_klasifikasi', '')[:30].rjust(30)} {property.get('lembaga_peradilan', '')[:20].rjust(20)}")
    global document_count
    document_count += 1


# Kode di bawah ini akan dieksekusi hanya jika script ini dijalankan sebagai program utama,
# dan tidak akan dieksekusi jika diimpor sebagai library oleh script lain
if __name__ == "__main__":
    # Cek apakah argumen baris perintah cukup untuk menjalankan script
    if len(sys.argv) < 2:
        print("Usage: python search.py <section> <keyword1> [<operator> <keyword2>] [<property_filter_keyword> <value>]")
        sys.exit(1)

    # Membuat list kosong untuk argumen filter dan search
    filter_arguments = []
    search_arguments = []

    # Memproses argumen baris perintah menjadi dua list berdasarkan jumlah dan jenis argumen
    if len(sys.argv) == 3:
        search_arguments = sys.argv[1:3]
    elif len(sys.argv) == 5:
        if sys.argv[3].startswith("--"):
            filter_arguments = sys.argv[3:]
            search_arguments = sys.argv[1:3]
        else:
            search_arguments = sys.argv[1:5]
    elif len(sys.argv) > 5:
        if sys.argv[5].startswith("--"):
            filter_arguments = sys.argv[5:]
            search_arguments = sys.argv[1:5]
    else:
        # Jika jumlah argumen tidak sesuai dengan kondisi di atas, tampilkan pesan kesalahan dan keluar dari program
        print("Argumen program tidak benar.")
        sys.exit(1)

    # Membuat dictionary kosong untuk filter
    filters = {}

    # Memeriksa keberpasangan property-value argumen filter yang valid
    if len(filter_arguments) % 2 == 0:
        # Melakukan iterasi pada argumen filter dalam pasangan
        for i in range(0, len(filter_arguments), 2):
            # Memeriksa apakah argumen dimulai dengan "--" (menunjukkan itu adalah keyword property) dan argumen berikutnya bukan "--" (menunjukkan itu adalah value)
            if filter_arguments[i].startswith("--") and not filter_arguments[i + 1].startswith("--"):
                key = filter_arguments[i][2:]
                # Memeriksa apakah keyword property valid
                valid_keys = [
                    "klasifikasi",
                    "lembaga_peradilan",
                    "provinsi",
                    "status",
                    "sub_klasifikasi"
                ]
                if key.lower() in valid_keys:
                    # Menambahkan pasangan keyword property-value ke dalam dictionary filter
                    filters[key.lower()] = filter_arguments[i + 1].lower()
                else:
                    print("Filter yang diperbolehkan: klasifikasi, lembaga_peradilan, provinsi, status, sub_klasifikasi")
                    sys.exit(1)
            else:
                print("Argumen program tidak benar.")
                sys.exit(1)
    else:
        print("Argumen program tidak benar.")
        sys.exit(1)

    # Menginisialisasi variabel-variabel berdasarkan argumen pencarian atau mencetak pesan kesalahan jika argumen tidak valid
    if len(search_arguments) == 2:
        section = str(search_arguments[0]).lower()
        keyword1 = str(search_arguments[1]).lower()
        operator = ""
        keyword2 = ""
    elif len(search_arguments) == 4 and search_arguments[2].upper() in ["AND", "OR", "ANDNOT"]:
        section = str(search_arguments[0]).lower()
        keyword1 = str(search_arguments[1]).lower()
        operator = str(search_arguments[2]).upper()
        keyword2 = str(search_arguments[3]).lower()
    elif len(search_arguments) == 4 and search_arguments[2].upper() not in ["AND", "OR", "ANDNOT"]:
        print("Mode harus berupa AND, OR atau ANDNOT.")  # Mencetak pesan kesalahan
        sys.exit(1)  # Keluar dari program
    else:
        # Jika argumen program tidak valid (jumlah argumen pencarian bukan 2 atau 4)
        print("Argumen program tidak benar.")
        sys.exit(1)

    document_count = 0  # Menginisialisasi penghitung dokumen

    start_time = time.time()  # Menginisialisasi waktu mulai

    # Melakukan iterasi pada setiap entri dalam folder 'dataset'
    for entry in os.scandir("dataset"):
        # Memeriksa semua bagian jika section adalah 'all'
        # Jika tidak, periksa bagian tertentu
        properties, result = (check_all(entry, [keyword1, keyword2]) if section == "all" else check_section(entry, section, [keyword1, keyword2]))
        # Mengasumsikan di awal bahwa filter cocok
        check_filter = True
        # Melakukan iterasi pada setiap kunci dalam filter
        for key in filters:
            # Jika nilai filter tidak sama dengan properti yang sesuai, filter tidak cocok
            if filters[key] != properties[key]:
                check_filter = False
        # Jika filter cocok, periksa operator dan hasil pencarian
        if check_filter:
            if operator == "AND" and result[0] and result[1]:
                print_hasil(entry, properties)
            elif operator == "OR" and (result[0] or result[1]):
                print_hasil(entry, properties)
            elif operator == "ANDNOT" and result[0] and not result[1]:
                print_hasil(entry, properties)
            elif not operator and result[0]:
                print_hasil(entry, properties)

    end_time = time.time()
    print(f"Jumlah dokumen yang ditemukan = {document_count}")  # Mencetak jumlah dokumen yang ditemukan
    print(f"Waktu pencarian total = {(end_time - start_time):.3f} detik")  # Mencetak waktu total pencarian
