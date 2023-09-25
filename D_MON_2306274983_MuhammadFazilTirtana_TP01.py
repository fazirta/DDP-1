# TP 1 | Dasar-Dasar Pemrograman 1
# Nama: Muhammad Fazil Tirtana
# Jurusan: Ilmu Komputer
# Kode Asdos: MON
# Kelas: D
# NPM: 2306274983

from turtle import *
import tkinter

title("Mini Super Mario Towers")
speed(0)
hideturtle()

# Meminta input dari user untuk variable jumlah tower
jumlah_tower = None
while jumlah_tower is None:
    jumlah_tower = textinput("Tower to Build", "Enter the number of towers you want to build (integer):")
    # Periksa apakah input adalah bilangan bulat dan memenuhi spesifikasi
    if jumlah_tower == "" or "." in str(jumlah_tower):
        tkinter.messagebox.showwarning("Invalid Input", "Please enter an integer between 1 and 10.")
        # Membuat jumlah_tower menjadi None agar loop berlanjut
        jumlah_tower = None
    elif int(jumlah_tower) < 1:
        tkinter.messagebox.showwarning("Too Small", "The allowed minimum value is 1. Please try again.")
        jumlah_tower = None
    else:
        # Konversi input menjadi bilangan bulat
        jumlah_tower = int(jumlah_tower)

# Jika ada lebih dari satu tower, Meminta input variable jarak dan beda layer
if jumlah_tower > 1:
    jarak = None
    while jarak is None:
        jarak = textinput("Distance between Towers", "Enter the distance between towers (integer):")
        # Periksa apakah input adalah bilangan bulat dan memenuhi spesifikasi
        if jarak == "" or "." in str(jarak):
            tkinter.messagebox.showwarning("Invalid Input", "Please enter an integer between 2 and 5.")
            # Membuat jarak menjadi None agar loop berlanjut
            jarak = None
        elif int(jarak) < 2:
            tkinter.messagebox.showwarning("Too Small", "The allowed minimum value is 2. Please try again.")
            jarak = None
        elif int(jarak) > 5:
            tkinter.messagebox.showwarning("Too Big", "The allowed maximum value is 5. Please try again.")
            jarak = None
        else:
            # Konversi input menjadi bilangan bulat
            jarak = int(jarak)

    beda_layer = None
    while beda_layer is None:
        beda_layer = textinput("Tower Layer Difference", "Enter the number of layer differences between each tower (integer):")
        # Periksa apakah input adalah bilangan bulat dan memenuhi spesifikasi
        if beda_layer == "" or "." in str(beda_layer):
            tkinter.messagebox.showwarning("Invalid Input", "Please enter an integer between 2 and 5.")
            # Membuat beda_layer menjadi None agar loop berlanjut
            beda_layer = None
        elif int(beda_layer) < 2:
            tkinter.messagebox.showwarning("Too Small", "The allowed minimum value is 2. Please try again.")
            beda_layer = None
        elif int(beda_layer) > 5:
            tkinter.messagebox.showwarning("Too Big", "The allowed maximum value is 5. Please try again.")
            beda_layer = None
        else:
            # Konversi input menjadi bilangan bulat
            beda_layer = int(beda_layer)
else:
    jarak, beda_layer = 0, 0

# Meminta input dari user untuk variable lebar bata
lebar_bata = None
while lebar_bata is None:
    lebar_bata = textinput("Brick Width", "Enter the width of a brick (integer):")
    # Periksa apakah input adalah bilangan bulat dan memenuhi spesifikasi
    if lebar_bata == "" or "." in str(lebar_bata):
        tkinter.messagebox.showwarning("Invalid Input", "Please enter an integer between 1 and 35.")
        # Membuat lebar_bata menjadi None agar loop berlanjut
        lebar_bata = None
    elif int(lebar_bata) < 1:
        tkinter.messagebox.showwarning("Too Small", "The allowed minimum value is 1. Please try again.")
        lebar_bata = None
    elif int(lebar_bata) > 35:
        tkinter.messagebox.showwarning("Too Big", "The allowed maximum value is 35. Please try again.")
        lebar_bata = None
    else:
        # Konversi input menjadi bilangan bulat
        lebar_bata = int(lebar_bata)

