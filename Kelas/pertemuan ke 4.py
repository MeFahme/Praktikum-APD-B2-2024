# ulang = 10
# for i in range (ulang):
#   print (f"perulangan ke-{i}")


# for i in range (1, 11, 13):
#   print (f"perulangan ke--{i}")

# simpan = "udin petot"
# for i in simpan:
#     print(i)

# simpan = [12, "udin petot", 14.5, True, 'A']
# for i in simpan:
#     print(i)

# for i in range (1,4):
#     for j in range (1,4):
#         print(f"{i} x {j} = {i*j}")
#     print()


# for i in range (1,6,2):
#     for j in range (1,6,2):
#         print(f"{i} x {j} = {i*j}")
#     print()

#ayam turun 10
# for i in range (10, -1, -1):
#     print (f"ayam ke-{i}")

# ulang = "ya"
# hitung = 1
# while ulang == "ya":
#   print(f"perulangan ke {hitung}")
#   ulang = input("masih mau ngulang?")
#   hitung += 1
# print("perulangan selesai")

# x = int(input("masukkan nilai "))
# while x < 10:
#   print(x)
#   x += 1

# hitung = 1
# while True:
#     print(f"perulangan ke {hitung}")
#     ulang = input ("masih mau ngulang? ")
#     if ulang == "tidak":
#       break
#     hitung += 1
# print (f"total perulangan {hitung}")


# print("daftar bil ganjil dari 1-10")
# for i in range(10):
#   if i % 2 == 0:
#       continue
#   # if i == 5:
#   #     break
#   print(i)

user = "admin"
pw = "1234"
salah = 0

while salah <3:
  usname = input("id anda : ")
  pswd = input("pw anda ")
  
  if usname == user and pw == pswd:
    print("login berhasil")
    break

  else:
    print("login gagal, coba lagi")
    salah += 1
