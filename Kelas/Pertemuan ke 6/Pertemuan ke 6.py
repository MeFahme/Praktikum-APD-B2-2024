# # # # daftar_buku = {
# # # # "Buku1" : "Harry Potter",
# # # # "Buku2" : "Percy Jackson",
# # # # "Buku3" : "Twillight"
# # # # }
# # # # print(daftar_buku["Buku1"])
# # # # print(daftar_buku["Buku2"])
# # # # print(daftar_buku["Buku3"])

# # # # daftar_buku = {}
# # # # daftar_buku["novel"] = "Harry Potter"
# # # # daftar_buku["novel2"] = "Percy Jackson"
# # # # daftar_buku["novel3"] = "Twillight"
# # # # print(["novel1"])

# # # # nama_dict = {
# # # #     "key1": "data",
# # # #     "key2": "data2",
# # # #     "key3": "data3"
# # # # }
# # # # print(nama_dict)

# # # # biodata = {
# # # #   "nama" : "Fahmi",
# # # #   "NIM" : "24090",
# # # #   "KRS" : ["APD", "JARKOM"],
# # # #   "Aktif" : True,
# # # #   "SosMed"  : {
# # # #     "Ig" : "@ysrn",
# # # #     "Dc" : "\'Fhm#312"
# # # #   }
# # # # }
# # # # print(biodata)

# # # # print(f"nama saya adalah {biodata["nama"]}")
# # # # print(f"NIM Saya adalah {biodata["NIM"]}")
# # # # print(f"Instagram : {biodata["SosMed"]["Ig"]}")


# # # game = dict(Burnout = "Racing", Apex = "Shooter")
# # # # print(game)
# # # print({game.get("Burnout")})

# # # nilai = {
# # #     "mtk" : 80,
# # #     "fisika" : 90
# # # }

# # # for i in nilai:
# # #     print(i)
# # # print()

# # # for i, j in nilai.items():
# # #       print(f"nilai {i} anda {j}")

# # game = {
# #   "Burnout" : "Racing",
# #   "Apex" : "Shooter",
# #   "DarkSoul" : "Open-World"
# # }



# # print (game)
# # print()

# # game.update({"Resident" : "Thriller"})

# # print (game)
# # print()

# # cache = game.pop("Resident")
# # print(game)

# # print("jumlah Data = ", len(game))

# # pinjam = game.copy()
# # print ("game yg dipinjam : ", pinjam)

# # import datetime as dt
# # tanggal_sekarang = dt.datetime.now()
# # print(tanggal_sekarang)
# # print()
# # hardware = "procie", "vga", "ssd"
# # value = 2
# # list_hardware = dict.fromkeys(hardware, value)
# # print(list_hardware)

# # game = {
# #   "Burnout" : "Racing",
# #   "Apex" : "Shooter",
# #   "DarkSoul" : "Open-World"
# # }

# # for i in game.keys():
# #     print(i)
# # print()
# # for j in game.values():
# #     print(j)

# # Musik = {
# #     "The Chainsmoker" : ["All we Know", "TheParis"],
# #     "Alan Walker" : ["Alone", "Lily"],
# #     "Neffex" : ["Best of Me", "Memories"]
# # }
# # #akses key dan value dictionary
# # for i, j in Musik.items():
# #     print(f"musik milik {i} adalah : ")
# #     #ambil nilai keys
# #     for song in j:
# #         print(song)
# #     print()

# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18, "hobi" : ["baca", "ngoding"]}
# }
# # # for i, value in mahasiswa.items():
# # #   print("ID Mahasiswa : ", key)
# # #   for key_a, value_a in value.items():
# # #     print (key_a, " : ", value_a)
# # #   print("")

# print(mahasiswa[111]["hobi"])

matkul = {
  "mtk" : 90,
  "fisika" : 80,
  "bio" : 80,
  "kimia" : 70
}
totalnilai = 0
jummatkul = 0

for nilai in matkul.value():
  print(f"Mata Kuliah {i} Nilai : {j}")

