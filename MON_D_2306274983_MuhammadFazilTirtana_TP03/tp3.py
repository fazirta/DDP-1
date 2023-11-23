# TP 3 | Dasar-Dasar Pemrograman 1
# Nama: Muhammad Fazil Tirtana
# Jurusan: Ilmu Komputer
# Kode Asdos: MON
# Kelas: D
# NPM: 2306274983

import matplotlib.pyplot as plt


def get_type(a_str):
    """
    Mengembalikan tipe dari literal string a_str.

    parameter:
        a_str (string): string literal dari sebuah nilai

    return (string): "int", "float", atau "str"
    """
    try:
        int(a_str)
        return "int"
    except:
        try:
            float(a_str)
            return "float"
        except:
            return "str"


def read_csv(file_name, delimiter=","):
    """
    parameter:
        file_name (string): nama file comma separated value
        delimiter (string): karakter pemisah antar kolom pada suatu baris.

    return (list, list, list): (data, list nama kolom, list tipe data)
    """
    # Buka file dengan nama yang ditentukan, dengan newline="" untuk menghapus karakter newline secara konsisten
    with open(file_name, newline="") as f:
        # Baca konten file, pecah setiap baris, dan kemudian pecah setiap baris menggunakan delimiter yang ditentukan
        content = f.read().splitlines()
        content = [line.split(delimiter) for line in content]

    # Mengambil header (list nama kolom) dan data dari konten
    header = content[0]
    data = content[1:]

    # Periksa apakah data kosong
    if not data:
        raise Exception("Tabel tidak boleh kosong.")

    # Dapatkan jumlah kolom dalam data
    num_columns = len(header)

    # Periksa apakah jumlah kolom konsisten di semua baris
    if any(len(row) != num_columns for row in data):
        raise Exception("Banyaknya kolom pada baris tidak konsisten.")

    # Inisialisasi list untuk menyimpan tipe data dari setiap kolom, dengan asumsi semua kolom awalnya bertipe "int"
    types = ["int"] * num_columns

    # Iterasi setiap kolom dan setiap baris untuk menentukan tipe data dari setiap kolom
    for i in range(num_columns):
        for j in range(len(data)):
            # Dapatkan tipe data dari sel saat ini menggunakan fungsi get_type
            cell_type = get_type(data[j][i])
            # Perbarui tipe data kolom berdasarkan tipe data sel saat ini
            if cell_type == "float":
                types[i] = "float"
            elif cell_type == "str":
                types[i] = "str"
                # Hentikan loop dalam jika tipe "str" ditemukan dalam kolom saat ini
                break

    # Konversi data di setiap kolom ke tipe yang sesuai berdasarkan tipe data yang ditentukan
    for i in range(num_columns):
        for j in range(len(data)):
            if types[i] == "int":
                data[j][i] = int(data[j][i])
            elif types[i] == "float":
                data[j][i] = float(data[j][i])

    # Kembalikan data yang telah diproses, header, dan list tipe data
    return data, header, types


def to_list(dataframe):
    """
    Mengembalikan bagian list of lists of items atau tabel data pada dataframe. Gunakan fungsi ini kedepannya jika ada keperluan untuk akses bagian data/tabel pada dataframe.

    parameter:
        dataframe (list, list, list): sebuah dataframe yang merupakan 3-tuple

    return (list): list of lists of items
    """
    return dataframe[0]


def get_column_names(dataframe):
    """
    Mengakses daftar nama kolom pada sebuah dataframe.

    parameter:
        dataframe (list, list, list): sebuah dataframe yang merupakan 3-tuple

    return (list): list of column names
    """
    return dataframe[1]


def get_column_types(dataframe):
    """
    Daftar tipe data dari setiap kolom tabel. Hanya ada tiga jenis tipe data, yaitu "str", "int", dan "float"

    parameter:
        dataframe (list, list, list): sebuah dataframe yang merupakan 3-tuple

    return (list): list of type names
    """
    return dataframe[2]


def head(dataframe, top_n=10):
    """
    Mengembalikan string yang merupakan representasi tabel (top_n baris pertama).

    parameter:
        dataframe (list, list, list): sebuah dataframe
        top_n (int): n, untuk penampilan top-n baris saja

    return (string): representasi string dari penampilan tabel.
    """
    cols = get_column_names(dataframe)
    out_str = ""
    out_str += "|".join([f"{str(col)[:15]:>15}" for col in cols]) + "\n"
    out_str += ("-" * (15 * len(cols) + (len(cols) - 1))) + "\n"
    for row in to_list(dataframe)[:top_n]:
        out_str += "|".join([f"{str(col)[:15]:>15}" for col in row]) + "\n"
    return out_str