# Meminta input dari user untuk variable tinggi bata
tinggi_bata = None
while tinggi_bata is None:
    tinggi_bata = textinput("Brick Height", "Enter the height of a brick (integer):")
    # Periksa apakah input adalah bilangan bulat dan memenuhi spesifikasi
    if tinggi_bata == "" or "." in str(tinggi_bata):
        tkinter.messagebox.showwarning("Invalid Input", "Please enter an integer between 1 and 25.")
        # Membuat tinggi_bata menjadi None agar loop berlanjut
        tinggi_bata = None
    elif int(tinggi_bata) < 1:
        tkinter.messagebox.showwarning("Too Small", "The allowed minimum value is 1. Please try again.")
        tinggi_bata = None
    elif int(tinggi_bata) > 25:
        tkinter.messagebox.showwarning("Too Big", "The allowed maximum value is 25. Please try again.")
        tinggi_bata = None
    else:
        # Konversi input menjadi bilangan bulat
        tinggi_bata = int(tinggi_bata)

# Meminta input dari user untuk variable jumlah layer untuk tower pertama
jumlah_layer = None
while jumlah_layer is None:
    jumlah_layer = textinput("The Number of First Tower Layers", "Enter the number of layers for the first tower (integer):")
    # Periksa apakah input adalah bilangan bulat dan memenuhi spesifikasi
    if jumlah_layer == "" or "." in str(jumlah_layer):
        tkinter.messagebox.showwarning("Invalid Input", "Please enter an integer between 1 and 25.")
        # Membuat jumlah_layer menjadi None agar loop berlanjut
        jumlah_layer = None
    elif int(jumlah_layer) < 1:
        tkinter.messagebox.showwarning("Too Small", "The allowed minimum value is 1. Please try again.")
        jumlah_layer = None
    elif int(jumlah_layer) > 25:
        tkinter.messagebox.showwarning("Too Big", "The allowed maximum value is 25. Please try again.")
        jumlah_layer = None
    else:
        # Konversi input menjadi bilangan bulat
        jumlah_layer = int(jumlah_layer)

# Meminta input dari user untuk variable lebar layer
lebar_layer = None
while lebar_layer is None:
    lebar_layer = textinput("Layer Width", "Enter the width of the layer (integer):")
    # Periksa apakah input adalah bilangan bulat dan memenuhi spesifikasi
    if lebar_layer == "" or "." in str(lebar_layer):
        tkinter.messagebox.showwarning("Invalid Input", "Please enter an integer between 1 and 10.")
        # Membuat lebar_layer menjadi None agar loop berlanjut
        lebar_layer = None
    elif int(lebar_layer) < 1:
        tkinter.messagebox.showwarning("Too Small", "The allowed minimum value is 1. Please try again.")
        lebar_layer = None
    elif int(lebar_layer) > 10:
        tkinter.messagebox.showwarning("Too Big", "The allowed maximum value is 10. Please try again.")
        lebar_layer = None
    else:
        # Konversi input menjadi bilangan bulat
        lebar_layer = int(lebar_layer)

total_bata = 0
# Hitung lebar total dari semua tower berdasarkan jumlah tower, lebar layer, jarak, dan lebar bata
lebar_total_tower = ((int(jumlah_tower) * (int(lebar_layer) + 1)) + ((int(jumlah_tower) - 1) * (int(jarak) - 1))) * lebar_bata

