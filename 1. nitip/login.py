username = "fahmi"
password = "79"
gagal = 3

print(f"Anda memiliki {gagal} kali kesempatan untuk login")
while gagal <= 3:
  
  loginname = input("masukkan username anda : ")
  loginpassword = input("masukkan password sesuai 2 digit terakhir nim anda: ")
  
  if loginname == username and loginpassword == password:
    print("login berhasil")
    break

  else:
    gagal -= 1
    print()

    if gagal != 0:
      print(f"percobaan login anda sisa {gagal}")
      print()

    elif gagal <=0:
      print(f"sisa percobaan login anda = {gagal} silahkan hubungi admin")
      exit()