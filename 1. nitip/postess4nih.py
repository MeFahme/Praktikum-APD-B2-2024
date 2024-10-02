percobaan = 0
kesempatan_login = 3
username="febri"
pw="90"
while True:
    while percobaan < kesempatan_login:
        masukkan_nama=input("masukkan nama akun kamu:")
        masukkan_pw=input("masukkan pw akun kamu:")
        percobaan += 1
        if masukkan_nama != username or masukkan_pw != pw:
            print("login gagal")
        if masukkan_nama == username or masukkan_pw == pw:
            print('login berhasil')
            berat_badan=float(input("masukkan berat badan: "))
            tinggi_badan=float(input("masukkan tinggi badan: "))
            tinggi_m=float(tinggi_badan/100)
            BMI=float(berat_badan/(tinggi_m * tinggi_m))
            if BMI<18.5:
                print("berat badan kamu underweight")
            elif BMI>=18.5 and BMI<=24.9:
                print("berat badan kamu normal")
            elif BMI>=24.9 and BMI<=29.9:
                print("berat badan kamu overweight")
            elif BMI > 29.9:
                print("mohon maaf badan kamu obesitas")
            opsi = input("ingin berhenti ? \n 1. ya \n 2. tidak \n\n pilih nomor 1/2 : ")
            if opsi == 1:
                break     
    else:
        break
            