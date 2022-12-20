from coba import coba as kasus

Matriks = []

# Untuk membuat matriks kosong
def BuatMatriks(Matriks, Baris, Kolom):
    for i in range(Baris):
        Matriks.append([])
        for j in range(Kolom):
            Matriks[i].append(0)

# Untuk menampilkan data menjadi Sistem Persamaan Linear
def SPL(Matriks, Baris, Kolom, Aljabar):
    for i in range(Baris):
        Cek = False
        for j in range(Kolom):
            # jika suku 0 maka tidak tampil
            if j < Kolom - 1:
                if Matriks[i][j] != 0:
                    if Cek == True:
                        # otomatis memilih keluaran + dan -
                        if Matriks[i][j] > 0:
                            print(" +", end="")
                        else:
                            print(" ", end="")
                    print(" {}{}".format(Matriks[i][j], Aljabar[j]), end="")
                    Cek = True
                else:
                    if Cek == True:
                        print(" =", Matriks[i][j])
        print()

# Untuk menampilkan matriks
def PrintMatriks(Matriks, Baris, Kolom):
    for i in range(Baris):
        print(" [", end="")
        for j in range(Kolom):
            # jika matriksnya bukan 0 maka angkanya akan disederhanakan menjadi 2 angka di belakang koma
            if Matriks[i][j] != 0:
                Matriks[i][j] = round(Matriks[i][j], 2)
            # print nilai matriks
            print(" {}".format(Matriks[i][j]), end="")
        print("]")

# Algoritma untuk operasi gauss
def Gauss(Matriks, Baris, Kolom, i = 0, x = 0):
    if i < Baris:
        if x < Kolom - 1:
            # jika suku 0 maka akan sorting dengan yang punya angka
            if Matriks[i][x] != 0:
                for j in range(i + 1, Baris):
                    # jika angka atau bukan 0 maka akan ditukar
                    if Matriks[j][x] != 0:
                        # menukar 1 baris dengan baris yang lain
                        for k in range(Kolom):
                            Matriks[i][k], Matriks[j][k] = Matriks[j][k], Matriks[i][k]
                        # menampilkan info
                        print("R{} =><= R{}".format(i + 1, j + 1))
                        PrintMatriks(Matriks, Baris, Kolom)
                        break
            if Matriks[i][x] != 0:
                # mengeliminasi matriks jika tidak 1
                if Matriks[i][x] != 1:
                    temp = Matriks[i][x]
                    for j in range(x, Kolom):
                        Matriks[i][j] = Matriks[i][j] / temp
                    # menampilkan info
                    print("R{} / {}".format(i + 1, temp))
                    PrintMatriks(Matriks, Baris, Kolom)
                for j in range(i + 1, Baris):
                    if Matriks[j][x] != 0:
                        temp = Matriks[j][x] / Matriks[i][x]
                        # jika matriks gak 0 maka akan eliminasi dengan matriks yang awalannya 1
                        for k in range(x, Kolom):
                            Matriks[j][k] = Matriks[j][k] - (temp * Matriks[i][k])
                        # menampilkan info
                        print("R{}".format(j + 1), end="")
                        if temp > 0:
                            print(" - ", end="")
                        else:
                            print(" + ", end="")
                            temp = temp * -1
                        print("{}R{}".format(temp, i + 1))
                        PrintMatriks(Matriks, Baris, Kolom)
                i = i + 1
                Gauss(Matriks, Baris, Kolom, i, x)
            else:
                x = x + 1
                Gauss(Matriks, Baris, Kolom, i, x)

