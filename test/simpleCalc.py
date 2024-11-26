print("1 - Tambah")
print("2 - Kurang")
print("3 - Kali")
print("4 - Bagi")
option = int(input("Pilih Operasi hitung : ") )

if (option in [1,2,3,4]):
    num1 = int(input("Pilih Nomor pertama : "))
    num2 = int(input("Pilih Nomor Kedua : "))
    
    if (option == 1):
        result = num1 + num2
    elif (option == 2):
        result = num1 - num2
    elif (option == 3):
        result = num1 * num2
    elif (option == 4):
        result = num1 // num2
    
else:
    print("Operasi hitung tidak ditemukan!")
    
print(f"Hasilnya ialah {result}")
    

        
        
         