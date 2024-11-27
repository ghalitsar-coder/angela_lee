nama =input("masukkan Nama : ")
sistolik =float(input("masukkan tekanan_darah :"))
diastolik =float(input("masukkan tekanan_darah :"))
denyut_nadi =float(input("masukkan denyut_nadi :"))

if sistolik > 180 and diastolik > 120 :
    kondisi = "rekomendasikan  pasien untuk segera mencari bantuan medis karena ini merupakan krisis hipertensi. "
else :
    kondisi ="cek tekanan darah"
    if sistolik > 140 and diastolik > 90 :
         kondisi = " sarankan untuk konsultasi  dengan dokter mengenai hipertensi. "
    elif 120 >= sistolik < 139 and 80 >= diastolik < 89:
        kondisi = " pasien berada dalam kategori prehipertensi.   "
        if denyut_nadi > 100 :
            kondisi = "  sarankan untuk memeriksa kondisi kesehatan jantung. "
        elif denyut_nadi < 60 :
            kondisi = "sarankan untuk memeriksa apakah ada gejala lain yang mengiringi bradikardia. "
        elif 60 >= denyut_nadi < 100 :
            kondisi = " denyut nadi mereka normal. "

print(f"nama: {Nama}, sistolik: {tekanan_darah }, diastolik:{tekanan_darah }, denyut_nadi:{denyut_nadi  },  kondisi akhir{kondisi}")