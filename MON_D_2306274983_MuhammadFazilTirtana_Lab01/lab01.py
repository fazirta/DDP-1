# LAB 1 | Dasar-Dasar Pemrograman 1
# Nama: Muhammad Fazil Tirtana
# Jurusan: Ilmu Komputer
# Kode Asdos: MON
# Kelas: D
# NPM: 2306274983

# Meminta pengguna untuk memasukkan pesan dalam format hexadecimal
pesan_kelompok_zog = input("Pesan Kelompok Zog: ")

# Mengubah pesan hexadecimal menjadi bytes
pesan_kelompok_zog = bytes.fromhex(pesan_kelompok_zog)

# Mengubah pesan bytes menjadi karakter ASCII
pesan_kelompok_zog = pesan_kelompok_zog.decode("ASCII")

# Meminta pengguna untuk memasukkan dua angka sebagai clue password
angka_1 = int(input("Angka 1: "))
angka_2 = int(input("Angka 2: "))

# Mengubah clue tersebut menjadi sebuah password
password = angka_1 * angka_2 * 13

# Mengubah password menjadi bentuk biner
password = bin(password)

# Menampilkan hasil terjemahan pesan dalam karakter ASCII
print(f"Hasil terjemahan pesan: {pesan_kelompok_zog}")

# Menampilkan password dalam bentuk biner
print(f"Password: {password}")

# Menampilkan pesan yang menandakan bahwa pesan dan password dari Kelompok Zog telah diterima
print(f'\nPesan "{pesan_kelompok_zog}" telah diterima dengan password "{password}".')
