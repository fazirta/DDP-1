# TP 4 | Dasar-Dasar Pemrograman 1
# Nama: Muhammad Fazil Tirtana
# Jurusan: Ilmu Komputer
# Kode Asdos: MON
# kelas: D
# NPM: 2306274983

import tkinter as tk
from tkinter import messagebox
import requests

# Membuat class BarcodeCanvas yang merupakan inheritance dari class Canvas di modul tkinter
class BarcodeCanvas(tk.Canvas):
    def __init__(self, master: tk.Tk, bg: str, width: int, height: int, **kw):
        super().__init__(master=master, bg=bg, width=width, height=height, **kw)
        self.width, self.height = width, height
        self.font_size = self.width // 20

    # Method untuk menghasilkan barcode EAN-13
    def generate(self, input_code, checkdigit):
        # Menghapus elemen-elemen sebelumnya pada canvas
        self.delete("all")

        # Menampilkan text "EAN-13 Barcode:" di tengah canvas
        self.create_text(
            self.width / 2,
            self.font_size * 2,
            text="EAN-13 Barcode:",
            fill="black",
            font=(f"Helvetica {self.font_size} bold"),
        )

        # Menampilkan text "Check Digit:" beserta nilai checkdigit pada bagian bawah canvas
        self.create_text(
            self.width / 2,
            self.height - self.font_size,
            text=f"Check Digit: {checkdigit}",
            fill="orange",
            font=(f"Helvetica {self.font_size} bold"),
        )

        # Menggabungkan kode input dan digit cek untuk membentuk barcode lengkap.
        self.code = input_code + str(checkdigit)
        # Inisialisasi lebar setiap batang di barcode, relatif terhadap ukuran font.
        self.bar_width = self.font_size / 8
        # Inisialisasi lebar total barcode. Sebuah barcode EAN-13 memiliki 95 batang.
        self.barcode_width = 95 * self.bar_width
        # Menghitung koordinat x awal untuk barcode, berpusat pada canvas.
        self.start_x = (self.width - self.barcode_width) / 2
        # Inisialisasi koordinat y awal untuk barcode.
        self.start_y = 70
        # Inisialisasi tinggi batang penjaga.
        self.guard_bars_height = self.bar_width * 60
        # Inisialisasi tinggi batang biasa. Batang biasa lebih pendek daripada batang penjaga.
        self.bar_height = self.guard_bars_height - (self.font_size * 0.8)

        # Membuat variabel first_bit_pattern dan menginisialisasikannya sebagai string kosong.
        # Variabel ini akan digunakan untuk menyimpan pola bit dari 6 digit pertama barcode.
        self.first_bit_pattern = ""
        # Membuat variabel second_bit_pattern dan menginisialisasikannya sebagai string kosong.
        # Variabel ini akan digunakan untuk menyimpan pola bit dari 6 digit kedua barcode.
        self.second_bit_pattern = ""

        # Kode untuk guard bars pada barcode
        self.GUARD_BARS = {
            "start": "101",
            "middle": "01010",
            "end": "101",
        }

        # Kode untuk struktur barcode
        self.STRUCTURE = [
            "LLLLLL",
            "LLGLGG",
            "LLGGLG",
            "LLGGGL",
            "LGLLGG",
            "LGGLLG",
            "LGGGLL",
            "LGLGLG",
            "LGLGGL",
            "LGGLGL",
        ]

        # Pola bit pada digit L
        self.L_CODE = [
            "0001101",
            "0011001",
            "0010011",
            "0111101",
            "0100011",
            "0110001",
            "0101111",
            "0111011",
            "0110111",
            "0001011",
        ]

        # Membuat pola bit untuk digit R
        # Untuk setiap bit dalam setiap kode digit L, nilai bit diubah menjadi kebalikannya (0 menjadi 1, 1 menjadi 0),
        # dan hasilnya digabungkan menjadi string pola bit digit R.
        self.R_CODE = [
            "".join([str(1 - int(bit)) for bit in code]) for code in self.L_CODE
        ]

        # Membuat pola bit untuk digit G
        # Pola bit digit G dihasilkan dengan membalik urutan karakter dalam pola bit digit R.
        self.G_CODE = [code[::-1] for code in self.R_CODE]

        # Digit pertama dari input kode
        self.first_digit = int(input_code[0])

        # 6 digit pertama dari input kode, dimulai dari index 1 hingga 6
        self.first_6_digits = input_code[1:7]

        # 6 digit kedua dari input kode, dimulai dari index 7 hingga akhir, ditambah dengan checkdigit
        self.second_6_digits = input_code[7:] + str(checkdigit)

        # Mendapatkan struktur barcode sesuai digit pertama
        self.structure = self.STRUCTURE[self.first_digit]

        # Mengisi pola bit untuk digit pertama berdasarkan struktur barcode
        for i in range(len(self.structure)):
            # Jika struktur pada indeks i adalah "L", tambahkan pola bit dari digit pertama ke first_bit_pattern
            if self.structure[i] == "L":
                self.first_bit_pattern += self.L_CODE[int(self.first_6_digits[i])]
            # Jika struktur pada indeks i adalah "G", tambahkan pola bit dari digit pertama ke first_bit_pattern
            if self.structure[i] == "G":
                self.first_bit_pattern += self.G_CODE[int(self.first_6_digits[i])]

        # Mengisi pola bit untuk digit kedua berdasarkan kode digit kedua
        for digit in self.second_6_digits:
            # Menambahkan pola bit dari digit kedua ke second_bit_pattern
            self.second_bit_pattern += self.R_CODE[int(digit)]

        # Pointer untuk menentukan posisi saat membuat barcode
        self.pointer = 0

        # Menampilkan digit pertama pada sebelah kiri guard bars
        self.create_text(
            self.start_x - (self.font_size / 2),
            self.start_y + self.guard_bars_height + self.font_size,
            text=self.code[0],
            fill="black",
            font=(f"Helvetica {self.font_size} bold"),
        )

        # Menampilkan guard bars pada awal barcode
        for bit in self.GUARD_BARS["start"]:
            # Jika bit adalah "1", buat garis dengan lebar dan warna yang ditentukan
            if bit == "1":
                self.create_line(
                    (self.start_x + (self.pointer * self.bar_width), self.start_y),
                    (
                        self.start_x + (self.pointer * self.bar_width),
                        self.start_y + self.guard_bars_height,
                    ),
                    width=self.bar_width,
                    fill="blue",
                )
            # Pindahkan pointer ke posisi berikutnya
            self.pointer += 1

        # Menampilkan pola bit untuk 6 digit pertama pada barcode
        for _, bit in enumerate(self.first_bit_pattern):
            # Jika bit adalah "1", buat garis dengan lebar dan warna yang ditentukan
            if bit == "1":
                self.create_line(
                    (self.start_x + (self.pointer * self.bar_width), self.start_y),
                    (
                        self.start_x + (self.pointer * self.bar_width),
                        self.start_y + self.bar_height,
                    ),
                    width=self.bar_width,
                    fill="black",
                )
            # Jika index pembagian 7 dari _ adalah 0, tampilkan digit pertama pada guard bars
            if _ % 7 == 0:
                self.create_text(
                    self.start_x
                    + (self.pointer * self.bar_width)
                    + (self.font_size / 2),
                    self.start_y + self.guard_bars_height + self.font_size,
                    text=self.code[(_ // 7) + 1],
                    fill="black",
                    font=(f"Helvetica {self.font_size} bold"),
                )
            # Pindahkan pointer ke posisi berikutnya
            self.pointer += 1

        # Menampilkan guard bars di tengah barcode
        for bit in self.GUARD_BARS["middle"]:
            # Jika bit adalah "1", buat garis dengan lebar dan warna yang ditentukan
            if bit == "1":
                self.create_line(
                    (self.start_x + (self.pointer * self.bar_width), self.start_y),
                    (
                        self.start_x + (self.pointer * self.bar_width),
                        self.start_y + self.guard_bars_height,
                    ),
                    width=self.bar_width,
                    fill="blue",
                )
            # Pindahkan pointer ke posisi berikutnya
            self.pointer += 1

        # Menampilkan pola bit untuk 6 digit kedua pada barcode
        for _, bit in enumerate(self.second_bit_pattern):
            # Jika bit adalah "1", buat garis dengan lebar dan warna yang ditentukan
            if bit == "1":
                self.create_line(
                    (self.start_x + (self.pointer * self.bar_width), self.start_y),
                    (
                        self.start_x + (self.pointer * self.bar_width),
                        self.start_y + self.bar_height,
                    ),
                    width=self.bar_width,
                    fill="black",
                )
            # Jika index pembagian 7 dari _ adalah 0, tampilkan digit kedua pada guard bars
            if _ % 7 == 0:
                self.create_text(
                    self.start_x
                    + (self.pointer * self.bar_width)
                    + (self.font_size / 2),
                    self.start_y + self.guard_bars_height + self.font_size,
                    text=self.code[7 + (_ // 7)],
                    fill="black",
                    font=(f"Helvetica {self.font_size} bold"),
                )
            # Pindahkan pointer ke posisi berikutnya
            self.pointer += 1

        # Menampilkan guard bars di akhir barcode
        for bit in self.GUARD_BARS["end"]:
            # Jika bit adalah "1", buat garis dengan lebar dan warna yang ditentukan
            if bit == "1":
                self.create_line(
                    (self.start_x + (self.pointer * self.bar_width), self.start_y),
                    (
                        self.start_x + (self.pointer * self.bar_width),
                        self.start_y + self.guard_bars_height,
                    ),
                    width=self.bar_width,
                    fill="blue",
                )
            # Pindahkan pointer ke posisi berikutnya
            self.pointer += 1


# Membuat class BarcodeApp
class BarcodeApp:
    def __init__(self, master=None):
        self.master = master
        self.setup_ui()

    def setup_ui(self):
        # Mengatur tampilan awal aplikasi
        self.master.title("EAN-13")
        self.master.resizable(0, 0)

        # Menampilkan label untuk memasukkan nama file
        self.label_file = tk.Label(
            self.master,
            text="Save barcode to PS file [eg: EAN13.eps]:",
            font=("Helvetica 10 bold"),
        )
        self.label_file.pack()

        # Membuat entry untuk memasukkan nama file
        self.input_file = self.create_entry(self.save)

        self.code = ""

        # Menampilkan label untuk memasukkan kode
        self.label_code = tk.Label(
            self.master,
            text="Enter code (first 12 decimal digits):",
            font=("Helvetica 10 bold"),
        )
        self.label_code.pack()

        # Membuat entry untuk memasukkan kode
        self.input_code = self.create_entry(self.validate)

        # Membuat objek BarcodeCanvas
        self.barcode_canvas = BarcodeCanvas(
            self.master, bg="white", width=300, height=300
        )
        self.barcode_canvas.pack()

        # Membuat tombol untuk menampilkan informasi
        self.info_button = tk.Button(
            self.master,
            text="Show Info",
            font=("Helvetica 10 bold"),
            command=self.show_info,
        )
        self.info_button.pack()

    # Method untuk membuat entry
    def create_entry(self, command):
        entry = tk.Entry(self.master)
        entry.focus_force()
        entry.bind("<Return>", command)
        entry.pack()
        return entry

    # Method untuk validasi kode yang dimasukkan
    def validate(self, event):
        # Mendapatkan kode dari objek input_code
        self.code = self.input_code.get()

        # Memeriksa apakah panjang kode adalah 12 digit dan semuanya adalah digit
        if len(self.code) == 12 and self.code.isdigit():
            # Menghitung digit cek
            checkdigit = self.checkdigit(self.code)

            # Menghasilkan barcode menggunakan kode dan digit cek yang valid
            self.barcode_canvas.generate(self.code, checkdigit)
        else:
            # Menampilkan pesan kesalahan jika kode tidak memenuhi syarat
            messagebox.showerror("Wrong input", "Please enter a correct input code.")

    # Method untuk menghitung checkdigit dari kode
    def checkdigit(self, code):
        # Menghitung checksum dengan menjumlahkan setiap digit dikalikan dengan bobot yang sesuai
        checksum = sum(int(digit) * weight for digit, weight in zip(code, [1, 3] * 6))

        # Mengembalikan checkdigit yang dihasilkan
        return (10 - checksum % 10) % 10

    # Method untuk menampilkan informasi produk
    def show_info(self):
        try:
            # Mengambil data produk dari API berdasarkan kode dan checkdigit
            data = requests.get(
                f"https://api.upcitemdb.com/prod/trial/lookup",
                params={"upc": self.code + str(self.checkdigit(self.code))},
            ).json()
        except requests.exceptions.ConnectionError:
            # Menangani error koneksi dengan menampilkan pesan kesalahan
            messagebox.showerror(
                "Connection error",
                "An error connecting to the API occurred. Please check your connection.",
            )
            return

        # Memeriksa status response dari API
        if data["code"] == "OK":
            # Mengambil data produk dari response API dan menyimpannya di variabel data
            data = data["items"]
        elif data["code"] == "TOO_FAST":
            # Menangani kesalahan jika terlalu banyak permintaan dalam waktu singkat
            messagebox.showerror(
                "Connection error", "Requests are too fast. Please try again later."
            )
            return
        elif data["code"] == "EXCEED_LIMIT":
            # Menangani kesalahan jika jumlah permintaan telah melebihi batas yang ditetapkan
            messagebox.showerror(
                "Connection error", "API rate limit exceeded. Please try again later."
            )
            return

        # Menampilkan informasi produk jika data ditemukan, jika tidak tampilkan pesan kesalahan
        if data:
            if self.code:
                messagebox.showinfo("Product Information", data[0]["title"])
            else:
                messagebox.showerror(
                    "Wrong input", "Please enter a correct input code."
                )
        else:
            messagebox.showerror(
                "Not found", f"{self.code} is not associated with any product."
            )

    # Method untuk menyimpan barcode sebagai file PS
    def save(self, event):
        # Melakukan validasi sebelum menyimpan
        self.validate(event)

        # Mendapatkan nama file dari objek input_file
        file_name = self.input_file.get()

        # Memeriksa apakah nama file berakhir dengan ekstensi ".eps"
        if file_name.endswith(".eps"):
            # Menyimpan barcode sebagai file PS dengan menggunakan modul postscript
            self.barcode_canvas.postscript(file=file_name, colormode="color")

            # Menampilkan pesan sukses jika penyimpanan berhasil
            messagebox.showinfo("File saved", f"{file_name} saved successfully.")
        else:
            # Menampilkan pesan kesalahan jika nama file tidak sesuai
            messagebox.showerror("Wrong input", "Please enter a correct file name.")


# Fungsi utama untuk menjalankan aplikasi barcode
def main():
    # Membuat objek Tk
    root = tk.Tk()

    # Membuat objek BarcodeApp dengan menggunakan root window
    app = BarcodeApp(master=root)

    # Menjalankan event loop
    root.mainloop()


# Menjalankan fungsi main jika file dijalankan langsung (bukan diimport sebagai modul)
if __name__ == "__main__":
    main()
