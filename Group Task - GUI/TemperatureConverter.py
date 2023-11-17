from tkinter import *

# Buat sebuah class untuk TemperatureConverter
class TemperatureConverter:
    def __init__(self, master):
        # Inisialisasi TemperatureConverter dengan window master
        self.master = master
        master.title("Temperature Converter")  # Tetapkan judul window
        master.geometry("300x50")  # Tetapkan ukuran window

        # Variabel untuk menyimpan suhu Fahrenheit
        self.fahrenheit = IntVar()
        self.celsius = 0  # Variabel untuk menyimpan suhu Celsius

        # Buat label untuk menampilkan hasil konversi
        self.label = Label(master, text="")
        self.label.grid(row=1, column=1, padx=0, pady=5)

        # Field input untuk memasukkan suhu Fahrenheit
        self.temperature_field = Entry(master, textvariable=self.fahrenheit, width=10)
        self.temperature_field.grid(row=1, column=2, padx=0, pady=5)

        # Label untuk menampilkan '°F' di sebelah field suhu
        self.fahrenheit_label = Label(master, text="°F")
        self.fahrenheit_label.grid(row=1, column=3, padx=0, pady=5)

        # Tombol untuk melakukan konversi
        self.submit_button = Button(master, text="→", command=self.convert)
        self.submit_button.grid(row=1, column=4, padx=10, pady=5)

        # Label untuk menampilkan suhu yang dikonversi dalam Celsius
        self.result_label = Label(master, text="-17.78°C")
        self.result_label.grid(row=1, column=5, padx=0, pady=5)

    # Method untuk mengonversi Fahrenheit ke Celsius dan memperbarui label hasil
    def convert(self):
        self.celsius = (self.fahrenheit.get() - 32) * 5 / 9
        self.result_label.config(text=f"{round(self.celsius, 2)}°C")


# Membuat window
root = Tk()

# Buat sebuah instance dari class TemperatureConverter 
window = TemperatureConverter(root)

# Jalankan Tkinter
root.mainloop()
