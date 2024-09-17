print ("INFORMASI TRANSAKSI BELANJA")
nb = str(input("Masukkan Nama Barang yang Anda = "))
hb = float(input("Masukkan Harga Barang = "))
jb = int(input("Masukan Jumlah Barang Anda = "))
dskn = float(input("Masukkan Diskon Barang Sesuai 2 digit terakhir NIM Anda = "))

thb = jb*hb
tdiskon = thb*(dskn/100)
hsd = thb-tdiskon
mod = dskn%3

print(f"""Anda membeli {jb} {nb} dengan harga satuan Rp.{hb}
total harga sebelum diskon adalah Rp.{thb}
total diskon adalah Rp.{tdiskon}
total harga yang harus dibayar adalah Rp.{hsd}
{dskn} dibagai dengan 3 sisanya {mod}""")