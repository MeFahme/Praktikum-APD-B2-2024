"""docstring"""
import os # Menyediakan macam-macam fungsi untuk interaksi dengan sistem operasi
import time # Diginakan untuk jeda time sleep 
import json # dDgunakan untuk bekerja dengan data dalam format JSON (JavaScript Object Notation)
from colorama import Fore 
# Modul colorama digunakan untuk memberikanwarna pada teks yang ditampilkan di terminal
# Fore adalah salah satu bagian dari colorama digunakan untuk mengubah warna teks (foreground) yang ditampilkan di terminal
print(Fore.LIGHTYELLOW_EX)

# Fungsi untuk membaca file akun.json
def muat_akun():
    """encoding utf-8"""
    with open("akun.json", "r", encoding="utf-8") as file:
        return json.load(file)

# Fungsi untuk menulis file akun.json
def save_akun(data):
    """encoding utf-8"""
    with open("akun.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

# Fungsi untuk membaca file vvip_room.json
def muat_rooms():
    """encoding utf-8"""
    with open("vvip_room.json", "r", encoding="utf-8") as file:
        return json.load(file)

# Fungsi untuk menulis file vvip_room.json
def save_rooms(data):
    """encoding utf-8"""
    with open("vvip_room.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

# Fungsi untuk menampilkan menu admin
def admin_menu():
    """admin menu"""
    clear()
    print("=" * 40)
    print("SULTAN GAMING CENTRE".center(40))
    print("=" * 40)
    print("""
[0] Hapus Akun
[1] Booking Room
[2] Hapus Room
[3] Manajemen Room
[4] Info Room
[5] List Room
[6] Log Out
[7] Exit
""")

# Fungsi untuk menampilkan menu user
def user_menu():
    """user menu"""
    clear()
    print("=" * 40)
    print("SULTAN GAMING CENTRE".center(40))
    print("=" * 40)
    print("""
[1] Reservasi Room
[2] List Room
[3] Log Out
[4] Exit
""")

# Fungsi untuk melakukan login
def login(user_akun):
    """login"""
    clear()
    batas_login = 3
    while batas_login > 0:
        clear()
        print("=" * 40)
        print("MAIN MENU".center(40))
        print("=" * 40)
        username = input("ID\t\t: ")
        password = input("PASSWORD\t: ")
        if username in user_akun and user_akun[username] == password:
            print(f"\nHALO {username} !")
            input("\nKlik enter untuk melanjutkan...")
            return True, username
        batas_login -= 1
        print("\nID atau PASSWORD salah!")
        print(f"\nKesempatan login tersisa {batas_login} kali lagi!")
        input("\nKlik enter untuk melanjutkan...")
        clear()
    print("\nANDA GAGAL LOGIN 3 KALI. HUBUNGI ADMIN")
    exit()

# Fungsi untuk membuat akun
def bikin_akun(user_akun):
    """bikin akun"""
    clear()
    print("=" * 40)
    print("BIKIN AKUN DULU GAN!".center(40))
    print("=" * 40)

    while True:
        username = input("ID BARU\t\t: ")
        if username.strip() == "":
            print("ID tidak boleh kosong")
        elif username in user_akun:
            print("ID sudah ada!")
        else:
            break

    while True:
        password = input("PASSWORD Baru\t: ")
        if password.strip() == "":
            print("Password tidak boleh kosong")
        else:
            break

    user_akun[username] = password
    save_akun(user_akun)
    print("AKUN BERHASIL DIBUAT SILAHKAN LOGIN")
    input("\nKlik enter untuk melanjutkan...")

# Fungsi untuk memesan/booking room yang tersedia
def booking_room():
    """Booking room"""
    clear()
    print("=" * 40)
    print("BOOKING ROOM".center(40))
    print("=" * 40)
    room_kosong()

    while True:
        print("\nInput 0 jika ingin kembali")
        sultan = input("Nama Sultan\t\t: ")
        if sultan == "0":
            return
        elif sultan.strip() == "" or not sultan.isalpha():
            clear()
            print("Pastikan input hanya huruf!")
            input("\nKlik enter untuk melanjutkan...")
            clear()
            room_kosong()
        else:
            break

    rooms = muat_rooms()
    rooms_kosong = []
    for r, room in rooms.items():
        if room["status"] == "Tersedia":
            rooms_kosong.append(str(r))

    print("Rooms kosong\t\t:", ", ".join(rooms_kosong))
    nomor_room = input("Nomor Room\t\t: ")

    if nomor_room in rooms_kosong:
        waktu_booking = input("Waktu Booking (Jam)\t: ")
        try:
            waktu_booking = int(waktu_booking)
            harga = rooms[nomor_room]["harga"] * waktu_booking
            rooms[nomor_room]["status"] = "Digunakan"
            rooms[nomor_room]["waktu_bermain"] = waktu_booking
            rooms[nomor_room]["sultan"] = sultan
            save_rooms(rooms)

            if usersekarang == "admin":
                print(f"Total bayar\t\t: Rp {harga:,.0f}")
                input("\nKlik enter untuk melanjutkan...")

            else:
                clear()
                print("=" * 43)
                print("NOTA RESERVASI".center(43))
                print("=" * 43)
                print(f"| NAMA\t\t: {sultan:<24}|")
                print(f"| ROOM\t\t: {nomor_room:<24}|")
                print(f"| WAKTU (Jam)\t: {waktu_booking:<24}|")
                print(f"| TOTAL BAYAR\t: Rp {harga:,.0f}".ljust(40) + "|")
                print("="*43)
                print("Silahkan hubungi @Admin untuk konfirmasi".center(43))
                print("=" * 43)
                time.sleep(5)
                print("Pembayaran telah dikonfirmasi, Terimakasih")
                input("\nKlik enter untuk melanjutkan...")

        except ValueError:
            clear()
            print("Input waktu tidak valid!")
            input("\nKlik enter untuk melanjutkan...")

    else:
        clear()
        print("Room tidak tersedia.")
        input("\nKlik enter untuk melanjutkan...")

# Fungsi untuk menghapus room yang ada
def clear_room():
    """clear room"""
    clear()
    rooms = muat_rooms()
    room_terpakai = []
    for r, room in rooms.items():
        if room["status"] == "Digunakan":
            room_terpakai.append((r, room))

    print("=" * 41)
    print("ROOM YANG SEDANG DIGUNAKAN".center(41))
    print("=" * 41)
    print("| No. |\tSultan\t |\t Room\t\t|")
    print("-" * 41)

    for index, (nomor_room, room) in enumerate(room_terpakai, start=1):
        print(f"| {index: <3} | {room.get('sultan'):<8} |\t {nomor_room:<15}|")

    try:
        print("-"*41)
        print("\nInput 0 untuk kembali")
        pilihan = int(input("Pilih nomor yang akan dihapus: "))

        if pilihan == 0:
            return
        elif pilihan < 1 or pilihan > len(room_terpakai):
            clear()
            print("Nomor room tidak valid.")
            input("\nKlik Enter untuk melanjutkan...")
            return

        hapus_room = room_terpakai[pilihan - 1][0]

        rooms[hapus_room]["status"] = "Tersedia"
        rooms[hapus_room]["waktu_bermain"] = 0
        rooms[hapus_room]["sultan"] = ""

        save_rooms(rooms)
        clear()
        print("DONE")
    except ValueError:
        clear()
        print("Input tidak valid.")
    input("\nKlik Enter untuk melanjutkan...")

# Fungsi untuk informasi semua room
def room_kosong():
    """daftar room tersedia"""
    clear()
    rooms = muat_rooms()
    print("=" * 86)
    print("LIST ROOM".center(86))
    print("=" * 86)
    print("| No.|\tID Room\t|\t Status\t       |\t Fasilitas\t    |\tHarga/Jam    |")
    print("-" * 86)

    room_tersedia = []
    for r, room in rooms.items():
        room_tersedia.append((r, room))

    if room_tersedia:
        for index, (nomor_room, room) in enumerate(room_tersedia, start=1):
            fasilitas = ",".join(room["fasilitas"])
            harga = room["harga"]
            print(f"| {index:<3}| \t{nomor_room}\t|\t{room['status']:<15}|\t{fasilitas:<20}|\tRp. {harga:,.0f}   |")

    else:
        print("Tidak ada room yang kosong.")

    input("\nKlik Enter untuk melanjutkan...")

akun = muat_akun() # Variabel akun menjadi tempat untuk menyimpan data akun yang ada
# Fungsi untuk menampilkan list akun yang telah dibuat
def list_akun():
    """list akun"""
    clear()
    print("LIST AKUN".center(40))
    print("=" * 40)
    print("NO. | \t ID\t |\t Pass")
    print("-" * 40)
    akun_tampil = {username: password for username, password in akun.items() if username != "admin"}

    for u, (username, password) in enumerate(akun_tampil.items(),start=1):
        print(f"{u}\t {username}\t\t {'*' * len(password)}")

    hapus = input("\nPilih nomor akun yang ingin dihapus: ")

    if hapus.isdigit() and 0 < int(hapus) <= len(akun_tampil):
        akun_hapus = list(akun_tampil.keys())[int(hapus) - 1]
        del akun[akun_hapus]
        save_akun(akun)
    else:
        print("\nPilihan tidak valid")
    input("\nKlik enter untuk melanjutkan...")

# Fungsi untuk menampilkan informasi room yang digunakan
def list_room():
    """List room yang digunakan"""
    clear()
    rooms = muat_rooms()
    print("=" * 43)
    print("| ROOM PARA SULTAN |".center(43))
    print("=" * 43)
    print("| NO. | Sultan\t |\tRoom\t  | Waktu |")
    print("-" * 43)

    rooms_digunakan = []
    for r, room in rooms.items():
        if room["status"] == "Digunakan":
            rooms_digunakan.append((r, room))

    for i, (nomor_room, room) in enumerate(rooms_digunakan, start=1):
        print(f"| {i:<4}| {room.get("sultan"):<8} |\t {nomor_room:<6}   | {room["waktu_bermain"]} Jam |")

    input("\nKlik Enter untuk melanjutkan...")

# Fungsi untuk mengahapus terminal
def clear():
    """clear terminal"""
    os.system("cls || clear")

# Fungsi untuk menampilkan main menu
def main_menu():
    """show menu"""
    clear()
    print("=" * 40)
    print("MAIN MENU".center(40))
    print("=" * 40)
    print("[1] SIGN IN")
    print("[2] SIGN UP")
    print("[3] EXIT")

# Fungsi untuk memperbarui (menambah/menghapus) fasilitas room
def update_room():
    """update room"""
    rooms = muat_rooms()
    while True:
        clear()
        print("=" * 41)
        print("UPDATE ROOM".center(41))
        print("=" * 41)
        # menampilkan ID Room dan fasilitas
        for key, room in rooms.items():
            print(f"|Room {key}, Fasilitas: {', '.join(room['fasilitas']):<20}|")
        print("=" * 41)
        print("Input 0 untuk kembali")
        nomor_room = input("Masukkan Nomor Room: ")
        if nomor_room == "0":
            return
        if nomor_room in rooms:
            break
        else:
            clear()
            print("Input tidak valid!")
            input("\nKlik enter untuk melanjutkan...")

    clear()
    fasilitas_sekarang = rooms[nomor_room]["fasilitas"]
    harga_sekarang = rooms[nomor_room]["harga"]

    while True:
        print("=" * 41)
        print(f"Fasilitas Room {nomor_room}: {', '.join(fasilitas_sekarang)}".center(41))
        print("=" * 41)
        print("[1] Tambah fasilitas")
        print("[2] Hapus fasilitas")
        print("[3] Kembali")
        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            list_fasilitas = ["Sim Racing", "PC", "PS 5"]
            clear()
            print("=" * 41)
            print(f"Fasilitas Room {nomor_room}: {', '.join(fasilitas_sekarang)}".center(41))
            print("=" * 41)

            for f, fasilitas in enumerate(list_fasilitas, start=1):
                print(f"{f}. {fasilitas}")

            try:
                pilih_fasilitas = int(input("\nPilih nomor fasilitas yang ditambahkan: "))
                if pilih_fasilitas in range(1, len(list_fasilitas) + 1):
                    fasilitas_baru = list_fasilitas[pilih_fasilitas - 1]

                    if fasilitas_baru not in fasilitas_sekarang:
                        fasilitas_sekarang.append(fasilitas_baru)
                        clear()
                        print(f"{fasilitas_baru} berhasil ditambahkan!")
                        if fasilitas_baru == "Sim Racing":
                            harga_sekarang += 40000
                        elif fasilitas_baru == "PC" or fasilitas_baru == "PS 5":
                            harga_sekarang += 20000
                    else:
                        clear()
                        print(f"{fasilitas_baru} sudah ada di Room {nomor_room}")
                else:
                    clear()
                    print("Nomor fasilitas tidak valid!")
                    input("\nKlik enter untuk melanjutkan...")

            except ValueError:
                clear()
                print("Input tidak valid!")
                input("\nKlik enter untuk melanjutkan...")

        elif pilihan == "2":
            clear()
            print("=" * 41)
            print("Fasilitas yang tersedia untuk dihapus".center(41))
            print("=" * 41)

            for i, fasilitas in enumerate(fasilitas_sekarang, 1):
                print(f"{i}. {fasilitas}")

            try:
                pilih_fasilitas = int(input("Pilih nomor fasilitas yang ingin dihapus: "))
                if 1 <= pilih_fasilitas <= len(fasilitas_sekarang):
                    fasilitas_dihapus = fasilitas_sekarang.pop(pilih_fasilitas - 1)

                    if fasilitas_dihapus == "Sim Racing":
                        harga_sekarang -= 40000
                    elif fasilitas_dihapus == "PC" or fasilitas_dihapus == "PS 5":
                        harga_sekarang -= 20000
                else:
                    clear()
                    print("Nomor fasilitas tidak valid!")
                    input("\nKlik enter untuk melanjutkan...")
            except ValueError:
                clear()
                print("Input tidak valid!")
                input("\nKlik enter untuk melanjutkan...")

        elif pilihan == "3":
            break

        else:
            clear()
            print("Pilihan tidak valid!")
            input("\nKlik Enter untuk melanjutkan...")

        rooms[nomor_room]["fasilitas"] = fasilitas_sekarang
        rooms[nomor_room]["harga"] = harga_sekarang
        save_rooms(rooms)
        input("\nKlik enter untuk melanjutkan...")
        clear()

# Fungsi untuk menghapus room yang digunakkan
def hapus_room():
    """hapus room"""
    clear()
    print("=" * 41)
    print("HAPUS ROOM".center(41))
    print("=" * 41)
    rooms = muat_rooms()
    for key, room in rooms.items():
        print(f"|Room {key}, Fasilitas: {", ".join(room["fasilitas"]):<20}|")
    print("=" * 41)

    nomor_room = input("Masukkan nomor room: ")

    if nomor_room in rooms:
        del rooms[nomor_room]
        print(f"Room {nomor_room} berhasil dihapus.")
        input("\nKlik Enter untuk melanjutkan...")
    else:
        print(f"Room {nomor_room} tidak ditemukan.")
        input("\nKlik Enter untuk melanjutkan...")

    save_rooms(rooms)

# Fungsi untuk menambah room baru kedalam list
def tambah_room():
    """Tambah room baru"""
    clear()
    print("=" * 40)
    print("ROOM BARU".center(40))
    print("=" * 40)
    rooms = muat_rooms()
    nomor_room_baru = str(len(rooms) + 1)
    harga = 0
    fasilitas = []

    print("[1] Rp. 80.000 (Sim Racing, PC, PS 5)")
    print("[2] Rp. 40.000 (PC, PS 5)")
    print("[3] Rp. 20.000 (PC)")

    try:
        pilih = int(input("Masukkan pilihan: "))

        if pilih == 1:
            harga = 80000
            fasilitas = ["Sim Racing", "PC", "PS 5"]

        elif pilih == 2:
            harga = 40000
            fasilitas = ["PC", "PS 5"]

        elif pilih == 3:
            harga = 20000
            fasilitas = ["PC"]

        else:
            print("Pilihan tidak valid!")
            input("\nKlik Enter untuk melanjutkan...")
            return

    except ValueError:
        print("Input tidak valid!")
        input("\nKlik Enter untuk melanjutkan...")
        return

    room_baru = {
        "status" : "Tersedia",
        "waktu_bermain" : 0,
        "sultan" : "",
        "harga" : harga,
        "fasilitas" : fasilitas
    }

    rooms[nomor_room_baru] = room_baru
    save_rooms(rooms)
    print("=" * 40)
    print(f"Room {nomor_room_baru} Ditambahkan".center(40))
    print("=" * 40)

# Fungsi untuk menampilkan menu manajemen room
def atur_room():
    """atur room"""
    while True:
        clear()
        print("=" * 40)
        print("MANAJEMEN ROOM".center(40))
        print("=" * 40)
        print("[1] Tambah Room Baru")
        print("[2] Hapus Room")
        print("[3] Update Fasilitas Room")
        print("[4] Kembali")

        try:
            pilih = int(input("Masukkan Pilihan: "))
            if pilih == 1:
                tambah_room()

            elif pilih == 2:
                hapus_room()

            elif pilih == 3:
                update_room()

            elif pilih == 4:
                break
            else:
                print("Input tidak valid!")
                input("\nKlik enter untuk melanjutkan...")
                clear()

        except ValueError:
            print("Input tidak valid!")
            input("\nKlik enter untuk melanjutkan...")
            clear()

#MAIN PROGRAM
try:
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
                        pilihan = input("Masukkan pilihan: ")

                        if pilihan == "0":
                            list_akun()

                        elif pilihan == "1":
                            booking_room()

                        elif pilihan == "2":
                            clear_room()

                        elif pilihan == "3":
                            atur_room()

                        elif pilihan == "4":
                            list_room()

                        elif pilihan == "5":
                            room_kosong()

                        elif pilihan == "6":
                            IS_LOGIN = False

                        elif pilihan == "7":
                            clear()
                            exit()

                        else:
                            print("\nInput Tidak Valid!")
                            input("\nKlik enter untuk melanjutkan...")

                    else:
                        user_menu()
                        pilihan = input("Masukkan pilihan: ")
                        if pilihan == "1":
                            booking_room()

                        elif pilihan == "2":
                            room_kosong()

                        elif pilihan == "3":
                            IS_LOGIN = False

                        elif pilihan == "4":
                            clear()
                            exit()

                        else:
                            print("\nInput tidak valid!")
                            input("\nKlik enter untuk melanjutkan...")

        elif pilihan == "2":
            bikin_akun(akun)

        elif pilihan == "3":
            IS_LOGIN = False
            clear()
            break

        else:
            print("Input Tidak Valid!")
            input("\nKlik enter untuk melanjutkan...")
            continue
except KeyboardInterrupt:
    print("\nProgram dihentikan.")