def info(dataframe):
    """
    Mengembalikan string yang merupakan representasi informasi dataframe.

    parameter:
        dataframe (list, list, list): sebuah dataframe

    return (string): representasi string dari info dataframe
    """
    # Inisialisasi string kosong untuk menyimpan informasi dataframe
    out_str = ""

    # Tambahkan informasi jumlah total baris ke dalam string
    out_str += f"Total Baris = {len(dataframe[0])} baris\n\n"

    # Tambahkan header untuk kolom dan tipe data ke dalam string
    out_str += f"{'Kolom':<15}{'Tipe':<15}\n"
    out_str += f"------------------------------\n"

    # Iterasi nama kolom dan tipe data untuk setiap kolom, dan tambahkan ke dalam string
    for i in range(len(dataframe[1])):
        out_str += f"{dataframe[1][i]:<15}{dataframe[2][i]:<15}\n"

    # Kembalikan string yang berisi informasi dataframe
    return out_str


def satisfy_cond(value1, condition, value2):
    """
    parameter:
        value1 (tipe apapun yang comparable): nilai pertama
        condition (string): salah satu dari ["<", "<=", "==", ">", ">=", "!="]
        value2 (tipe apapun yang comparable): nilai kedua

    return (boolean): hasil perbandingan value1 dan value2

    """
    if condition == "<":
        return value1 < value2
    elif condition == "<=":
        return value1 <= value2
    elif condition == ">":
        return value1 > value2
    elif condition == ">=":
        return value1 >= value2
    elif condition == "!=":
        return value1 != value2
    elif condition == "==":
        return value1 == value2
    else:
        raise Exception(f"Operator {condition} tidak dikenal.")


def select_rows(dataframe, col_name, condition, value):
    """
    Mengembalikan dataframe baru dimana baris-baris sudah dipilih hanya yang nilai col_name memenuhi 'condition' terkait 'value' tertentu.

    parameter:
        dataframe (list, list, list): sebuah dataframe
        col_name (string): nama kolom sebagai basis untuk selection
        condition (string): salah satu dari ["<", "<=", "==", ">", ">=", "!="]
        value (tipe apapun): nilai untuk basis perbandingan pada col_name

    return (list, list, list): dataframe baru hasil selection atau filtering

    """
    # Inisialisasi dataframe baru yang akan menyimpan hasil seleksi
    new_data = []

    # Dapatkan data, header (list nama kolom), dan tipe data dari dataframe
    data = to_list(dataframe)
    header = get_column_names(dataframe)
    types = ["int"] * len(header)

    # Periksa apakah col_name tidak ditemukan
    if col_name not in header:
        raise Exception(f"Kolom {col_name} tidak ditemukan.")

    # Iterasi setiap baris data untuk seleksi
    for i in range(len(data)):
        # Gunakan function satisfy_cond untuk menentukan apakah baris memenuhi syarat
        if satisfy_cond(data[i][header.index(col_name)], condition, value):
            # Tambahkan baris yang memenuhi syarat ke dataframe baru
            new_data.append([str(d) for d in data[i]])

    # Tentukan tipe data baru untuk setiap kolom berdasarkan dataframe baru
    for i in range(len(types)):
        for j in range(len(new_data)):
            if get_type(new_data[j][i]) == "float":
                types[i] = "float"
            elif get_type(new_data[j][i]) == "str":
                types[i] = "str"
                break

    # Konversi nilai pada dataframe baru ke tipe data yang sesuai
    for i in range(len(types)):
        for j in range(len(new_data)):
            if types[i] == "int":
                new_data[j][i] = int(new_data[j][i])
            elif types[i] == "float":
                new_data[j][i] = float(new_data[j][i])

    # Kembalikan dataframe baru yang sudah diproses
    return new_data, header, types