# Algoritma untuk operasi jordan
def Jordan(Matriks, Baris, Kolom, Aljabar):
    Unik = False
    for i in range(Baris):
        Cek1 = True
        Cek2 = False
        for j in range(Kolom):
            if j < Kolom - 1:
                if Matriks[i][j] == 0 and Cek1 == True:
                    Cek1 = True
                else:
                    Cek1 = False
            else:
                if Matriks[i][j] == 0:
                    Cek2 = True
                else:
                    Cek2 = False
        # jika isi baris matriks bernilai 0 dan hasilnya tidak 0 maka tidak ada solusi
        if Cek1 == True and Cek2 == False:
            Solusi = "Tidak ada solusi"
            break
        # jika isi baris matriks bernilai 0 dan hasilnya 0 maka akan ada banyak solusi
        elif Cek1 == True and Cek2 == True:
            Solusi = "Banyak solusi"
            break
        # jika bukan maka solusi unik
        else:
            Solusi = "Solusi unik"
            Unik = True
    if Unik == True or (Cek1 == True and Cek2 == True):
        # perulagan dimulai dari paling bawah
        for i in range(Baris - 1, -1, -1):
            for j in range(Kolom - 1):
                # jika nilai tidak 0 maka akan mengeliminasi yang di atasnya
                if Matriks[i][j] != 0:
                    for k in range(i - 1, -1, -1):
                        # eliminasi matriks yang sejajar
                        if Matriks[k][j] != 0:
                            temp = Matriks[k][j] / Matriks[i][j]
                            for l in range(j, Kolom):
                                Matriks[k][l] = Matriks[k][l] - (temp * Matriks[i][l])
                            # menampilkan info
                            print("R{}".format(k + 1), end="")
                            if temp > 0:
                                print(" - ", end="")
                            else:
                                print(" + ", end="")
                                temp = temp * -1
                            print("{} x R{}".format(temp, i + 1))
                            print(temp, "R", i + 1)
                            PrintMatriks(Matriks, Baris, Kolom)
                    break
        print("~" + Solusi + "~")
        # setelah eliminasi maka akan mengeluarkan nilai dari setiap variabel
        for i in range(Baris):
            Cek = False
            for j in range(Kolom):
                if Matriks[i][j] != 0 and j < Kolom - 1:
                    if Cek == True:
                        print(" +", end="")
                    print(" {}{}".format(Matriks[i][j], Aljabar[j]), end="")
                    Cek = True
            if Cek == True:
                print(" = {}".format(Matriks[i][j]))
# fungsi gauss
def GS():
    print("Masukan data")
    Baris = int(input("Baris : "))
    Kolom = int(input("Kolom : "))
    Kolom = Kolom + 1
    Aljabar = ["x{}".format(i + 1) for i in range(Kolom - 1)]
    BuatMatriks(Matriks, Baris, Kolom)
    for i in range(Baris):
        for j in range(Kolom):
            print("[{}][{}] : ".format(i + 1, j + 1))
            Matriks[i][j] = float(input())
    print()
    print("Sistem Persamaan Linear")
    SPL(Matriks, Baris, Kolom, Aljabar)
    print()
    print("Matriks")
    PrintMatriks(Matriks, Baris, Kolom)
    Gauss(Matriks, Baris, Kolom)

# fungsi gauss jordan
def GSJD():
    print("Masukan data")
    Baris = int(input("Baris : "))
    Kolom = int(input("Kolom : "))
    Kolom = Kolom + 1
    Aljabar = ["x{}".format(i + 1) for i in range(Kolom - 1)]
    BuatMatriks(Matriks, Baris, Kolom)
    for i in range(Baris):
        for j in range(Kolom):
            print("[{}][{}] : ".format(i + 1, j + 1))
            Matriks[i][j] = float(input())
    print()
    print("Sistem Persamaan Linear")
    SPL(Matriks, Baris, Kolom, Aljabar)
    print()
    print("Matriks")
    PrintMatriks(Matriks, Baris, Kolom)
    Gauss(Matriks, Baris, Kolom)
    Jordan(Matriks, Baris, Kolom, Aljabar)

# fungsi gauss (file uji)
def FolderTestGauss():
    Baris = kasus.ManyRow
    Kolom = kasus.ManyKolom
    Matriks = kasus.Matrix
    Aljabar = ["x{}".format(i + 1) for i in range(Kolom - 1)]
    print()
    print("Matriks")
    PrintMatriks(Matriks, Baris, Kolom)
    Gauss(Matriks, Baris, Kolom)

# fungsi gauss jordan (file uji)
def FolderTestJordan():
    Baris = kasus.ManyRow
    Kolom = kasus.ManyKolom
    Matriks = kasus.Matrix
    Aljabar = ["x{}".format(i + 1) for i in range(Kolom - 1)]
    print()
    print("Matriks")
    PrintMatriks(Matriks, Baris, Kolom)
    Gauss(Matriks, Baris, Kolom)
    Jordan(Matriks, Baris, Kolom, Aljabar)


def main():
    print("================= MENU ==================")
    print("1. Input dari keyboard (Eliminasi Gauss)")
    print("2. Input dari keyboard (Eliminasi Gauss-Jordan)")
    print("3. Input dari file (Eliminasi Gauss)")
    print("4. Input dari file (Eliminasi Gauss-Jordan)")
    Pilih = int(input("Masukan pilihan : "))
    print()
    
    # Jika pilih 1 maka akan mengeksekusi data dengan gauss
    if Pilih == 1:
        GS()
    # Jika pilih 2 maka akan mengeksekusi data dengan gauss-jordan
    elif Pilih == 2:
        GSJD()
    # Folder test eliminasi Gauss
    elif Pilih == 3:
        FolderTestGauss()
    # Folder test eliminasi Gauss-Jordan
    elif Pilih == 4:
        FolderTestJordan()
    else:
        print("Pilihan tidak terdapat dalam menu")

main()
