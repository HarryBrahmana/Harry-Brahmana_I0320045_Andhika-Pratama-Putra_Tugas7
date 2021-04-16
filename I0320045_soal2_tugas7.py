#Soal nomor 2
#Membuat program dengan menggunakan min 3 jenis fungsi numerik
print("UNS Super Kalkulator ")
print("-----------------------------------")
print("")
print("UNS Super Kalkulator")
print("Akurat, Super, Teliti ")
print("")
input("Klik ENTER untuk memulai")
print("")
print("Keterangan : "
      "Masukkan angka kamu dengan cara memisahkan setiap nilai dengan klik spasi kemudian masukkan angka berikutnya")
angka = input("Masukkan angka: ").split()
for i in range(len(angka)):
    angka[i] = int(angka[i])
rata_rata = sum(angka)/len(angka)
print("angka yang diinput : ", angka)
print('\n')
import math
print("Nih hasil yang didapatkan: ")
print("1. Angka yang paling tinggi adalah ", max(angka))
print("2. Angka yang paling rendah adalah ", min(angka))
print("3. Rata-rata angka yang kamu masukkan adalah ", rata_rata)
print("4. Rata-rata angka yang kamu masukkan dengan pembulatan ke bawah adalah ", math.floor(rata_rata))
print("5. Rata-rata angka yang kamu masukkan dengan pembulatan ke atas adalah ", math.ceil(rata_rata))
print("")
print("----------------------------------------------------")
print(""" Apakah hasil dari perhitungan kami memuaskan?
#.ya
#.tidak""")
answer = input("> ")
if answer == "ya":
    print("Terima kasih telah menggunakan layanan kami. Sukses ya buat kamu")
elif answer == "tidak":
    print("Mohon maaf atas ketidaknyamanan nya, kami akan coba untuk memperbaharui layanan kami menjadi lebih baik. Terima kasih sudah menggunakan layanan kami")
else:
    pass
input("Klik ENTER untuk keluar")
print("")
print(":)")
print("Finish")