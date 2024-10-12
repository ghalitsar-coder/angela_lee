

usia = int(input("Masukkan usia anda "))

laki_laki  = 0;
perempuan = 0;

if not usia < 3:
    
        jenis_kelamin  = input("Masukkan Jenis kelamin anda L untuk laki-laki P untuk Perempuan ")
        if jenis_kelamin in ['L','P']:

            if  3 <= usia <18:
                laki_laki = 1.6
                perempuan = 1.4
            elif 18 <= usia < 64:
                laki_laki = 1.8
                perempuan = 1.6
            else : 
                laki_laki = 2.0
                perempuan = 1.8

            my_gender = laki_laki if jenis_kelamin == "L" else perempuan
            print(f"Usia saya {usia}  tahun , dan rekomendasi asupan air untuk saya adalah {my_gender}")
            
        else :
            print("Jenis kelamin tidak ditemukan")
else:
        print("Masih diberi asi ")
    

