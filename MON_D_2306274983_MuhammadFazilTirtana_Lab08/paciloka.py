class Hotel:
    def __init__(self, name, available_room, room_price):
        """
        Inisialisasi objek Hotel.

        Parameters:
        - name (str): Nama hotel.
        - available_room (int): Jumlah kamar yang tersedia di hotel.
        - room_price (int): Harga satu kamar di hotel.
        """
        self.name = name
        self.available_room = available_room
        self.room_price = room_price
        self.profit = 0
        self.guests = []

    def booking(self, user, jumlah_kamar):
        """
        Metode untuk melakukan pemesanan kamar di hotel.

        Parameters:
        - user (str): Nama pengguna yang melakukan pemesanan.
        - jumlah_kamar (int): Jumlah kamar yang akan dipesan.
        """
        self.available_room = self.available_room - jumlah_kamar
        self.guests.append(user)
        self.profit = self.profit + (self.room_price * jumlah_kamar)

    def __str__(self):
        """
        Representasi string dari objek Hotel, mengembalikan nama hotel.
        """
        return self.name


class User:
    def __init__(self, name, money):
        """
        Inisialisasi objek User.

        Parameters:
        - name (str): Nama pengguna.
        - money (int): Saldo pengguna.
        """
        self.name = name
        self.money = money
        self.hotel_list = []

    def topup(self, jumlah_topup):
        """
        Metode untuk menambahkan saldo ke akun pengguna.

        Parameters:
        - jumlah_topup (int): Jumlah uang yang akan ditambahkan ke saldo pengguna.
        """
        self.money = self.money + jumlah_topup

    def __str__(self):
        """
        Representasi string dari objek User, mengembalikan nama pengguna.
        """
        return self.name


def print_header():
    """
    Fungsi untuk mencetak header aplikasi.
    """
    print("\n=============Welcome to Paciloka!=============\n")


def get_initial_inputs(hotel_data={}, user_data={}):
    """
    Fungsi untuk mendapatkan input awal berupa jumlah hotel dan pengguna.

    Parameters:
    - hotel_data (dict): Dictionary untuk menyimpan data hotel.
    - user_data (dict): Dictionary untuk menyimpan data pengguna.

    Returns:
    Tuple dari hotel_data dan user_data setelah mendapatkan input.
    """
    # Mengambil input jumlah hotel dan pengguna dari pengguna
    num_hotel = int(input("Masukan banyak hotel : "))
    num_user = int(input("Masukan banyak user : "))

    # Loop untuk mengambil input data hotel
    for i in range(1, num_hotel + 1):
        name = input(f"\nMasukan nama hotel ke-{i} : ")
        available_room = int(input(f"Masukan banyak kamar hotel ke-{i} : "))
        room_price = int(input(f"Masukan harga satu kamar hotel ke-{i} : "))
        # Membuat objek Hotel dan menyimpannya dalam dictionary hotel_data
        hotel_data[name] = Hotel(
            name=name, available_room=available_room, room_price=room_price
        )

    # Loop untuk mengambil input data pengguna
    for i in range(1, num_user + 1):
        name = input(f"\nMasukan nama user ke-{i} : ")
        money = int(input(f"Masukan saldo user ke-{i} : "))
        # Membuat objek User dan menyimpannya dalam dictionary user_data
        user_data[name] = User(name=name, money=money)

    # Mengembalikan dictionary hotel_data dan user_data setelah mendapatkan input
    return hotel_data, user_data


def print_data(hotel_data, user_data):
    """
    Fungsi untuk mencetak daftar hotel dan pengguna.

    Parameters:
    - hotel_data (dict): Dictionary data hotel.
    - user_data (dict): Dictionary data pengguna.
    """
    # Menampilkan daftar hotel
    print("Daftar Hotel")
    for index, key in enumerate(hotel_data):
        print(f"{index+1}. {key}")

    # Menampilkan daftar pengguna
    print("\nDaftar User")
    for index, key in enumerate(user_data):
        print(f"{index+1}. {key}")


def print_profit(hotel_data):
    """
    Fungsi untuk mencetak profit dari suatu hotel.

    Parameters:
    - hotel_data (dict): Dictionary data hotel.
    """
    # Meminta input dari pengguna untuk nama hotel
    hotel_name = input("Masukkan nama hotel : ")

    # Memeriksa apakah nama hotel ada dalam data hotel
    if hotel_name in hotel_data.keys():
        # Menampilkan informasi profit hotel jika nama hotel ditemukan
        print(
            f"Hotel dengan nama {hotel_name} mempunyai profit sebesar {hotel_data[hotel_name].profit}"
        )
    else:
        # Menampilkan pesan jika nama hotel tidak ditemukan di sistem
        print("Nama hotel tidak ditemukan di sistem!")


