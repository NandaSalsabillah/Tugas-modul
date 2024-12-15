# percabangan
# Percabangan 1 kondisi

# struktur percabangan
"""
   1. if -nya
   2. kondisinya, statement yang harus terpenuhi agar aksi dijalankan
   3. aksinya
"""

nama = input("Masukkan nama anda! ")

# percabangan inline
# if <kondisi> : <aksi>
if nama == "Nanda" : print("Selamat Datang") 
print("Terima Kasih") # bukan aksi

# Percabangan dengan indensitas
if nama == "Nanda" : # kondisi
    print("Selamat Datang") # aksi
    print("Selamat Belajar") # aksi
print("Terima Kasih") # bukan aksi


# percabangan dengan Else Statement
if nama == "Nanda" :
    print("Selamat Datang")
else :
    print("Anda Bukan Nanda")
print("Program Berakhir")