def select_cols(dataframe, selected_cols):
    """
    Mengembalikan dataframe baru dimana kolom-kolom sudah dipilih hanya yang terdapat pada 'selected_cols' saja.

    parameter:
        dataframe (list, list, list): sebuah dataframe
        selected_cols (list): list of strings, atau list yang berisi daftar nama kolom

    return (list, list, list): dataframe baru hasil selection pada kolom, yaitu hanya mengandung kolom-kolom pada selected_cols saja.

    """
    # Dapatkan data, header (list nama kolom), dan tipe data dari dataframe
    data = to_list(dataframe)
    header = get_column_names(dataframe)
    types = get_column_types(dataframe)

    # Validasi bahwa selected_cols tidak boleh kosong
    if not selected_cols:
        raise Exception("Parameter selected_cols tidak boleh kosong.")

    # Validasi nama-nama kolom yang ada di selected_cols
    for selected_col in selected_cols:
        if selected_col not in header:
            raise Exception(f"Kolom {selected_col} tidak ditemukan.")

    # Dapatkan indeks kolom yang terdapat pada selected_cols
    selected_cols_indices = [header.index(col) for col in selected_cols]

    # Buat dataframe baru hanya dengan kolom-kolom yang dipilih
    new_data = [[row[i] for i in selected_cols_indices] for row in data]

    # Dapatkan nama kolom dan tipe data yang dipilih
    new_header = [header[i] for i in selected_cols_indices]
    new_types = [types[i] for i in selected_cols_indices]

    # Kembalikan dataframe baru yang sudah diproses
    return new_data, new_header, new_types


def count(dataframe, col_name):
    """
    Mengembalikan dictionary yang berisi frequency count dari setiap nilai unik pada kolom col_name.

    parameter:
        dataframe (list, list, list): sebuah dataframe
        col_name (string): nama kolom yang ingin dihitung frequency nilainya

    return (dict): dictionary yang berisi informasi frequency count dari setiap nilai unik.
    """
    # Dapatkan data, header (list nama kolom), dan tipe data dari dataframe
    data = to_list(dataframe)
    header = get_column_names(dataframe)
    types = get_column_types(dataframe)

    # Periksa apakah data kosong
    if not data:
        raise Exception("Tabel tidak boleh kosong.")

    # Validasi nama kolom
    if col_name not in header:
        raise Exception(f"Kolom {col_name} tidak ditemukan.")

    col_index = header.index(col_name)

    # Validasi tipe data kolom
    if types[col_index] != "str":
        raise Exception(f"Kolom {col_name} harus bertipe string.")

    # Ambil data pada kolom
    col_data = [d[col_index] for d in data]
    unique_col_data = set(col_data)

    frequency = dict((d, 0) for d in unique_col_data)

    # Hitung frekuensi setiap nilai unik pada kolom
    for d in unique_col_data:
        frequency[d] = col_data.count(d)

    return frequency


def mean_col(dataframe, col_name):
    """
    Mengembalikan nilai rata-rata nilai pada kolom 'col_name' di dataframe.

    parameter:
        dataframe (list, list, list): sebuah dataframe
        col_name (string): nama kolom yang ingin dihitung rataannya

    return (float): nilai rataan
    """
    # Dapatkan data, header (list nama kolom), dan tipe data dari dataframe
    data = to_list(dataframe)
    header = get_column_names(dataframe)
    types = get_column_types(dataframe)

    # Periksa apakah data kosong
    if not data:
        raise Exception("Tabel tidak boleh kosong.")

    # Validasi nama kolom
    if col_name not in header:
        raise Exception(f"Kolom {col_name} tidak ditemukan.")

    col_index = header.index(col_name)

    # Validasi tipe data kolom
    if types[col_index] not in ["int", "float"]:
        raise Exception(f"Kolom {col_name} harus bertipe numerik.")

    # Ambil data pada kolom
    col_data = [d[col_index] for d in data]

    # Hitung dan kembalikan nilai rata-rata
    return sum(col_data) / len(col_data)