# Gambar tower
for tower in range(int(jumlah_tower)):
    # Gambar badan tower
    for baris in range(int(jumlah_layer)):
        for _ in range(int(lebar_layer)):
            # Hitung koordinat x dan y dari bata berdasarkan tower, baris, lebar bata, tinggi bata, dan lebar total dari semua tower
            x = tower * ((lebar_layer + int(jarak)) * int(lebar_bata)) + _ * int(lebar_bata) - (int(lebar_total_tower) / 2)
            y = baris * int(tinggi_bata)
            penup()
            goto(x, y)
            pencolor("black")
            pendown()
            begin_fill()
            fillcolor("#CA7F65")
            # Gambar bentuk persegi panjang untuk bata dengan maju dan berputar ke kanan 4 kali
            for _ in range(2):
                forward(int(lebar_bata))
                right(90)
                forward(int(tinggi_bata))
                right(90)
            end_fill()
            total_bata = total_bata + 1

    # Gambar kepala tower
    for _ in range(int(lebar_layer) + 1):
        # Hitung koordinat x dan y dari bata berdasarkan tower, lebar layer, lebar bata, tinggi bata, dan lebar total dari semua tower
        x = tower * ((int(lebar_layer) + int(jarak)) * int(lebar_bata)) + _ * int(lebar_bata) - (int(lebar_bata) / 2) - (int(lebar_total_tower) / 2)
        y = (int(jumlah_layer) * int(tinggi_bata))
        penup()
        goto(x, y)
        pendown()
        begin_fill()
        fillcolor("#693424")
        # Gambar bentuk persegi panjang untuk bata dengan maju dan berputar ke kanan 4 kali
        for _ in range(2):
            forward(int(lebar_bata))
            right(90)
            forward(int(tinggi_bata))
            right(90)
        end_fill()
        total_bata = total_bata + 1

    # Gambar badan jamur
    # Hitung koordinat x dan y dari bata berdasarkan tower, lebar layer, lebar bata, tinggi bata, dan lebar total dari semua tower
    x = tower * ((int(lebar_layer) + int(jarak)) * int(lebar_bata)) - (int(lebar_bata) / 2) + (int(lebar_layer) * int(lebar_bata) / 2) - (int(lebar_bata) / 8) - (int(lebar_total_tower) / 2)
    y = (int(jumlah_layer) * int(tinggi_bata)) + int(lebar_bata) + 1
    penup()
    goto(x, y)
    pencolor("#fce6a0")
    pendown()
    begin_fill()
    fillcolor("#fce6a0")
    # Gambar bentuk persegi panjang sebagai badan jamur
    for _ in range(2):
        forward(int(lebar_bata) * 1.25)
        right(90)
        forward(int(lebar_bata))
        right(90)
    end_fill()

    # Gambar kepala jamur
    # Hitung koordinat x dan y dari bata berdasarkan tower, lebar layer, lebar bata, tinggi bata, dan lebar total dari semua tower
    x = tower * ((int(lebar_layer) + int(jarak)) * int(lebar_bata)) - int(lebar_bata) + (int(lebar_layer) * int(lebar_bata) / 2) - (int(lebar_total_tower) / 2)
    y = (int(jumlah_layer) * int(tinggi_bata)) + int(lebar_bata) + 1
    penup()
    goto(x, y)
    pencolor("#eb2b1b")
    pendown()
    begin_fill()
    fillcolor("#eb2b1b")
    left(90)
    # Gambar setengah lingkaran sebagai kepala jamur
    circle(-int(lebar_bata), 180)
    right(90)
    forward(int(lebar_bata) * 2)
    right(180)
    end_fill()

    # Gambar mata jamur kiri
    # Hitung koordinat x dan y dari bata berdasarkan tower, lebar layer, lebar bata, tinggi bata, dan lebar total dari semua tower
    x = tower * ((int(lebar_layer) + int(jarak)) * int(lebar_bata)) - (int(lebar_bata) / 2) + (int(lebar_layer) * int(lebar_bata) / 2) + (int(lebar_bata) / 8) - (int(lebar_total_tower) / 2)
    y = (int(jumlah_layer) * int(tinggi_bata)) + int(lebar_bata) - (int(lebar_bata) / 3)
    penup()
    goto(x, y)
    pencolor("white")
    pendown()
    begin_fill()
    fillcolor("white")
    left(90)
    # Gambar lingkaran putih sebagai mata jamur
    circle(-int(lebar_bata) / 8)
    end_fill()

    # Gambar mata jamur kanan
    # Hitung koordinat x dan y dari bata berdasarkan tower, lebar layer, lebar bata, tinggi bata, dan lebar total dari semua tower
    x = tower * ((lebar_layer + int(jarak)) * int(lebar_bata)) - (int(lebar_bata) / 2) + (int(lebar_layer) * int(lebar_bata) / 2) + (int(lebar_bata)) - (int(lebar_bata) / 8) - (int(lebar_total_tower) / 2)
    y = (int(jumlah_layer) * int(tinggi_bata)) + int(lebar_bata) - (int(lebar_bata) / 3)
    penup()
    goto(x, y)
    pencolor("white")
    pendown()
    begin_fill()
    fillcolor("white")
    # Gambar lingkaran putih sebagai mata jamur
    circle(int(lebar_bata) / 8)
    right(90)
    end_fill()

    # Tambah jumlah layer untuk tower berikutnya sebanyak variable beda layer
    jumlah_layer = jumlah_layer + beda_layer

# Tampilkan jumlah tower dan total bata yang digunakan
penup()
goto(0, -int(tinggi_bata) - 75)
pendown()
pencolor("black")
write(f"{int(jumlah_tower)} Super Mario Towers have been built with a total of {total_bata} bricks", font=("Arial", 12, "bold"), align="center")

# Keluar dari window turtle saat diclick
done()
