# LAB 10 | Dasar-Dasar Pemrograman 1
# Nama: Muhammad Fazil Tirtana
# Jurusan: Ilmu Komputer
# Kode Asdos: MON
# kelas: D
# NPM: 2306274983


# Import modules yang diperlukan dari tkinter
import tkinter as tk
from tkinter import messagebox

# Buat class PacilokaApp
class PacilokaApp:
    def __init__(self, master=None):
        # Inisialisasi window
        self.master = master

        # Inisalisasi dictionary yang berisi informasi hotel
        self.dict_hotel = {
            "Marriott Yogyakarta": [18, 3400000, "MRIOT", 5],
            "Four Seasons Jakarta": [34, 5300000, "FRSNS", 4],
            "Grand Hyatt Jakarta": [57, 4700000, "HYATT", 5],
            "Raffles Jakarta": [95, 3200000, "RFFLS", 4],
            "Grand Tjokro Bandung": [9, 3100000, "TJKRO", 3],
            "Favehotel Braga": [16, 3500000, "FVHTL", 4],
            "Aryaduta Bandung": [11, 4200000, "ARYDT", 5],
            "Jambuluwuk Malioboro": [19, 7500000, "JMLWK", 3],
            "The Ritz-Carlton Jakarta": [23, 5800000, "CRLTN", 4],
            "Intercontinental Jakarta": [31, 3000000, "INTRC", 5],
            "The Apurva Kempinski Bali": [27, 6400000, "APRVA", 5],
            "Shangri La Jakarta": [52, 3500000, "SHNGR", 3],
        }

        # Atur judul dan geometri window
        master.title("Paciloka App")
        master.geometry("800x700")

        # Buat frame utama
        self.frame = tk.Frame(self.master, bg="#0E0D11", height=600, width=600)
        self.frame.pack_propagate(0)
        self.frame.pack(fill="both", expand="true")
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        # Inisialisasi aplikasi dengan menampilkan homepage
        self.homepage()

    # Method untuk menampilkan homepage
    def homepage(self):
        # Buat frame untuk menampilkan informasi hotel
        info_frame = tk.Frame(self.frame, bg="#282942")
        info_frame.pack(pady=20)

        # Buat label untuk menampilkan informasi hotel
        self.dict_hotel_label = {}

        for i in range(len(self.dict_hotel.keys())):
            key = list(self.dict_hotel.keys())[i]

            hotel_info = ""
            hotel_info += f"Nama Hotel: {key}\n"
            hotel_info += f"Jumlah Kamar Tersedia: {self.dict_hotel[key][0]}\n"
            hotel_info += f"Harga per Kamar: Rp.{self.dict_hotel[key][1]:,}\n"
            hotel_info += f"Rating: {'⭐' * int(self.dict_hotel[key][3])}\n"

            # Buat label untuk setiap informasi hotel
            self.dict_hotel_label[key] = tk.Label(
                info_frame,
                text=hotel_info,
                justify="left",
                font=("calibre", 10),
                bg="#282942",
                fg="#FFFFFF",
                padx=15,
                pady=10,
            )
            self.dict_hotel_label[key].grid(row=i // 3, column=i % 3, sticky="w")

        # Buat frame untuk input pengguna
        input_frame = tk.Frame(self.frame, bg="#0E0D11")
        input_frame.pack(pady=10)

        # Buat label dan widget entry untuk input pengguna
        self.label_nama_pengguna = tk.Label(
            input_frame,
            text="Nama Pengguna:",
            justify="left",
            font=("calibre", 10),
            bg="#0E0D11",
            fg="#FFFFFF",
            padx=10,
            pady=5,
        )
        self.label_nama_pengguna.grid(row=0, column=0, sticky="w")

        self.nama_pengguna = tk.StringVar()
        self.input_nama_pengguna = tk.Entry(
            input_frame,
            textvariable=self.nama_pengguna,
            width=20,
            font=("calibre", 10),
            bg="#1D1B22",
            fg="#FFFFFF",
        )
        self.input_nama_pengguna.grid(row=0, column=1)
        self.input_nama_pengguna.focus_force()

        self.label_nama_hotel = tk.Label(
            input_frame,
            text="Nama Hotel:",
            justify="left",
            font=("calibre", 10),
            bg="#0E0D11",
            fg="#FFFFFF",
            padx=10,
            pady=5,
        )
        self.label_nama_hotel.grid(row=1, column=0, sticky="w")

        self.nama_hotel = tk.StringVar()
        self.input_nama_hotel = tk.Entry(
            input_frame,
            textvariable=self.nama_hotel,
            width=20,
            font=("calibre", 10),
            bg="#1D1B22",
            fg="#FFFFFF",
        )
        self.input_nama_hotel.grid(row=1, column=1)

        self.label_jumlah_kamar = tk.Label(
            input_frame,
            text="Jumlah Kamar:",
            justify="left",
            font=("calibre", 10),
            bg="#0E0D11",
            fg="#FFFFFF",
            padx=10,
            pady=5,
        )
        self.label_jumlah_kamar.grid(row=2, column=0, sticky="w")

        self.jumlah_kamar = tk.StringVar()
        self.input_jumlah_kamar = tk.Entry(
            input_frame,
            textvariable=self.jumlah_kamar,
            width=20,
            font=("calibre", 10),
            bg="#1D1B22",
            fg="#FFFFFF",
        )
        self.input_jumlah_kamar.grid(row=2, column=1)

        # Buat frame untuk button
        button_frame = tk.Frame(self.frame, bg="#0E0D11")
        button_frame.pack(pady=20)

        # Buat button untuk memesan dan keluar
        self.button_pesan_kamar = tk.Button(
            button_frame,
            text="Pesan Kamar",
            command=self.booking,
            font=("calibre", 10, "bold"),
            bg="#7359F8",
            fg="white",
            padx=10,
            pady=5,
        )
        self.button_pesan_kamar.grid(row=0, column=0, padx=10)

        self.button_exit = tk.Button(
            button_frame,
            text="Exit",
            command=self.master.destroy,
            font=("calibre", 10, "bold"),
            bg="#E0554A",
            fg="white",
            padx=10,
            pady=5,
        )
        self.button_exit.grid(row=0, column=1, padx=10)

    # Method untuk memroses pemesanan
    def booking(self):
        # Periksa apakah ada input field yang kosong
        if self.nama_pengguna.get() or self.nama_hotel.get() or self.jumlah_kamar.get():
            # Periksa apakah hotel yang dipilih ada di dalam dictionary
            if self.nama_hotel.get() in self.dict_hotel.keys():
                # Periksa apakah input jumlah kamar adalah integer
                try:
                    int(self.jumlah_kamar.get())
                except ValueError:
                    # Tampilkan peringatan jika jumlah kamar bukan integer
                    messagebox.showwarning(
                        "Jumlah kamar harus bilangan bulat",
                        f"Jumlah kamar harus bilangan bulat.",
                    )
                    return

                # Periksa apakah jumlah kamar yang dimasukkan valid
                if int(self.jumlah_kamar.get()) > 0:
                    # Periksa apakah jumlah kamar yang diminta tersedia
                    if (
                        int(self.jumlah_kamar.get())
                        <= self.dict_hotel[self.nama_hotel.get()][0]
                    ):
                        # Perbarui jumlah kamar yang ada di dalam dictionary
                        self.dict_hotel[self.nama_hotel.get()][0] -= int(
                            self.jumlah_kamar.get()
                        )

                        # Perbarui informasi hotel yang ditampilkan
                        hotel_info = ""
                        hotel_info += f"Nama Hotel: {self.nama_hotel.get()}\n"
                        hotel_info += f"Jumlah Kamar Tersedia: {self.dict_hotel[self.nama_hotel.get()][0]}\n"
                        hotel_info += f"Harga per Kamar: Rp.{self.dict_hotel[self.nama_hotel.get()][1]:,}\n"
                        hotel_info += f"Rating: {'⭐' * int(self.dict_hotel[self.nama_hotel.get()][3])}\n"

                        self.dict_hotel_label[self.nama_hotel.get()].config(
                            text=hotel_info
                        )

                        # Hitung total biaya dan buat nomor tiket
                        total_biaya = (
                            int(self.jumlah_kamar.get())
                            * self.dict_hotel[self.nama_hotel.get()][1]
                        )
                        nomor_tiket = f"{self.dict_hotel[self.nama_hotel.get()][2]}/{self.jumlah_kamar.get()}/{self.nama_pengguna.get()[:3]}"

                        # Tampilkan pesan berhasil memesan
                        messagebox.showinfo(
                            "Booking Berhasil!",
                            f"Booking Berhasil!\nPesanan untuk {self.nama_pengguna.get()} di hotel {self.nama_hotel.get()} sebanyak {self.jumlah_kamar.get()} kamar!\nTotal Biaya: Rp.{total_biaya:,}\nNomor Tiket: {nomor_tiket}",
                        )

                        # Hapus kolom input
                        self.input_nama_pengguna.delete(0, "end")
                        self.input_nama_hotel.delete(0, "end")
                        self.input_jumlah_kamar.delete(0, "end")
                    else:
                        # Tampilkan peringatan jika kamar yang diminta tidak tersedia
                        messagebox.showwarning(
                            "Tidak Bisa Memesan Kamar",
                            f"Maaf, tidak bisa memesan kamar sebanyak {self.jumlah_kamar.get()} di hotel {self.nama_hotel.get()}.",
                        )
                else:
                    # Tampilkan peringatan jika kamar yang diminta tidak tersedia
                    messagebox.showwarning(
                        "Tidak Bisa Memesan Kamar",
                        f"Maaf, kamar yang dipesan harus lebih dari 0.",
                    )
            else:
                # Tampilkan peringatan jika hotel yang dipilih tidak tersedia
                messagebox.showwarning(
                    "Hotel Tidak Tersedia",
                    f"Maaf, {self.nama_hotel.get()} tidak tersedia di sistem.",
                )
        else:
            # Tampilkan peringatan jika ada salah satu input yang kosong
            messagebox.showwarning(
                "Warning",
                f"Mohon isi semua input.",
            )


# Blok utama untuk menjalankan aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = PacilokaApp(master=root)
    root.mainloop()
