
"""
This module provides functions for interacting with the operating system.
""" #buat hilangin problem missing docstring
import os

def clear():
    """clear terminal"""
    os.system('cls || clear')

def main_menu():
    """show menu"""
    clear()
    print("="*30)
    print("MAIN MENU".center(30))
    print("="*30)
    print("[1] SIGN IN")
    print("[2] SIGN UP")
    print("[3] EXIT")

def admin_menu():
    """show admin menu"""
    clear()
    print("="*30)
    print("SULTAN GAMING CENTRE".center(30))
    print("="*30)
    print("[0] Ganti Password Akun")
    print("[1] Booking Room")
    print("[2] Clear Room")
    print("[3] List Room")
    print("[4] Log Out")
    print("[5] Exit")

def user_menu():
    """show user menu"""
    clear()
    print("="*30)
    print("SULTAN GAMING CENTRE".center(30))
    print("="*30)
    print("[3] List Room")
    print("[4] Log Out")
    print("[5] Exit")

def login(user_akun):
    """login"""
    clear()
    batas_login = 3
    while batas_login > 0:
        clear()
        print("="*30)
        print("MAIN MENU".center(30))
        print("="*30)
        username = input("ID\t\t: ")
        password = input("PASSWORD\t: ")
        if username in user_akun and user_akun[username] == password:
            clear()
            print(f"\nBerhasil Login! anda login sebagai {username}")
            input("\nKlik enter untuk menlanjutkan...")
            return True, username
        batas_login -= 1
        print("\nID atau PASSWORD salah!")
        print(f"\nKesempatan login tersisa {batas_login} kali lagi!")
        input("\nKlik enter untuk menlanjutkan...")
        clear()
    print("\nANDA GAGAL LOGIN 3 KALI. HUBUNGI ADMIN")
    exit()

def bikin_akun(user_akun):
    """bikin akun"""
    clear()
    print("="*30)
    print("BIKIN AKUN DULU GAN!".center(30))
    print("="*30)
    username = input("ID BARU\t\t: ")
    if username in user_akun:
        print("ID sudah ada GAN!")
    else:
        password = input("PASSWORD Baru\t: ")
        akun[username] = password
        print("AKUN JADI SILAHKAN LOGIN GAN!")
    input("\nKlik enter untuk menlanjutkan...")

def booking_room(listsultan_room):
    """booking room"""
    clear()
    print("="*30)
    print("LIST SULTAN MAU BOOKING ROOM".center(30))
    print("="*30)
    sultan = input("Nama Sultan: ")
    if sultan != "0":
        roomsultan = input("Room Sultan: ")
        room_sama = False
        for room in listsultan_room:
            if room == roomsultan:
                room_sama = True
                break
        if room_sama:
            print("\nRoom sedang digunakan")
        else:
            listsultan[sultan] = roomsultan
            print("Nama Sultan Berhasil ditambahkan")
        input("\nKlik enter untuk melanjutkan...")

def list_akun():
    """list akun"""
    clear()
    print("LIST AKUN".center(30))
    print("="*30)
    print("NO. | \t ID\t |\t Pass")
    print("-"*30)
    for u, (username, password) in enumerate(akun.items()):
        print(f"{u+1}\t {username}\t\t {password}")
    ganti_password = input("\nPilih nomor akun yang ingin diubah: ")
    if ganti_password.isdigit() and 0 < int(ganti_password) <= len(akun):
        pilih = list(akun.keys()) [int(ganti_password) -1]
        password_baru = input("Masukkan password baru: ")
        if password_baru:
            akun.update({pilih: password_baru})
            print("Password berhasil diubah")
            input("\nKlik enter untuk melanjutkan...")
        else:
            print("Password tidak boleh kosong")
    else:
        print("\nPilihan tidak valid")
    input("\nKlik enter untuk melanjutkan...")

def clear_room():
    """clear room"""
    clear()
    print("="*30)
    print("CLEAR ROOM SULTAN YANG PULANG".center(30))
    print("="*30)
    print("NO. | \t Sultan\t |\tRoom")
    print("-"*30)
    for index, (sultan, room) in enumerate(listsultan.items()):
        print(f"{index+1}\t {sultan}\t\t {room}")
    input_string = input("\nPilih nomor sultan yang pulang. [0 = kembali] : ")

    if not input_string.isdigit():
        print("input tidak valid")
        input("\nKlik enter untuk menlanjutkan...")
        return

    index = int(input_string) - 1

    if index == -1:
        return
    elif 0 <= index < len(listsultan):
        hapusroom = list(listsultan.keys())[index]
        listsultan.pop(hapusroom)
        print("Room berhasil dikosongkan")
    else:
        print("input tidak valid")
    input("\nKlik enter untuk menlanjutkan...")

def list_room():
    """list room"""
    clear()
    print("="*30)
    print("LIST ROOM PARA SULTAN".center(30))
    print("="*30)
    print("NO. | \t Sultan\t |\tRoom")
    for index, (sultan, room) in enumerate(listsultan.items()):
        print(f"{index+1}\t {sultan}\t\t {room}")
    input("\nKlik enter untuk menlanjutkan...")

akun = {"admin":"admin"}
listsultan = {}
IS_LOGIN = False

while True:
    clear()
    main_menu()
    pilihan = input("\nMasukkan Pilihan: ")
    if pilihan == "1":
        IS_LOGIN, usersekarang = login(akun)
        if IS_LOGIN:
            while IS_LOGIN:
                clear()
                if usersekarang == "admin":
                    admin_menu()
                else:
                    user_menu()
                pilihan = input("\nMasukkan pilihan: ")

                if pilihan == "0" and usersekarang == "admin":
                    list_akun()

                elif pilihan == "1" and usersekarang == "admin":
                    booking_room(listsultan)

                elif pilihan == "2" and usersekarang == "admin":
                    clear_room()

                elif pilihan == "3":
                    list_room()

                elif pilihan == "4":
                    IS_LOGIN = False

                elif pilihan == "5":
                    exit()

    elif pilihan == "2":
        bikin_akun(akun)

    elif pilihan == "3":
        IS_LOGIN = False
        clear()
        break

    else:
        print("PILIHAN GADA GAN")
        input("\nKlik enter untuk menlanjutkan...")
        continue
