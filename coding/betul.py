# Fungsi in melakukan validasi password
def validasi_password(passwd):
    spesial_karakter = ['$', '@', '#', '%']
    
    # Variabel-variabel untuk menyimpan hasil pengujian ketentuan. Inisialisasi dengan False.
    panjang_benar = False
    ada_digit = False
    ada_huruf_besar = False
    ada_huruf_kecil = False
    ada_spesial_karakter = False
	
	# [1] Mulai validasi dengan uji panjang karakter
    # Untuk menguji adanya digit, huruf besar, huruf kecil, dan spesial karakter, gunakan loop yang mengiterasi passwd
    if len(passwd) > 6 and len(passwd) < 20:
        for i in passwd:
            if i.isdigit():
                ada_digit = True
                
            if i.isupper():
                ada_huruf_besar = True
                
            if i.islower():
                ada_huruf_kecil = True
            
            if i == '$' or i == '@' or i == '#' or i == '%':
                ada_spesial_karakter = True
                
                
	       
    # [2] Jika semua ketentuan terpenuhi tetapkan sebuah varibel untuk nilai kembali dengan True
    # dan selain itu tetapkan dengan False
    if ada_digit and ada_huruf_besar and ada_huruf_kecil and ada_spesial_karakter:
        return True
    else:
        return False


    # [3] Kembalikan variabel nilai kembali yang didapatrkan dari [2]