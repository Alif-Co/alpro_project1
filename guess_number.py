
def guess_number():
    secret_number = 9
    guess = 0
    guess_limit = 3
    
    while guess < guess_limit:
        user = int(input('[:] Masukkan Angka : '))
        if user == secret_number:
            print("[!] Selamat! Anda berhasil menemukan Angkanya")
            break
        
        else:
            print('Salah!')
            guess += 1
            
    else:
        print(f'[!] Gagal, angkanya adalah = {secret_number}')
        
guess_number()