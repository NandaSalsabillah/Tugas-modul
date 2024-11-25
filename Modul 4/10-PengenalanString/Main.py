# Mengenal String
# String = kumpulan karakter

data = "ini adalah string" # 21 karakter
print(data)
print(type (data))

# 1. cara membuat string
""""
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
"""

data = 'menggunakan single qoute'
print(data)

data = "menggunakan double quote"
print(data)

print("ini hari jum'at")
print("nama saya ma'ruf")

# 2. Menggunakan tanda \ 

# membuat tanda ' menjadi string
print('mari sholat jum\'at')

print('c:\\user\\adam')

# tab
print("ronaldo\t\tmessi")
print("MU\t\tjuara")

# backspace
print("MU\bjuara")

# newline
print("baris pertama .\nbaris kedua.") # LF = line feed
print("baris pertama,\r\nbaris kedua.") #CRLF = line

# raw string 
print(r'c:\user\adam')