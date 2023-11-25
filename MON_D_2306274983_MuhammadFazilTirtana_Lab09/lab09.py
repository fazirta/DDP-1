# LAB 9 | Dasar-Dasar Pemrograman 1
# Nama: Muhammad Fazil Tirtana
# Jurusan: Ilmu Komputer
# Kode Asdos: MON
# kelas: D
# NPM: 2306274983


class Person:
    def __init__(self, name: str, payment: int, stamina: int) -> None:
        """
        Inisialisasi objek Person.

        Parameters:
        - name (str): nama dari person.
        - payment (int): jumlah bayaran untuk tiap pekerjaan yang dikerjakan.
        - stamina (int): nilai yang menentukan person mampu bekerja atau tidak.
        """
        # Inisialisasi atribut objek
        self.__name = name
        self.__payment = payment
        self.__stamina = stamina
        self.__total_work = 0

    # Method untuk mengatur nilai atribut stamina
    def set_stamina(self, value: int) -> None:
        self.__stamina = value

    # Method untuk mengatur nilai atribut total_work
    def set_total_work(self, value: int) -> None:
        self.__total_work = value

    # Method untuk mendapatkan nilai atribut name
    def get_name(self) -> str:
        return self.__name

    # Method untuk mendapatkan nilai atribut payment
    def get_payment(self) -> int:
        return self.__payment

    # Method untuk mendapatkan nilai atribut stamina
    def get_stamina(self) -> int:
        return self.__stamina

    # Method untuk mendapatkan nilai atribut total_work
    def get_total_work(self) -> int:
        return self.__total_work

    # Method untuk mengecek ketersediaan stamina untuk bekerja
    def is_available(self, cost_stamina: int) -> bool:
        return True if self.__stamina >= cost_stamina else False

    # Method untuk menghitung jumlah gaji yang harus dibayarkan
    def pay_day(self) -> int:
        return self.__payment * self.__total_work

    # Method untuk mengeksekusi pekerjaan
    def work(self, cost_stamina: int) -> None:
        # Mengurangkan stamina person sesuai dengan biaya stamina untuk pekerjaan
        self.__stamina -= cost_stamina

        # Menambahkan satu ke jumlah total pekerjaan yang telah dilakukan oleh person
        self.__total_work += 1

    # Method untuk mengekspresikan objek dalam bentuk string
    def __str__(self) -> str:
        # Mendapatkan nama class saat ini
        class_name = self.__class__.__name__

        # Mendapatkan nama
        name = self.get_name()

        # Mendapatkan jumlah total pekerjaan yang telah dilakukan oleh
        total_work = self.get_total_work()

        # Mendapatkan nilai stamina
        stamina = self.get_stamina()

        # Menghitung total gaji
        payment = self.pay_day()

        # Mengembalikan string yang berisi informasi tentang person
        return f"{class_name:20} | {name:20} | Total kerja: {total_work:20} | Stamina:{stamina:20} | Gaji:{payment:20}"


class Manager(Person):
    def __init__(self, name: str, payment: int, stamina: int) -> None:
        """
        Inisialisasi objek Manager yang merupakan subclass dari Person.

        Parameters:
        - name (str): nama dari manager.
        - payment (int): jumlah bayaran untuk tiap pekerjaan yang dikerjakan.
        - stamina (int): nilai yang menentukan manager mampu bekerja atau tidak.
        """
        # Memanggil konstruktor class (Person)
        super().__init__(name, payment, stamina)

        # Menambahkan atribut khusus untuk class Manager
        self.__list_worker = []

    # Method untuk mendapatkan daftar pegawai
    def get_list_worker(self) -> list:
        return self.__list_worker

    # Method untuk merekrut pegawai baru
    def hire_worker(self, name: str) -> None:
        # Mengurangkan stamina manajer setiap kali merekrut pegawai baru
        self.set_stamina(self.get_stamina() - 10)

        # Mengecek apakah nama pegawai sudah ada dalam daftar pegawai yang dimiliki oleh manajer
        if (
            name.title() not in [worker.get_name() for worker in self.__list_worker]
            and name.title() != self.get_name()
        ):
            # Menambahkan objek Worker baru ke dalam daftar pegawai manajer
            self.__list_worker.append(
                Worker(name=name.title(), payment=5000, stamina=100)
            )

            # Menambahkan satu ke jumlah total pekerjaan yang telah dilakukan oleh manager
            self.set_total_work(self.get_total_work() + 1)

            # Menampilkan pesan berhasil merekrut pegawai baru
            print("Berhasil mendapat pegawai baru")
        else:
            # Menampilkan pesan bahwa pegawai dengan nama yang sama sudah ada
            print("Sudah ada!")

    # Method untuk memecat pegawai
    def fire_worker(self, name: str) -> None:
        # Mengurangkan stamina manajer setiap kali memecat pegawai
        self.set_stamina(self.get_stamina() - 10)

        # Iterasi melalui setiap pegawai dalam daftar pegawai manajer
        for worker in self.__list_worker:
            # Memeriksa apakah nama pegawai saat ini sama dengan nama yang ingin dipecat
            if worker.get_name() == name.title():
                # Menghapus objek Worker dari daftar pegawai manajer
                self.__list_worker.remove(worker)

                # Menambahkan satu ke jumlah total pekerjaan yang telah dilakukan oleh manager
                self.set_total_work(self.get_total_work() + 1)

                # Menampilkan pesan berhasil memecat pegawai
                print(f"Berhasil memecat {name}")
                return
        # Menampilkan pesan jika nama yang ingin dipecat tidak ditemukan
        print("Nama tidak ditemukan")

    # Method untuk memberikan tugas kepada pegawai
    def give_work(self, name: str, bonus: int, cost_stamina: int) -> None:
        # Mengurangkan stamina manajer setiap kali memberikan pekerjaan
        self.set_stamina(self.get_stamina() - 10)

        # Menampilkan pesan awal untuk memberitahu bahwa ketersediaan pegawai sedang dicek
        print("Hasil cek ketersediaan pegawai:")

        # Iterasi melalui setiap pegawai dalam daftar pegawai manajer
        for worker in self.__list_worker:
            # Memeriksa apakah nama pegawai saat ini sama dengan nama yang akan diberi pekerjaan
            if worker.get_name() == name.title():
                # Memeriksa apakah pegawai memiliki stamina yang cukup untuk menerima pekerjaan
                if worker.is_available(cost_stamina):
                    # Menampilkan pesan bahwa pegawai dapat menerima pekerjaan
                    print("Pegawai dapat menerima pekerjaan")

                    # Memanggil method work pada objek Worker untuk mengeksekusi pekerjaan
                    worker.work(bonus=bonus, cost_stamina=cost_stamina)

                    # Menambahkan satu ke jumlah total pekerjaan yang telah dilakukan oleh manager
                    self.set_total_work(self.get_total_work() + 1)

                    # Menampilkan pesan berhasil memberi pekerjaan kepada pegawai
                    print("========================================")
                    print(f"Berhasil memberi pekerjaan kepada {name}")
                    return
                else:
                    # Menampilkan pesan bahwa pegawai tidak dapat menerima pekerjaan karena stamina tidak cukup
                    print(
                        "Pegawai tidak dapat menerima pekerjaan. Stamina pegawai tidak cukup."
                    )
                    return
        # Menampilkan pesan jika nama pegawai tidak ditemukan
        print("Nama tidak ditemukan")


