# Inisialisasi variabel file_input dan file_output
file_input = None
file_output = None

# Loop hingga file input valid dimasukkan
while file_input is None:
    print("Selamat datang! Masukkan dua nama file yang berisi daftar makanan yang kamu miliki.")

    # Minta pengguna untuk memasukkan nama file input dan output
    file_input = input("Masukkan nama file input daftar makanan: ")
    file_output = input("Masukkan nama file output: ")
    
    # Periksa apakah file input ada
    try:
        with open(file_input) as file:
            pass
    except FileNotFoundError:
        print("\nMaaf, file input tidak ada\n")
        file_input = None

    # Coba membuka file output dalam mode 'r+' untuk menghapus isinya (jika ada)
    try:
        with open(file_output, 'r+') as file:
            file.truncate(0)
    except:
        pass

# Fungsi untuk mencetak menu pilihan action
def print_menu():
    print("")
    print("Apa yang ingin kamu lakukan?")
    print("================================================")
    print("1. Tampilkan daftar makanan pertama")
    print("2. Tampilkan daftar makanan kedua")
    print("3. Tampilkan gabungan makanan dari dua daftar")
    print("4. Tampilkan makanan yang sama dari dua daftar")
    print("5. Keluar")
    print("================================================")

# Fungsi untuk menampilkan daftar makanan dari file input yang pertama
def tampilkan_daftar_makanan_pertama(file_input, file_output):
    print("")
    daftar_makanan_pertama = ""
    with open(file_input, "r") as file:
        # Membaca baris pertama dari file input, mengubahnya menjadi huruf kecil, dan menghapus 18 karakter pertama dan karakter newline
        lines = file.readlines()[0].lower()[18:].strip("\n")
        lines += ","

        # Loop untuk memproses daftar makanan
        while lines != "":
            makanan = ""  # Variabel untuk menyimpan nama makanan sementara
            for n in range(len(lines)):
                if lines[n] != ",":
                    makanan += lines[n]  # Menambahkan karakter ke variabel makanan
                else:
                    lines = lines[n+1:]  # Menghapus makanan yang telah diproses dari lines
                    break  # Keluar dari loop saat tanda koma ditemukan

            # Memastikan tidak ada duplikat makanan dalam daftar
            if makanan not in daftar_makanan_pertama:
                daftar_makanan_pertama += f"{makanan},"

    with open(file_output, "a") as file:
        print("Daftar makanan pertama:")
        print(daftar_makanan_pertama[:-1])
        file.write("Daftar makanan pertama:\n")
        file.write(f"{daftar_makanan_pertama[:-1]}\n\n")
    file.close()

# Fungsi untuk menampilkan daftar makanan dari file input yang kedua
def tampilkan_daftar_makanan_kedua(file_input, file_output):
    print("")
    daftar_makanan_kedua = ""
    with open(file_input, "r") as file:
        # Membaca baris kedua dari file input, mengubahnya menjadi huruf kecil, dan menghapus 18 karakter pertama dan karakter newline
        lines = file.readlines()[1].lower()[18:].strip("\n")
        lines += ","

        # Loop untuk memproses daftar makanan
        while lines != "":
            makanan = ""  # Variabel untuk menyimpan nama makanan sementara
            for n in range(len(lines)):
                if lines[n] != ",":
                    makanan += lines[n]  # Menambahkan karakter ke variabel makanan
                else:
                    lines = lines[n+1:]  # Menghapus makanan yang telah diproses dari lines
                    break  # Keluar dari loop saat tanda koma ditemukan

            # Memastikan tidak ada duplikat makanan dalam daftar
            if makanan not in daftar_makanan_kedua:
                daftar_makanan_kedua += f"{makanan},"

    with open(file_output, "a") as file:
        print("Daftar makanan kedua:")
        print(daftar_makanan_kedua[:-1])
        file.write("Daftar makanan kedua:\n")
        file.write(f"{daftar_makanan_kedua[:-1]}\n\n")
    file.close()