def show_scatter_plot(x, y, x_label, y_label):
    """
    parameter:
        x (list): list of numerical values, tidak boleh string
        y (list): list of numerical values, tidak boleh string
        x_label (string): label pada sumbu x
        y_label (string): label pada sumbu y

    return None, namun fungsi ini akan menampilkan scatter
    plot dari nilai pada x dan y.
    """
    plt.scatter(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


def scatter(dataframe, col_name_x, col_name_y):
    """
    Menampilkan scatter plot antara kolom col_name_x dan col_name_y pada dataframe.

    parameter:
        dataframe (list, list, list): sebuah dataframe
        col_name_x (string): nama kolom yang nilai-nilainya diplot pada axis x
        col_name_y (string): nama kolom yang nilai-nilainya diplot pada axis y

    return None
    """
    # Dapatkan data, header (list nama kolom), dan tipe data dari dataframe
    data = to_list(dataframe)
    header = get_column_names(dataframe)
    types = get_column_types(dataframe)

    # Periksa apakah data kosong
    if not data:
        raise Exception("Tabel tidak boleh kosong.")

    # Validasi nama kolom
    if col_name_x not in header:
        raise Exception(f"Kolom {col_name_x} tidak ditemukan.")
    if col_name_y not in header:
        raise Exception(f"Kolom {col_name_y} tidak ditemukan.")

    col_index_x, col_index_y = header.index(col_name_x), header.index(col_name_y)

    # Validasi tipe data kolom
    if types[col_index_x] not in ["int", "float"]:
        raise Exception(f"Kolom {col_name_x} harus bertipe numerik.")
    if types[col_index_y] not in ["int", "float"]:
        raise Exception(f"Kolom {col_name_y} harus bertipe numerik.")

    col_data_x, col_data_y = [d[col_index_x] for d in data], [
        d[col_index_y] for d in data
    ]

    # Gunakan fungsi show_scatter_plot untuk menampilkan scatter plot
    show_scatter_plot(col_data_x, col_data_y, col_name_x, col_name_y)


def sort(dataframe, col_name):
    """
    Mengurutkan dataframe berdasarkan kolom dengan nama col_name.

    Metode pengurutan yang digunakan adalah Bubble Sort.

    parameter:
        dataframe (list, list, list): sebuah dataframe
        col_name (string): nama kolom yang akan digunakan sebagai basis pengurutan

    return (list, list, list): dataframe yang sudah diurutkan berdasarkan kolom
    """
    n = len(dataframe[0])  # Jumlah baris pada dataframe
    col_index = dataframe[1].index(
        col_name
    )  # Indeks kolom yang akan digunakan untuk pengurutan

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            # Bandingkan nilai pada kolom col_name pada dua baris berturut-turut
            if dataframe[0][j][col_index] > dataframe[0][j + 1][col_index]:
                # Jika nilai pada baris pertama lebih besar dari nilai pada baris kedua, tukar posisi baris
                dataframe[0][j], dataframe[0][j + 1] = (
                    dataframe[0][j + 1],
                    dataframe[0][j],
                )
                swapped = True
        if not swapped:
            # Jika tidak ada pertukaran pada satu iterasi, dataframe sudah terurut dan keluar dari loop
            break

    return dataframe


def dropna(dataframe):
    """
    Menghilangkan baris yang memiliki kolom yang tidak memiliki nilai (kosong).

    parameter:
        dataframe (list, list, list): sebuah dataframe

    return (list, list, list): dataframe yang sudah dihapus baris kosongnya
    """
    # Inisialisasi dataframe baru yang akan menyimpan hasil seleksi
    new_data = []

    # Dapatkan data, header (list nama kolom), dan tipe data dari dataframe
    data = to_list(dataframe)
    header = get_column_names(dataframe)
    types = ["int"] * len(header)

    # Iterasi setiap baris data untuk seleksi
    for i in range(len(data)):
        if not any(str(d) in ["-", ""] for d in data[i]):
            # Tambahkan baris yang memenuhi syarat ke dataframe baru
            new_data.append([str(d) for d in data[i]])

    # Tentukan tipe data baru untuk setiap kolom berdasarkan dataframe baru
    for i in range(len(types)):
        for j in range(len(new_data)):
            if get_type(new_data[j][i]) == "float":
                types[i] = "float"
            elif get_type(new_data[j][i]) == "str":
                types[i] = "str"
                break

    # Konversi nilai pada dataframe baru ke tipe data yang sesuai
    for i in range(len(types)):
        for j in range(len(new_data)):
            if types[i] == "int":
                new_data[j][i] = int(new_data[j][i])
            elif types[i] == "float":
                new_data[j][i] = float(new_data[j][i])

    # Kembalikan dataframe baru yang sudah diproses
    return new_data, header, types


if __name__ == "__main__":
    # Contoh penggunaan functions

    # Loading data
    df = read_csv("abalone.csv")

    # Data exploration
    print(head(df))
    print(info(df))
    print(count(df, "Sex"))
    print(mean_col(df, "Diameter"))
    print(mean_col(df, "Length"))

    # Memilih row berdasarkan jumlah ring diatas 10
    df1 = select_rows(df, "Rings", ">", 10)
    print(head(df1))

    # Memili column Sex, Diameter dan Length
    df2 = select_cols(df1, ["Sex", "Diameter", "Length"])
    print(head(df2))

    # Sort kolom Diameter
    df3 = sort(df2, "Diameter")
    print(head(df3))

    # Plot kolom Diameter dengan Length
    scatter(df3, "Diameter", "Length")
