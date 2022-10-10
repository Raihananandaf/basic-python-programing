# list buah
list_buah = ['pisang', 'nanas', 'melon', 'durian']

# print list
print('list_buah :' , list_buah)
print(list_buah [0:1])
print(list_buah [-1:0])
print(list_buah [0:3])

#ubah data pertama
list_buah[0] ='jeruk'

#ubah data terakhir
list_buah[3] = 'anggur'

print('list_buah :' , list_buah)

#list angka
list_angka = [1,2,3,4,5,6]
print('list_angka :', list_angka)

# fungsi pop() 
angka_yang_terhapus = list_angka.pop()
print('angka yang terhapus :', angka_yang_terhapus )


mystr = 'yes'
mystr += 'no'
mystr += 'yes'
print(mystr)

mystring = 'abcdefg'
print(mystring[2:5])

mystr = 'abc' * 3
print(mystr)