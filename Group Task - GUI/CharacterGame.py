import tkinter as tk


class CharacterGame:
    def __init__(self, master):
        # Inisialisasi objek CharacterGame
        self.master = master
        master.title("Character Game")
        master.geometry("500x500")

        # Inisialisasi posisi awal karakter
        self.x, self.y = 250, 250
        self.speed = 2

        # Membuat objek Canvas untuk menggambar karakter
        self.canvas = tk.Canvas(master, height=500, width=500)
        self.character = self.canvas.create_rectangle(
            self.x, self.y, self.x + 50, self.y + 50, fill="blue"
        )

        # Menghubungkan fungsi gerakan dengan tombol panah
        self.master.bind("<Left>", self.move_left)
        self.master.bind("<Right>", self.move_right)
        self.master.bind("<Up>", self.move_up)
        self.master.bind("<Down>", self.move_down)

        # Menampilkan canvas
        self.canvas.pack()

    def update_character(self):
        # Memperbarui posisi karakter di canvas
        self.canvas.coords(self.character, self.x, self.y, self.x + 50, self.y + 50)

    def move_left(self, event):
        # Menggerakkan karakter ke kiri
        self.x -= self.speed
        self.update_character()

    def move_right(self, event):
        # Menggerakkan karakter ke kanan
        self.x += self.speed
        self.update_character()

    def move_up(self, event):
        # Menggerakkan karakter ke atas
        self.y -= self.speed
        self.update_character()

    def move_down(self, event):
        # Menggerakkan karakter ke bawah
        self.y += self.speed
        self.update_character()


# Membuat instance dari Tkinter
root = tk.Tk()
# Membuat objek CharacterGame
window = CharacterGame(root)
# Menjalankan aplikasi Tkinter
root.mainloop()
