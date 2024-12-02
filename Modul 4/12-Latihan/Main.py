# import fungsi date

import datetime as dt

# meminta input tanggal lahir
tanggal = int(input("Masukkan tanggal lahir : "))
bulan = int(input("Masukkan bulan lahir :"))
tahun = int(input("Masukkan tahun lahir : "))

# konversi ke tipe date
tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"tanggal_lahir = {tanggal_lahir}")

# tanggal hari ini
hari_ini = dt.date.today()
print(f"hari_ini = {hari_ini}")

# hitung usia dalam tahun dan bulan
usia_tahun = hari_ini.year - tanggal_lahir.year
usia_bulan = hari_ini.month - tanggal_lahir.month

# cetak usia
print(f"usia: {usia_tahun} tahun, {usia_bulan} bulan")


