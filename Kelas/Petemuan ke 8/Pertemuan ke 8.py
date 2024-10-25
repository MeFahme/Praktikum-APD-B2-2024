
#syntax error
# if cx <10;
#   print("x kurang dari 10 ")
# else:
#   print("x lebih dari 10 ")

#index error
# harga=[10,15,20]
# print(harga[6])


# nama = "fahmi"
# if nama > 5:
# hasil = nama + 5
# print(hasil)

#attribute error
# umur = "saya"
# umur.upper()
# print(umur.upper())


#import error / module not found error
# import anjay

#key error
# data = {
#     "nama": "Panduan Python",
#     "penulis": "Anjay Kumar",
#     "tahun": 2019
# }

# print(data["umur"])

# try:
#   angka = int(input("Masukkan angka: "))
#   print(angka)
# except Exception:
#   print("Input yang anda masukkan bukan angka")
# input("\nKlik enter untuk melanjutkan...")

# angka = int(input("Masukkan angka: "))
# print(angka)


# while True:
#   try:
#     angka = int(input("Masukkan angka: "))
#     print(angka)
#     break
#   except Exception:
#     print("Input yang anda masukkan bukan angka")
#   input("\nKlik enter untuk melanjutkan...")
#   continue

# try:
#   nama = input("Hello, what's your name? ")
#   if len(nama) > 5:
#     raise ValueError("Nama tidak boleh lebih dari 5 karakter")
# except ValueError as e:
#   print(e)

# fungsi rekursif
# def tes():
#   try:
#     umur = int(input("masukkan umur: "))
#   except ValueError:
#     print("Input yang anda masukkan bukan angka")
#     tes()
#   else:
#     print(f"Anda berusia {umur} tahun")

# tes()


# import json

# with open('coba.txt', 'r') as file:
#   konten = file.read()
#   print("DATA AWAL")
# print(konten)


# with open('coba.txt', 'r') as file:
#   for baris in file:
#     print(baris, end='')

# with open('coba.txt', 'a') as file:
#     tulis = input("masukkan input baru: ")
#     file.write(tulis + '\n')

# print(konten)


import json


# experimen database baru
# with open ("database.json", 'r') as file:
#   data = json.load(file)
#   print(data)
#   # for i in data.items():
# asal_baru = input("masukkan asal baru: ")
# data["asal"] = asal_baru

# with open("database.json", 'w') as file:
#     json.dump(data, file, indent=4)

# file.close()

# print("Data asal berhasil diperbarui menjadi:", asal_baru)

# kode bang ghozali
# baca databse
with open ("database.json", "r") as file:
   data = json.load(file)
   print(data)
   file.close()

# tambah database
with open ("database.json", "a") as file:
   json.dump("abs", file)
   file.close()