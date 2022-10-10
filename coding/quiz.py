
from ast import If


def program_hitung():
    print('Rumus Bangun')
    print('1. Persegi Panjang')
    print('2. Lingkaran')
  

    a = int(input('Pilih Bangun [1..2]: ')) 

def persegi_panjang():
    panjang = float(input("masukan panjang :"))
    lebar   = float(input("masukan lebar:"))
    luas = panjang * lebar
    keliling = 2*(panjang + lebar)
    print("Keliling Persegi Panjang : ",keliling)
    print("Luas Persegi Panjang : ",luas)

def lingkaran():
    phi = 3.14

    r = input("Masukan Nilai Jari jari :")
    keliling2 = 2*phi*float(r)
    luas2 = phi*float(r)*float(r)
    print("Keliling Lingkaran : ",keliling2)
    print("Luas Lingkaran : ",luas2)
    
    return luas2

if  a == 1:
    persegi_panjang()
elif a== 2:
    lingkaran

  
a = input("Hitung lagi [y/t]: ")
while a == 'y':
        program_hitung()
        break













    

