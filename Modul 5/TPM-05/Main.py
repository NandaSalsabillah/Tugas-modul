# Program Diskon Berdasarkan Keanggotaan dan Total Belanja

# Input dari pengguna
member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").strip().lower()
total_belanja = float(input("Masukkan total belanja (Rp): "))

# Inisialisasi diskon
diskon_persen = 0

# Aturan diskon
if member == "ya":
    if total_belanja > 500_000:
        diskon_persen = 20
    else:
        diskon_persen = 10
else:  # Tidak memiliki kartu member
    if total_belanja > 500_000:
        diskon_persen = 5

# Menghitung total diskon dan total bayar
diskon = (diskon_persen / 100) * total_belanja
total_bayar = total_belanja - diskon

# Menampilkan hasil Output
print("\n--- Hasil Program ---")
print(f"Total Belanja: Rp {total_belanja:,.0f}")
print(f"Diskon Persen: {diskon_persen}%")
print(f"Diskon: Rp {diskon:,.0f}")
print(f"Total Bayar: Rp {total_bayar:,.0f}")
