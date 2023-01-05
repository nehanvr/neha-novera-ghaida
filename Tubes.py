dict_rumah_ganjil = {}
dict_rumah_genap = {}

my_file = open("C:\\Users\\anand\\Documents\\KULIAH\\CodingBelajar\\JOKI_NEHA.txt", "r")
teks = my_file.readline()
mylist = teks.split()

for i in range(2):
    mylist[i] = int(mylist[i])

cek_default_Rumah, cek_banyak_Rumah = mylist[0], mylist[1]

for i in range(1,cek_banyak_Rumah+1):
    if i % 2 == 0:
        dict_rumah_genap[i] = "tidak tahu"
    else:
        dict_rumah_ganjil[i] = "tidak tahu"

if cek_default_Rumah % 2 == 0:
    dict_rumah_genap[cek_default_Rumah] = "anda"
else:
    dict_rumah_ganjil[cek_default_Rumah] = "anda"

teks = my_file.readline()
while teks != "":
    kalimat = teks.split()
    temp = int(kalimat[0])

    for i in dict_rumah_ganjil:
        if dict_rumah_ganjil[i] == kalimat[5]:
            tampung = i
            break

    for j in dict_rumah_genap:
        if dict_rumah_genap[j] == kalimat[5]:
            tampung = j
            break

    if kalimat[2] == 'seberang':
        if kalimat[3] == 'kiri':
            if tampung % 2 == 1:
                tampung += 1
                nomor = 2 * temp
                tampung -= nomor
                dict_rumah_genap[tampung] = kalimat[9]
            else:
                tampung -= 1
                nomor = 2 * temp
                tampung -= nomor
                dict_rumah_ganjil[tampung] = kalimat[9]
        elif kalimat[3] == 'kanan':
            if tampung % 2 == 1:
                tampung += 1
                nomor = 2 * temp
                tampung += nomor
                dict_rumah_genap[tampung] = kalimat[9]
            else:
                tampung -= 1
                nomor = 2 * temp
                tampung += nomor
                dict_rumah_ganjil[tampung] = kalimat[9]

    elif kalimat[2] == 'sebelah':
        if kalimat[3] == 'kiri':
            if tampung % 2 == 1:
                nomor = 2 * temp
                tampung -= nomor
                dict_rumah_ganjil[tampung] = kalimat[9]
            else:
                nomor = 2 * temp
                tampung -= nomor
                dict_rumah_genap[tampung] = kalimat[9]
        elif kalimat[3] == 'kanan':
            if tampung % 2 == 1:
                nomor = 2 * temp
                tampung += nomor
                dict_rumah_ganjil[tampung] = kalimat[9]
            else:
                nomor = 2 * temp
                tampung += nomor
                dict_rumah_genap[tampung] = kalimat[9]

    teks = my_file.readline()

print(dict_rumah_genap)
print(dict_rumah_ganjil)

def nomor_rumah():
    nama_Rumah = input("Masukkan nama penghuni rumah yang akan dicek : ")
    lower_nama_rumah = nama_Rumah.lower()

    flag_ganjil = 1
    for i in dict_rumah_ganjil:
        cek_lower = dict_rumah_ganjil[i].lower()
        if lower_nama_rumah == cek_lower:
            return flag_ganjil

        flag_ganjil += 2

    flag_genap = 2
    for j in dict_rumah_genap:
        cek_lower = dict_rumah_genap[j].lower()
        if lower_nama_rumah == cek_lower:
            return flag_genap

        flag_genap += 2

    kosong = 'tidak tahu'
    return kosong

print(nomor_rumah())