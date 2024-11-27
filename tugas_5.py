# import numpy as np

# # def hewan():
# #     def hewan1():
# #         jenis= "angsa"
# #     def hewan2():
# #         nonlocal  jenis
# #         jenis = "harimau"
# #     def hewan3():
# #         global jenis
# #         jenis = "gajah"

# #     jenis = "ayam"
# #     hewan1()
# #     print(f"jenis hewan pertama {jenis}")
# #     hewan2()
# #     print(f"jenis hewan kedua {jenis}")
# #     hewan3()
# #     print(f"jenis hewan ketiga {jenis}")

# # hewan()
# # print(f"jenis hwan adalah {jenis}")


# # multi_array = np.array([['a','b','c'],[1,2,66],[4,5,6]])
# # # print(my_arra)


# # my_array = np.array([1,2,3,4,5])
# # newArr= multi_array[1,2]

# # multi_array[1,2] = 99
# # print(multi_array)



def hitung_IMT(weight, height):
    imt = weight / (height / 100) ** 2
    if imt < 18.5:
        return "Kurus"
    elif 18.5 <= imt < 25:
        return "Normal (Ideal)"
    elif 25 <= imt < 30:
        return "Kelebihan Berat Badan"
    else:
        return "Obesitas"

arr = []

while True:
    nama = input("Masukkan nama anda : ")
    bb = float(input("Masukkan berat badan anda : "))
    tb = float(input("Masukkan tinggi badan anda : "))
    
    arr.append({"nama": nama, "IMT": hitung_IMT(bb, tb)})
    
    retry = input("\nApakah anda ingin menghitung lagi ? y untuk Ya , n untuk Tidak : ")
    if retry in ['y','n']:
        if retry == 'n':
            print("Silahkan datang kembali ! ")
            break
    else :
        print("Input tidak valid , Silahkan kembali!")
        break
    

print("\n\nData yang tersimpan:")
for data in arr:
    print(f"\nNama: {data['nama']}, IMT: {data['IMT']}")
