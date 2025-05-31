# Soal Latihan 1
# game = {'Mobile Legends', 'Free Fire', 'PUBG', 'Among Us'}
# edukasi = {'Ruangguru', 'Duolingo', 'Kahoot', 'PUBG'}
# produtivitas = {'Google Docs', 'Zoom', 'Kahoot', 'Ruangguru'}

# semua_aplikasi = game | edukasi | produtivitas
# app_count = {}

# for apk in semua_aplikasi:
#     count = 0
#     if apk in game:
#         count += 1
#     if apk in edukasi:
#         count += 1
#     if apk in produtivitas:
#         count += 1
#     app_count[apk] = count

# hanya_satu_categori = {app for app, count in app_count.items() if count == 1}
# print("Aplikasi yang hanya muncul di satu kategori: ")
# print(hanya_satu_categori)

# dalam_dua_kategori = {app for app, count in app_count.items() if count == 2}
# print("\nAplikasi yang muncul tepat di dua kategori: ")
# print(dalam_dua_kategori)

# Soal Latihan 2
# data_list = ['apel', 'jeruk', 'apel', 'mangga']
# print("List sebelum dikonversi:", data_list)
# list_to_set = set(data_list)
# print("Set setelah dikonversi dari List:", list_to_set)
# print()

# data_set = {'python', 'java', 'c++'}
# print("Set sebelum dikonversi:", data_set)
# set_to_list = list(data_set)
# print("List setelah dikonversi dari Set:", set_to_list)
# print()

# data_tuple = ('a', 'b', 'a', 'c')
# print("Tuple sebelum dikonversi:", data_tuple)
# tuple_to_set = set(data_tuple)
# print("Set setelah dikonversi dari Tuple:", tuple_to_set)
# print()

# set_data = {1, 2, 3, 2}
# print("Set sebelum dikonversi:", set_data)
# set_to_tuple = tuple(set_data)
# print("Tuple setelah dikonversi dari Set:", set_to_tuple)

# Soal Latihan 3
def baca_kata_dari_file(nama_file):
    try:
        with open(nama_file, 'r') as file:
            isi = file.read().lower()  
            kata = isi.split()  
            return set(kata)  
    except FileNotFoundError:
        print(f"Error: File '{nama_file}' tidak ditemukan.")
        return None
    except IOError:
        print(f"Error: Tidak bisa membaca file '{nama_file}'.")
        return None

file1 = input("Masukkan nama file pertama: ")
file2 = input("Masukkan nama file kedua: ")

kata_file1 = baca_kata_dari_file(file1)
kata_file2 = baca_kata_dari_file(file2)

if kata_file1 is not None and kata_file2 is not None:
    irisan_kata = kata_file1 & kata_file2
    print("\nKata-kata yang muncul di kedua file:")
    print(irisan_kata)

