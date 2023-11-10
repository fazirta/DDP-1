# LAB 7 | Dasar-Dasar Pemrograman 1
# Nama: Muhammad Fazil Tirtana
# Jurusan: Ilmu Komputer
# Kode Asdos: MON
# Kelas: D
# NPM: 2306274983


def print_menu():
    """
    Mencetak menu utama program.
    """

    print("\n=====================================================================")
    print("Selamat Datang di Relation Finder! Pilihan yang tersedia:")
    print("1. CEK_KETURUNAN")
    print("2. CETAK_KETURUNAN")
    print("3. JARAK_GENERASI")
    print("4. EXIT")


def create_tree(relation_data):
    """
    Mengubah relation data berbentuk pasangan relasi (parent, child) menjadi dictionary dengan parent sebagai key dan list childs sebagai value.
    Parameters:
        relation_data (list): data relasi berisi pasangan (parent, child)
    Returns:
        dictionary: relation_data yang telah diubah formatnya
    """

    # Inisialisasi dictionary untuk menyimpan struktur family tree
    family_tree = {}

    # Iterasi melalui setiap pasangan relasi (parent, child) dalam relation_data
    for parent, child in relation_data:
        # Jika parent belum ada dalam family_tree, tambahkan dengan nilai awal berupa list kosong
        if parent not in family_tree:
            family_tree[parent] = []

        # Tambahkan child ke dalam list keturunan parent
        family_tree[parent].append(child)

    # Kembalikan struktur family tree yang telah dibuat
    return family_tree


def cek_keturunan(family_tree, parent, child):
    """
    Mengecek apakah suatu child merupakan keturunan dari suatu parent, baik secara langsung maupun tidak.
    Parameters:
        family_tree (dictionary): data relasi parent dengan list childs
        parent (string): parent
        child (string): child
    Returns:
        string: pesan berisi apakah suatu child merupakan keturunan dari suatu parent
    """

    # Jika nama parent dan child sama
    if parent == child:
        return f"{child} bukan merupakan keturunan dari {parent}"

    # Set untuk melacak node yang sudah dikunjungi selama pencarian
    visited = set()

    # Fungsi rekursif untuk melakukan Depth First Search (DFS)
    def dfs(current):
        # Jika node saat ini adalah node child yang dicari dan node terdapat di data family_tree, kembalikan True
        if current == child and (
            (current in family_tree.keys())
            or (current in [j for i in family_tree.values() for j in i])
        ):
            return True

        # Tandai node saat ini sebagai sudah dikunjungi
        visited.add(current)

        # Jika node saat ini memiliki keturunan, rekursi ke setiap keturunan
        if current in family_tree:
            for keturunan in family_tree[current]:
                # Jika keturunan belum dikunjungi dan merupakan keturunan yang dicari, kembalikan True
                if keturunan not in visited and dfs(keturunan):
                    return True

        # Jika tidak ada hubungan keturunan ditemukan, kembalikan False
        return False

    return (
        f"{child} benar merupakan keturunan dari {parent}"
        if dfs(parent)
        else f"{child} bukan merupakan keturunan dari {parent}"
    )


def cetak_keturunan(family_tree, parent):
    """
    Fungsi rekursif yang mencetak seluruh child dari suatu parent, baik yang merupakan child secara langsung maupun tidak.
    Parameters:
        family_tree (dictionary): data relasi parent dengan list childs
        parent (string): parent
    """

    # Periksa apakah parent ada dalam family_tree
    if parent in family_tree:
        # Inisialisasi output dengan tanda hubung sebagai awal
        output = "-"

        # Iterasi melalui setiap nama keturunan dan tambahkan ke output
        for nama in family_tree[parent]:
            output += " " + nama

        # Cetak output untuk parent saat ini
        print(output)

        # Rekursif: Panggil fungsi cetak_keturunan untuk setiap keturunan
        for keturunan in family_tree[parent]:
            cetak_keturunan(family_tree, keturunan)


