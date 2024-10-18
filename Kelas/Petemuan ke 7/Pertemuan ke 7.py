# def salam():
#     print("Selamat datang di program ini!")
# def kali():
#     x=6*6
#     print("Hasil kali 6*6 adalah:", x)

# salam()
# kali()



# def tambah(a,b):
#     hasil = a+b
#     print(hasil)

# tambah(10,5)


# def tambah(a,b):
#     hasil = a+b
#     return(hasil)

# tambahan = tambah(2,4) + tambah(4,6)

# print(tambahan)


# def pilihan():
#     match opsi:
#         case 1:
#             print(1)
#             return
#         case 2:
#             print(2)
#             return

#     print(3)

# pilihan(2)



#**matkul jadi dictionary , *matkul jadi tuple
# def cetak(nama, nim, **matkul):
#     print(nama,nim,matkul)

# cetak("Fahmi", 69, mtk=90, fisdas=88)


# var = 2,4,5
# print(var)

# var1, var2, var3 = var

# print (var)
# print (var1)
# print (var2)
# print (var3)


#global
# Nama = "Informatika"
# Mata_Kuliah = "Algoritma dan Pemrograman Dasar"
# kelas = "it "

# #lokal
# def info():
#    Nama = "Teknik Elektro"
#    Mata_Kuliah = "Pengantar Teknik ELektro"
#    print("Prodi:", Nama)
#    print("Mata Kuliah:", Mata_Kuliah)
#    print(kelas)

# print()
# print("Prodi:", Nama)
# print("Mata Kuliah:", Mata_Kuliah)

# print()
# info()


# def cetak(nama, nim, umur = 18):
#     print(nama,nim,umur)

# cetak("Fahmi", 41,112)


mahasiswa = ["stephen", "lisa"]
def show():
    for i, data in enumerate(mahasiswa,1):
      print(f"{i} {data}")

show()