def print_money(user_data):
    """
    Fungsi untuk mencetak saldo dari suatu pengguna.

    Parameters:
    - user_data (dict): Dictionary data pengguna.
    """
    # Meminta input dari pengguna untuk nama pengguna
    user_name = input("Masukkan nama user : ")

    # Memeriksa apakah nama pengguna ada dalam data pengguna
    if user_name in user_data.keys():
        # Menampilkan informasi saldo pengguna jika nama pengguna ditemukan
        print(
            f"User dengan nama {user_name} mempunyai saldo sebesar {user_data[user_name].money}"
        )
    else:
        # Menampilkan pesan jika nama pengguna tidak ditemukan di sistem
        print("Nama user tidak ditemukan di sistem!")


def topup(user_data):
    """
    Fungsi untuk menambahkan saldo ke akun pengguna.

    Parameters:
    - user_data (dict): Dictionary data pengguna.
    """
    # Meminta input dari pengguna untuk nama pengguna
    user_name = input("Masukkan nama user : ")

    # Memeriksa apakah nama pengguna ada dalam data pengguna
    if user_name in user_data.keys():
        # Meminta input dari pengguna untuk jumlah uang yang akan ditambahkan ke saldo pengguna
        amount = input("Masukkan jumlah uang yang akan ditambahkan ke user : ")

        try:
            # Mengonversi input jumlah uang menjadi integer
            amount = int(amount)

            # Pengecekan apakah jumlah uang yang akan ditambahkan lebih dari 0
            if amount > 0:
                # Menambahkan jumlah uang ke saldo pengguna dan memperbarui data pengguna
                user_data[user_name].topup(jumlah_topup=amount)
                print(
                    f"Berhasil menambahkan {amount} ke user {user_name}. Saldo user menjadi {user_data[user_name].money}"
                )
            else:
                # Menampilkan pesan jika jumlah uang yang akan ditambahkan kurang dari atau sama dengan 0
                print("Jumlah saldo yang akan ditambahkan ke user harus lebih dari 0!")
        except ValueError:
            # Menampilkan pesan jika input jumlah uang bukan merupakan angka integer
            print("Jumlah saldo yang akan ditambahkan ke user harus berupa integer!")
    else:
        # Menampilkan pesan jika nama pengguna tidak ditemukan di sistem
        print("Nama user tidak ditemukan di sistem!")


def booking(hotel_data, user_data):
    """
    Fungsi untuk melakukan pemesanan kamar hotel oleh pengguna.

    Parameters:
    - hotel_data (dict): Dictionary data hotel.
    - user_data (dict): Dictionary data pengguna.
    """
    # Meminta input dari pengguna untuk nama pengguna
    user_name = input("Masukkan nama user : ")

    # Memeriksa apakah nama pengguna ada dalam data pengguna
    if user_name in user_data.keys():
        # Meminta input dari pengguna untuk nama hotel
        hotel_name = input("Masukkan nama hotel : ")

        # Memeriksa apakah nama hotel ada dalam data hotel
        if hotel_name in hotel_data.keys():
            # Meminta input dari pengguna untuk jumlah kamar yang akan dibooking
            amount = input("Masukkan jumlah kamar yang akan dibooking : ")

            try:
                # Mengonversi input jumlah kamar menjadi integer
                amount = int(amount)

                # Pengecekan apakah jumlah kamar yang akan dibooking lebih dari 0
                if amount > 0:
                    # Pengecekan apakah pengguna memiliki saldo cukup dan kamar tersedia di hotel
                    if (
                        user_data[user_name].money - hotel_data[hotel_name].room_price
                        >= 0
                        and hotel_data[hotel_name].available_room - amount >= 0
                    ):
                        # Melakukan pemesanan kamar dan memperbarui data pengguna dan hotel
                        hotel_data[hotel_name].booking(
                            user=user_name, jumlah_kamar=amount
                        )
                        user_data[user_name].hotel_list.append(hotel_name)
                        user_data[user_name].money -= hotel_data[hotel_name].room_price
                        print(
                            f"User dengan nama {user_name} berhasil melakukan booking di hotel {hotel_name} dengan jumlah {amount} kamar!"
                        )
                    else:
                        # Menampilkan pesan jika pemesanan tidak berhasil
                        print("Booking tidak berhasil!")
                else:
                    # Menampilkan pesan jika jumlah kamar yang akan dibooking kurang dari atau sama dengan 0
                    print("Jumlah kamar yang akan dibooking harus lebih dari 0!")
            except ValueError:
                # Menampilkan pesan jika input jumlah kamar bukan merupakan angka integer
                print("Jumlah kamar yang akan dibooking harus berupa integer!")
        else:
            # Menampilkan pesan jika nama hotel tidak ditemukan di sistem
            print("Nama hotel tidak ditemukan di sistem!")
    else:
        # Menampilkan pesan jika nama pengguna tidak ditemukan di sistem
        print("Nama user tidak ditemukan di sistem!")


