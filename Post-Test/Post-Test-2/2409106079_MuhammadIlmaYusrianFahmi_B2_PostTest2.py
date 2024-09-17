print ("INFORMASI TRANSAKSI BELANJA")
nb = str(input("Nama Barang yang Anda Beli = "))
hb = float(input("Berapa Harga Barang = "))
jb = int(input("Berapa Jumlah Barang yang Anda Beli = "))
diskon = float(input("Masukkan Diskon Barang Sesuai 2 digit terakhir NIM Anda = "))

thb = jb*hb
tdiskon = thb*(diskon/100)
hsd = thb-tdiskon
mod = diskon%3

#print (type (nb))

#print ("Anda membeli", jb, nb, "dengan harga satuan", hb, "total sebelum diskon adalah", thb, "total diskon adalah", tdiskon, "dan total harga yang harus dibayar adalah", hsd)
#print (diskon, "dibagi dengan 3 sisanya", mod)

print(f"""Anda membeli {jb} {nb} dengan harga satuan Rp.{hb}
total harga sebelum diskon adalah Rp.{thb}
total diskon adalah Rp.{tdiskon}
total harga yang harus dibayar adalah Rp.{hsd}
{diskon} dibagai dengan 3 sisanya {mod}""")