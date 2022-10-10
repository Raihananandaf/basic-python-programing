#TIPE DATA SET

from winreg import REG_DWORD_BIG_ENDIAN


himpunan_siswa = {'himti', 'himsw', 'himkom', 'himsi'}
print(himpunan_siswa)

set_campuran = {'manusia', 'hewan', 5 , True, ('a', 'b')}
print(set_campuran)

himpunan_buah = set({'apel', ' jeruk', 'mangga'})
print(himpunan_buah)

#unchangable
himpunan = {'maya', 'budi', 100, ('a','b'), False, True}
himpunan.remove(100)
print(himpunan)

#anggota data set dengan perulangan
himpunan_buah = { 'pepaya', 'apel','jagung', 'rambuatan'}

for buah in himpunan_buah:
    print(buah)

#dictionary

buku  = {'judul': 'Hafalan solat delisa', 'penulis' : 'Tere liye'}

for key in buku:
    print(key, '- >', buku[key])