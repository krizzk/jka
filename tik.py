
# 1 Program Hello World
print("Hello, World!")
print("\n")

# 2 Menghitung akara kuadrat
angka = float(input("Masukan angka: "))
akar_kuadrat = angka ** 0.5
print("Akar kuadrat dari", angka, "adalah", akar_kuadrat)
print("\n")

# 3 Menghitung luas persegi panjang
panjang = float(input("Masukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))
luas = panjang * lebar
print("Luas persegi panjang dengan panjang", panjang, "dan lebar", lebar, "adalah", luas)
print("\n")


# 4 Menghitung Volume kubus
sisi = float(input("Masukkan panjang sisi kubus: "))
volume = sisi ** 3
print("Volume kubus dengan sisi", sisi, "adalah", volume)
print("\n")

# 5 Mengurutkan kata sesuai abjad
kata = input("Masukkan kata-kata yang akan diurutkan (pisahkan dengan spasi): ")
daftar_kata = kata.split()
daftar_kata.sort()
kata_urut = ' '.join(daftar_kata)
print("Kata-kata setelah diurutkan: ", kata_urut)
print("\n")

# 6 Mengubah Kilometer menjadi mil
kilometer = float(input("Masukkan jumlah kilometer: "))
mil = kilometer * 0.621371
print(kilometer, "kilometer adalah sama dengan", mil, "mil")
print("\n")

# 7 Menghitung rata-rata
jumlah_angka = int(input("Masukkan jumlah angka: "))
total = 0
for i in range(jumlah_angka):
 angka = float(input("Masukkan angka ke-{}: ".format(i + 1)))
 total += angka
rata_rata = total / jumlah_angka
print("Rata-rata dari angka-angka tersebut adalah", rata_rata)
print("\n")

# 8 Menentukan bilangan prima
bilangan = int(input("Masukkan bilangan: "))
if bilangan > 1:
 for i in range(2, bilangan):
    if (bilangan % i) == 0:
     print(bilangan, "bukan bilangan prima")
     break
 else:
     print(bilangan, "adalah bilangan prima")
else:
    print(bilangan, "bukan bilangan prima")
print("\n")
        

# 9 Menebak angka acak
import random

angka_acak = random.randint(1, 100)
tebakan = 0
while True:
    tebakan = int(input("Tebak angka (1-100): "))
    if tebakan < angka_acak:
         print("Angka terlalu kecil, coba lagi!")
    elif tebakan > angka_acak:
         print("Angka terlalu besar, coba lagi!")
    else:
         print("Selamat, tebakan Anda benar!")
         break
print("\n")

# 10 Menghitung faktorial
bilangan = int(input("Masukkan bilangan: "))
faktorial = 1
if bilangan < 0:
 print("Maaf, faktorial tidak dapat dihitung untuk bilangan negatif")
elif bilangan == 0:
    print("Faktorial dari 0 adalah 1")
else:
 for i in range(1, bilangan + 1):
    faktorial *= i
    print("Faktorial dari", bilangan, "adalah", faktorial)
print("\n")

# 11 Mengkonversi suhu Celsius ke Fahrenheit
celsius = float(input("Masukkan suhu dalam Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Suhu dalam Fahrenheit:", fahrenheit)
print("\n")
    
# 12 Menghitung pangkat
basis = float(input("Masukkan basis: "))
pangkat = int(input("Masukkan pangkat: "))
hasil = basis ** pangkat
print("Hasil dari", basis, "pangkat", pangkat, "adalah", hasil)
print("\n")

# 13 Mencari bilangan terbesar dan terkecil
jumlah_bilangan = int(input("Masukkan jumlah bilangan: "))
bilangan_terbesar = float('-inf')
bilangan_terkecil = float('inf')

for i in range(jumlah_bilangan):
 bilangan = float(input(f"Masukkan bilangan ke-{i + 1}: "))
 
 if bilangan > bilangan_terbesar:
  bilangan_terbesar = bilangan
 
 if bilangan < bilangan_terkecil:
  bilangan_terkecil = bilangan 

print("Bilangan terbesar:", bilangan_terbesar)
print("Bilangan terkecil:", bilangan_terkecil)
print("\n")

# 14 Menghitung keliling lingkaran
import math
jari_jari = float(input("Masukkan panjang jari-jari lingkaran: "))
keliling = 2 * math.pi * jari_jari
print("Keliling lingkaran dengan jari-jari", jari_jari, "adalah", keliling)
print("\n")

# 15 Mencari nilai mutlak
bilangan = float(input("Masukkan bilangan: "))
nilai_mutlak = abs(bilangan)
print("Nilai mutlak dari", bilangan, "adalah", nilai_mutlak)
print("\n")

# 16 Menghitung persentase
nilai = float(input("Masukkan nilai: "))
total_nilai = float(input("Masukkan total nilai: "))
persentase = (nilai / total_nilai) * 100
print("Persentase:", persentase, "%")
print("\n")

# 17 Menentukan hari dan tanggal
import datetime

tahun = int(input("Masukkan tahun: "))
bulan = int(input("Masukkan bulan: "))
tanggal = int(input("Masukkan tanggal: "))
tanggal_input = datetime.date(tahun, bulan, tanggal)
nama_hari = tanggal_input.strftime("%A")
tanggal_format = tanggal_input.strftime("%d %B %Y")
print("Tanggal", tanggal_format, "adalah hari", nama_hari)
print("\n")

# 18 Membalik kata atau kalimat
kata_kalimat = input("Masukkan kata atau kalimat: ")
balik = kata_kalimat[::-1]
print("Hasil pembalikan:", balik)

# 19 Menghitung Umur (dalam Tahun, Bulan, Hari)
from datetime import datetime

tanggal_lahir = input("Masukkan tanggal lahir (YYYY-MM-DD): ")
tanggal_lahir = datetime.strptime(tanggal_lahir, "%Y-%m-%d")

tanggal_sekarang = datetime.now()
umur = tanggal_sekarang - tanggal_lahir

umur_tahun = umur.days // 365
sisa_hari = umur.days % 365
umur_bulan = sisa_hari // 30
sisa_hari = sisa_hari % 30

print("Umur Anda:", umur_tahun, "tahun,", umur_bulan, "bulan,", sisa_hari, "hari")

# 20 Menentukan Kategori Nilai (A, B, C, D)
nilai = float(input("Masukkan nilai: "))

if nilai >= 80:
    kategori = "A"
elif nilai >= 70:
    kategori = "B"
elif nilai >= 60:
    kategori = "C"
else:
    kategori = "D"
print("Kategori nilai:", kategori)

print("TAMAT BJIIIRRRRRRR :)")
print("Kangen kamu")
print("lope uuu")
