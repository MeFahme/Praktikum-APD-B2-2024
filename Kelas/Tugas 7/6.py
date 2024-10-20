"""
This module provides functions for interacting with the operating system.
""" #cuma buat hilangin problem missing docstring
import os
os.system('cls || clear')
akun = {"admin":"admin"}
listsultan = {}
while True:
    os.system('cls || clear')
    print("="*40)
    print("MAIN MENU".center(40))
    print("="*40)
    print("[1] SIGN IN")
    print("[2] SIGN UP")
    print("[3] EXIT")
    pilihan = input("\nMasukkan Pilihan = ")

    if pilihan == "1":
        BATAS_LOGIN = 3
        IS_LOGIN = False
        while BATAS_LOGIN > 0:
            os.system('cls || clear')
            print("="*40)
            print("MAIN MENU".center(40))
            print("="*40)

            username = input("ID\t\t: ")
            password = input("PASSWORD\t: ")
            if username in akun and akun[username] == password:
                IS_LOGIN = True
                usersekarang = username
                os.system('cls || clear')
                print(f"\nBerhasil Login! anda login sebagai {username}")
                input("\nKlik enter untuk menlanjutkan...")
                break
            BATAS_LOGIN -= 1
            print("\nID atau PASSWORD salah!")
            print(f"\nKesempatan login tersisa {BATAS_LOGIN} kali lagi!")
            input("\nKlik enter untuk menlanjutkan...")

        if IS_LOGIN:
            while IS_LOGIN:
                os.system('cls || clear')
                print("="*40)
                print("SULTAN GAMING CENTRE".center(40))
                print("="*40)

                if usersekarang == "admin":
                    print("[0] Ganti Password Akun")
                    print("[1] Booking Room")
                    print("[2] Clear Room")
                print("[3] List Room")
                print("[4] Log Out")
                print("[5] Exit")
                pilihan = input("\nMasukkan Pilihan: ")


                if pilihan == "1" and usersekarang == "admin":
                    os.system('cls || clear')
                    print("="*40)
                    print("LIST SULTAN MAU BOOKING ROOM".center(40))
                    print("="*40)
                    print("\n[0] untuk kembali")
                    sultan = input("Nama Sultan: ")
                    if sultan == "0":
                        IS_LOGIN = True
                    else:
                        roomsultan = input("Room Sultan: ")
                        if not roomsultan:
                            print("\nRoom tidak boleh kosong")
                            input("\nKlik enter untuk melanjutkan...")
                            continue
                        ROOM_SAMA = False
                        for r, room in listsultan.values():
                            if room == roomsultan:
                                ROOM_SAMA = True
                                break
                        if ROOM_SAMA:
                            print("\nRoom sedang digunakan sultan lain")
                        else:
                            listsultan[sultan] = roomsultan
                            print("Nama Sultan Berhasil ditambahkan")
                        input("\nKlik enter untuk menlanjutkan...")
                        IS_LOGIN = True

                elif pilihan == "0" and usersekarang == "admin":
                    os.system('cls || clear')
                    print("="*40)
                    print("LIST USER".center(40))
                    print("="*40)
                    print("NO. | \t ID\t |\tPASSWORD")
                    for u, (username, password) in enumerate(akun.items()):
                        print(f"{u+1}\t {username}\t\t {password}")
                    ganti_password = input("\nPilih nomor akun yang ingin diubah: ")
                    if ganti_password.isdigit() and 0 < int(ganti_password) <= len(akun):
                        pilih = list(akun.keys()) [int(ganti_password) -1]
                        password_baru = input("Masukkan password baru: ")
                        if password_baru:
                            akun.update({pilih: password_baru})
                            print("Password berhasil diubah")
                        else:
                            print("Password tidak boleh kosong")
                    else:
                        print("\nPilihan tidak valid")
                    input("\nKlik enter untuk melanjutkan...")
                elif pilihan == "2" and usersekarang == "admin":
                    os.system('cls || clear')
                    print("="*40)
                    print("CLEAR ROOM SULTAN YANG PULANG".center(40))
                    print("="*40)
                    print("NO. | \t Sultan\t |\tRoom")
                    for index, (sultan, room) in enumerate(listsultan.items()):
                        print(f"{index+1}\t {sultan}\t\t {room}")
                    input_string = input("\nPilih nomor sultan yang pulang. [0 = kembali] : ")
                    #untuk memastikan input adalah integer
                    if not input_string.isdigit():
                        print("input tidak valid")
                        input("\nKlik enter untuk menlanjutkan...")
                        continue
                    index = int(input_string) -1

                    if index == -1:
                        continue
                    elif 0 <= index < len(listsultan):
                        hapusroom = list(listsultan.keys())[index]
                        listsultan.pop(hapusroom)
                        print("Room berhasil dikosongkan")
                    else:
                        print("input tidak valid")
                    input("\nKlik enter untuk menlanjutkan...")

                elif pilihan == "3":
                    os.system('cls || clear')
                    print("="*40)
                    print("LIST ROOM PARA SULTAN".center(40))
                    print("="*40)
                    print("NO. | \t Sultan\t |\tRoom")
                    for index, (sultan, room) in enumerate(listsultan.items()):
                        print(f"{index+1}\t {sultan}\t\t {room}")
                    input("\nKlik enter untuk menlanjutkan...")

                elif pilihan == "4":
                    os.system('cls || clear')
                    print("="*40)
                    print("GANTI AKUN".center(40))
                    print("="*40)
                    break

                elif pilihan == "5":
                    os.system('cls || clear')
                    print("="*40)
                    print("TERIMAKASIH".center(40))
                    print("="*40)
                    exit()

                else:
                    print("\nPilihan tidak tersedia! atau anda tidak memiliki akses")
                    input("\nKlik enter untuk menlanjutkan...")
            continue
        else:
            print("\nGagal Login! PROGRAM BERHENTI")
            input("\nKlik enter untuk menlanjutkan...")
            IS_LOGIN = False
            break

    elif pilihan == "2":
        os.system('cls || clear')
        print("="*40)
        print("BIKIN AKUN DULU GAN!".center(40))
        print("="*40)
        username = input("ID BARU\t\t: ")
        if username in akun:
            print("ID sudah ada GAN!")
        else:
            password = input("PASSWORD Baru\t: ")
            akun.update({username: password})
            print("AKUN JADI SILAHKAN LOGIN GAN!")
        input("\nKlik enter untuk menlanjutkan...")

    elif pilihan == "3":
        os.system('cls || clear')
        print("="*40)
        print("PROGRAM CLOSED!".center(40))
        print("="*40)
        IS_LOGIN = False
        break

    else:
        print("PILIHAN GADA GAN")
        input("\nKlik enter untuk menlanjutkan...")
        continue
