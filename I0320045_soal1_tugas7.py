#Soal nomor 1
#Membuat program dengan menggunakan min 3 jenis fungsi string
print("UNS Nickname Generator")
print("-----------------------------------")
print("")
print("Selamat datang di UNS Nickname Generator")
print("""Ingin membuat nickname untuk akun game, akun medsos, dan akun lainnya??
#.ya
#.tidak""")
answer = input("> ")
if answer == "ya":
    print("")
    input("Klik ENTER untuk memulai")
    print("")
    print("Isi data data berikut:")
    print("")
    nama_lengkap = input("Masukkan nama lengkap kamu: ")
    zodiak = input("Masukkan zodiak kamu: ")
    angka_kesukaan = input("Masukkan 1 angka kesukaan kamu: ")
    d = nama_lengkap.capitalize()
    b = zodiak.capitalize()
    a = angka_kesukaan.capitalize()
    nickname = ""
    if (len(d) > 2):
        nickname += d[0:2]
    else:
        nickname += d
    if (len(b) > 2):
        nickname += b[:2]
    else:
        nickname += b
    if (len(a) > 2):
        nickname += a[:2]
    else:
        nickname += a
    nickname += angka_kesukaan
    print("")
    print("Wow nickname anda sangat keren")
    print("= ", nickname)

elif answer == "tidak":
    print("Terima kasih telah berkunjung")
else:
    pass
print("")
input("Klik ENTER untuk keluar")
print("")
print(":)")
print("Finish")