class Worker(Person):
    def __init__(self, name: str, payment: int, stamina: int) -> None:
        """
        Inisialisasi objek Worker yang merupakan subclass dari Person.

        Parameters:
        - name (str): nama dari worker.
        - payment (int): jumlah bayaran untuk tiap pekerjaan yang dikerjakan.
        - stamina (int): nilai yang menentukan worker mampu bekerja atau tidak.
        """
        # Memanggil konstruktor class (Person)
        super().__init__(name, payment, stamina)

        # Menambahkan atribut khusus untuk class Worker
        self.__bonus = 0

    # Method untuk mengeksekusi pekerjaan
    def work(self, bonus: int, cost_stamina: int) -> None:
        # Mengurangkan stamina pegawai sesuai dengan biaya stamina untuk pekerjaan
        self.set_stamina(self.get_stamina() - cost_stamina)

        # Menambahkan bonus ke atribut bonus pegawai
        self.set_bonus(self.get_bonus() + bonus)

        # Menambahkan satu ke jumlah total pekerjaan yang telah dilakukan oleh pegawai
        self.set_total_work(self.get_total_work() + 1)

    # Method untuk mendapatkan nilai atribut bonus
    def get_bonus(self) -> int:
        return self.__bonus

    # Method untuk mengatur nilai atribut bonus
    def set_bonus(self, new_bonus: int) -> None:
        self.__bonus = new_bonus

    # Method untuk menghitung jumlah gaji yang harus dibayarkan
    def pay_day(self) -> int:
        return (self.get_payment() * self.get_total_work()) + self.__bonus


# Function utama program
def main() -> None:
    # Mendapatkan input awal dari pengguna
    name = input("Masukkan nama manajer: ")
    payment = int(input("Masukkan jumlah pembayaran: "))
    stamina = int(input("Masukkan stamina manajer: "))

    # Membuat objek Manager
    manager = Manager(name.title(), payment, stamina)

    # Loop utama program
    while manager.is_available(1):
        print(
            """
PACILOKA
-----------------------
1. Lihat status pegawai
2. Beri tugas
3. Cari pegawai baru
4. Pecat pegawai
5. Keluar
-----------------------
        """
        )
        # Meminta input untuk perintah dari pengguna
        action = int(input("Masukkan pilihan: "))

        if action == 1:
            # Menampilkan seluruh nama pegawai (termasuk manajer) yang ada di dalam sistem
            for worker in manager.get_list_worker():
                print(worker)
            print(manager)

        elif action == 2:
            # Memberikan tugas ke pegawai beserta bonus dan stamina jika melakukan tugas tersebut
            name = input("Tugas akan diberikan kepada: ")
            bonus = int(input("Bonus pekerjaan: "))
            cost_stamina = int(input("Beban stamina: "))
            manager.give_work(name=name, bonus=bonus, cost_stamina=cost_stamina)

        elif action == 3:
            # Menambahkan pegawai baru
            name = input("Nama pegawai baru: ")
            manager.hire_worker(name=name)

        elif action == 4:
            # Memecat pegawai dari sistem dan menghapusnya dari daftar status pegawai
            name = input("Nama pegawai yang akan dipecat: ")
            manager.fire_worker(name=name)

        elif action == 5:
            # Jika pilihan adalah '5', keluar dari loop dan tampilkan pesan sampai jumpa
            print(
                """
----------------------------------------
Berhenti mengawasi hotel, sampai jumpa !
----------------------------------------"""
            )
            return
    print(
        """
----------------------------------------
Stamina manajer sudah habis, sampai jumpa !
----------------------------------------"""
    )


# Memastikan bahwa script ini dijalankan sebagai program utama
if __name__ == "__main__":
    main()
