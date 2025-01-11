# Input dari pengguna
nama = input("Masukkan nama pelanggan: ")
kartu_member_input = input("Apakah pelanggan memiliki kartu member? (ya/tidak): ").strip().lower()
kartu_member = kartu_member_input == 'ya'
total_belanja = float(input("Masukkan total belanja: "))

# Inisialisasi potongan
potongan = 0

# Menghitung potongan
if kartu_member:
    if total_belanja > 500000:
        potongan = 10  # 10% diskon
    elif 100000 < total_belanja <= 499000:
        potongan = 5  # 5% diskon
else:
    if total_belanja > 100000:
        potongan = 3  # 3% diskon

# Menghitung total setelah potongan
diskon_rupiah = total_belanja * (potongan / 100)
total_setelah_diskon = total_belanja - diskon_rupiah

# Menampilkan informasi
print(f"Nama Pelanggan: {nama}")
print(f"Status Kartu Member: {'Ada' if kartu_member else 'Tidak Ada'}")
print(f"Total Belanja Sebelum Potongan: Rp {total_belanja:,.0f}")
print(f"Diskon: {potongan}%")
print(f"Diskon (dalam Rupiah): Rp {diskon_rupiah:,.0f}")
print(f"Total Belanja Setelah Potongan: Rp {total_setelah_diskon:,.0f}")