def jarak_generasi(family_tree, parent, child):
    """
    Menghitung jarak antara suatu parent dan suatu child.
    Parameters:
        family_tree (dictionary): data relasi parent dengan list childs
        parent (string): parent
        child (string): child
    Returns:
        string: pesan berisi jarak generasi
    """

    # Set untuk melacak node yang sudah dikunjungi selama pencarian
    visited = set()

    # Fungsi rekursif untuk melakukan Depth First Search (DFS)
    def dfs(current, depth):
        # Jika node saat ini adalah node child yang dicari, kembalikan depth
        if current == child:
            return depth

        # Tandai node saat ini sebagai sudah dikunjungi
        visited.add(current)

        # Jika node saat ini memiliki keturunan, rekursi ke setiap keturunan
        if current in family_tree:
            for keturunan in family_tree[current]:
                # Jika keturunan belum dikunjungi, rekursi dan tambahkan depth
                if keturunan not in visited:
                    jarak = dfs(keturunan, depth + 1)
                    # Jika jarak ditemukan, kembalikan jarak
                    if jarak is not None:
                        return jarak

        # Jika pencarian tidak menemukan hubungan, kembalikan None
        return None

    # Panggil fungsi dfs dengan node awal (parent) dan depth awal (0)
    jarak = dfs(parent, 0)

    # Hasilkan pesan berdasarkan hasil pencarian
    return (
        f"{parent} memiliki hubungan dengan {child} sejauh {jarak}"
        if jarak is not None
        else f"Tidak ada hubungan antara {parent} dengan {child}"
    )


def proses_pilihan(relation_data, pilihan):
    # Jika pilihan adalah "1", minta input nama parent dan child, lalu cetak hasil cek keturunan
    if pilihan == "1":
        parent = input("Masukkan nama parent: ")
        child = input("Masukkan nama child: ")
        print(cek_keturunan(relation_data, parent, child))
        print()
    # Jika pilihan adalah "2", minta input nama parent, lalu cetak keturunan
    elif pilihan == "2":
        parent = input("Masukkan nama parent: ")
        cetak_keturunan(relation_data, parent)
        print()
    # Jika pilihan adalah "3", minta input nama parent dan child, lalu cetak jarak generasi
    elif pilihan == "3":
        parent = input("Masukkan nama parent: ")
        child = input("Masukkan nama child: ")
        print(jarak_generasi(relation_data, parent, child))
        print()
    # Jika pilihan tidak valid, cetak pesan kesalahan
    else:
        print("Pilihan tidak valid.")


# Memastikan bahwa script ini dijalankan sebagai program utama
if __name__ == "__main__":
    # Inisialisasi list untuk menyimpan relation_data
    relation_data = []

    # Menampilkan pesan untuk meminta input relation_data dari pengguna
    print("Masukkan data relasi: ")

    # Membaca input pengguna secara terus menerus hingga pengguna memasukkan "SELESAI"
    while True:
        input_user = input()

        # Jika input bukan "SELESAI", tambahkan tuple dari input ke dalam list relation_data
        if input_user != "SELESAI":
            # Input validation
            if len(input_user.split()) == 2:
                if input_user.split()[0] != input_user.split()[1]:
                    relation_data.append(tuple(input_user.split()))
                else:
                    print("Nama parent dan child harus berbeda")
            else:
                print("Masukkan data dengan format: <nama_parent> <nama_child>")
        else:
            # Jika input adalah "SELESAI", keluar dari loop
            break

    # Membentuk struktur family tree dari relation_data menggunakan fungsi create_tree
    relation_data = create_tree(relation_data)

    # Membaca input pengguna untuk memproses pilihan hingga pengguna memilih keluar (pilihan 4)
    while True:
        # Menampilkan opsi pilihan kepada pengguna
        print_menu()
        pilihan = input("Masukkan pilihan: ")

        # Jika pilihan adalah "4", keluar dari loop dan tampilkan pesan terima kasih
        if pilihan == "4":
            print("Terima kasih telah menggunakan Relation Finder!")
            break
        else:
            # Jika pilihan bukan "4", panggil fungsi proses_pilihan dengan relation_data dan pilihan pengguna
            proses_pilihan(relation_data, pilihan)