# Fungsi untuk menampilkan gabungan daftar makanan dari kedua file input
def tampilkan_gabungan_makanan(file_input, file_output):
    print("")
    with open(file_input, "r") as file:
        lines = file.readlines()
        # Membaca daftar makanan pertama dan kedua, mengubahnya menjadi huruf kecil, dan menghapus 18 karakter pertama dan karakter newline
        daftar_makanan_pertama = lines[0].lower()[18:].strip("\n")
        daftar_makanan_kedua = lines[1].lower()[18:].strip("\n")
        daftar_gabungan_makanan = ""
        daftar_makanan_pertama += ","
        daftar_makanan_kedua += ","

        # Loop untuk memproses daftar makanan pertama
        while daftar_makanan_pertama != "":
            makanan = ""  # Variabel untuk menyimpan nama makanan sementara
            for n in range(len(daftar_makanan_pertama)):
                if daftar_makanan_pertama[n] != ",":
                    makanan += daftar_makanan_pertama[n]  # Menambahkan karakter ke variabel makanan
                else:
                    daftar_makanan_pertama = daftar_makanan_pertama[n+1:]  # Menghapus makanan yang telah diproses dari lines
                    break  # Keluar dari loop saat tanda koma ditemukan

            # Memastikan tidak ada duplikat makanan dalam daftar gabungan
            if makanan not in daftar_gabungan_makanan:
                daftar_gabungan_makanan += f"{makanan},"

        # Loop untuk memproses daftar makanan kedua
        while daftar_makanan_kedua != "":
            makanan = ""  # Variabel untuk menyimpan nama makanan sementara
            for n in range(len(daftar_makanan_kedua)):
                if daftar_makanan_kedua[n] != ",":
                    makanan += daftar_makanan_kedua[n]  # Menambahkan karakter ke variabel makanan
                else:
                    daftar_makanan_kedua = daftar_makanan_kedua[n+1:]  # Menghapus makanan yang telah diproses dari lines
                    break  # Keluar dari loop saat tanda koma ditemukan
                
            # Memastikan tidak ada duplikat makanan dalam daftar gabungan
            if makanan not in daftar_gabungan_makanan:
                daftar_gabungan_makanan += f"{makanan},"

        with open(file_output, "a") as file:
            print("Gabungan makanan favorit dari kedua daftar:")
            print(daftar_gabungan_makanan[:-1])
            file.write("Gabungan makanan favorit dari kedua daftar:\n")
            file.write(f"{daftar_gabungan_makanan[:-1]}\n\n")
    file.close()

# Fungsi untuk menampilkan makanan yang sama dari kedua file input
def tampilkan_makanan_sama(file_input, file_output):
    print("")
    with open(file_input, "r") as file:
        lines = file.readlines()
        # Membaca daftar makanan pertama dan kedua, mengubahnya menjadi huruf kecil, dan menghapus 18 karakter pertama dan karakter newline
        daftar_makanan_pertama = lines[0].lower()[18:].strip("\n")
        daftar_makanan_kedua = lines[1].lower()[18:].strip("\n")
        daftar_makanan_sama = ""
        daftar_makanan_pertama += ","

        # Loop untuk memproses daftar makanan
        while daftar_makanan_pertama != "":
            makanan = ""  # Variabel untuk menyimpan nama makanan sementara
            for n in range(len(daftar_makanan_pertama)):
                if daftar_makanan_pertama[n] != ",":
                    makanan += daftar_makanan_pertama[n]  # Menambahkan karakter ke variabel makanan
                else:
                    daftar_makanan_pertama = daftar_makanan_pertama[n+1:]  # Menghapus makanan yang telah diproses dari lines
                    break  # Keluar dari loop saat tanda koma ditemukan

            # Jika makanan ada dalam daftar makanan kedua, tambahkan ke daftar makanan yang sama
            if makanan in daftar_makanan_kedua and makanan not in daftar_makanan_sama:
                daftar_makanan_sama += f"{makanan},"

        with open(file_output, "a") as file:
            if daftar_makanan_sama[:-1] == "":
                print("Tidak ada makanan yang sama dari kedua daftar.")
                file.write("Tidak ada makanan yang sama dari kedua daftar.\n\n")
            else:
                print("Makanan yang sama dari dua daftar:")
                print(daftar_makanan_sama[:-1])
                file.write("Makanan yang sama dari dua daftar:\n")
                file.write(f"{daftar_makanan_sama[:-1]}\n\n")
    file.close()

# Loop utama untuk menampilkan menu dan memproses pilihan pengguna
while True:
    print_menu()
    pilihan = int(input("Masukkan aksi yang ingin dilakukan: "))
    if pilihan == 1:
        tampilkan_daftar_makanan_pertama(file_input, file_output)
    elif pilihan == 2:
        tampilkan_daftar_makanan_kedua(file_input, file_output)
    elif pilihan == 3:
        tampilkan_gabungan_makanan(file_input, file_output)
    elif pilihan == 4:
        tampilkan_makanan_sama(file_input, file_output)
    elif pilihan == 5:
        # Menghapus 2 baris terakhir dari file output dan keluar dari program
        file = open(file_output, "r")
        lines = file.read().split("\n")
        lines = "\n".join(lines[:-2])
        file.close()
        file = open(file_output, "w+")
        for i in range(len(lines)):
            file.write(lines[i])
        file.close()
        print("\nTerima kasih telah menggunakan program ini!")
        print(f"Semua keluaran telah disimpan pada file {file_output}")
        break
    else:
        print("Perintah tidak diketahui!")
