tahun = int(input('Input Tahun: '))
def kabisat (tahun_1):
    if tahun_1%4==0:
        print("Hasil: TAHUN KABISAT")        
    else:
        print("Hasil: BUKAN TAHUN KABISAT")
kabisat(tahun)