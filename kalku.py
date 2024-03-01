def pertambahan(A,B):
    print("Hasil dari", A , "+", B , "=", A+B)
def pengurangan(A,B):
    print("Hasil dari", A , "-", B , "=", A-B)
def perkalian(A,B):
    print("Hasil dari", A , "x", B , "=", A*B)
def pembagian(A,B):
    if B == 0:
        print("ERROR!!!")
    else:
        print("Hasil dari", A , ":", B , "=", A/B)
while True:
    print("Selamat Datang dalam Aplikasi Kalkulator")
    enter = input("Silahkan tekan enter untuk melanjutkan")
    print("\n=====================")
    print(" KALKULATOR PROGRAM ")
    print("=====================\n")
    print("------ Input Angka -------")
    A = int(input("Angka pertama : "))
    B = int(input("Angka kedua : "))
    print("\n------ Operasi -------")
    print("1. Pertambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")
    pilih = input("Masukkan pilihan : ")
    print("\n------ Output -------")
    if pilih == '1':
        pertambahan(A,B)
    elif pilih == '2':
        pengurangan(A,B)
    elif pilih == '3':
        perkalian(A,B)
    elif pilih == '4':
        pembagian(A,B)
    elif pilih == '5':
        break
    else:
        print("Pilihan tidak valid")
    print("---------------------")