def print_users(hotel_data):
    """
    Fungsi untuk mencetak daftar tamu di suatu hotel.

    Parameters:
    - hotel_data (dict): Dictionary data hotel.
    """
    # Meminta input dari pengguna untuk nama hotel
    hotel_name = input("Masukkan nama hotel : ")

    # Memeriksa apakah nama hotel ada dalam data hotel
    if hotel_name in hotel_data.keys():
        # Memeriksa apakah hotel memiliki pelanggan (tamunya)
        if len(hotel_data[hotel_name].guests) > 0:
            # Menampilkan daftar tamu yang telah melakukan pemesanan di hotel
            print(
                f"""{hotel_name} | {str(hotel_data[hotel_name].guests)[1:-1].replace("'", "")}"""
            )
        else:
            # Menampilkan pesan jika hotel tidak memiliki pelanggan
            print(f"Hotel {hotel_name} tidak memiliki pelanggan!")
    else:
        # Menampilkan pesan jika nama hotel tidak ditemukan di sistem
        print("Nama hotel tidak ditemukan di sistem!")


def print_hotels(user_data):
    """
    Fungsi untuk mencetak daftar hotel yang pernah dipesan oleh suatu pengguna.

    Parameters:
    - user_data (dict): Dictionary data pengguna.
    """
    # Meminta input dari pengguna untuk nama pengguna
    user_name = input("Masukkan nama user : ")

    # Memeriksa apakah nama pengguna ada dalam data pengguna
    if user_name in user_data.keys():
        # Memeriksa apakah pengguna pernah melakukan booking di hotel
        if len(user_data[user_name].hotel_list) > 0:
            # Menampilkan daftar hotel yang pernah dipesan oleh pengguna
            print(
                f"""{user_name} | {str(user_data[user_name].hotel_list)[1:-1].replace("'", "")}"""
            )
        else:
            # Menampilkan pesan jika pengguna tidak pernah melakukan booking
            print(f"User {user_name} tidak pernah melakukan booking!")
    else:
        # Menampilkan pesan jika nama pengguna tidak ditemukan di sistem
        print("Nama user tidak ditemukan di sistem!")


# Memastikan bahwa script ini dijalankan sebagai program utama
if __name__ == "__main__":
    # Mendapatkan input awal berupa data hotel dan pengguna
    hotel_data, user_data = get_initial_inputs()

    # Loop utama program
    while True:
        # Menampilkan header aplikasi
        print_header()

        # Meminta input untuk perintah dari pengguna
        option = input("Masukkan perintah : ")

        # Menggunakan percabangan untuk memproses perintah yang dimasukkan pengguna
        if option == "1":
            # Menampilkan daftar hotel dan pengguna
            print_data(hotel_data, user_data)
        elif option == "2":
            # Menampilkan profit suatu hotel
            print_profit(hotel_data)
        elif option == "3":
            # Menampilkan saldo suatu pengguna
            print_money(user_data)
        elif option == "4":
            # Menambahkan saldo ke akun pengguna
            topup(user_data)
        elif option == "5":
            # Melakukan pemesanan kamar hotel oleh pengguna
            booking(hotel_data, user_data)
        elif option == "6":
            # Menampilkan daftar tamu di suatu hotel
            print_users(hotel_data)
        elif option == "7":
            # Menampilkan daftar hotel yang pernah dipesan oleh suatu pengguna
            print_hotels(user_data)
        elif option == "8":
            # Jika pilihan adalah "8", keluar dari loop dan tampilkan pesan terima kasih
            print("Terima kasih sudah mengunjungi Paciloka!")
            break
        else:
            # Menampilkan pesan kesalahan jika perintah tidak valid
            print("Perintah tidak diketahui! Masukkan perintah yang valid")
