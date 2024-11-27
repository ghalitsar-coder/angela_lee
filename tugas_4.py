kondisi = ""
kondisiDn = ""

retry = 0
while retry < 3:
    nama = input("Masukkan nama : ")
    tds = int(input("Masukkan Tekanan darah sistolik : "))
    tdd = int(input("Masukkan Tekanan darah diastolik : "))
    if tds > 180 or tdd > 120:
        kondisi = (
            "Tolong segera mencari bantuan medis karena ini merupakan krisis hipertensi"
        )
    else:
        if tds > 140 or tdd > 90:
            kondisi = "Tolong segera konsultasi dengan dokter mengenai hipertensi"
        elif 120 <= tds <= 139 or 80 <= tdd <= 89:
            kondisi = "Anda menderita hipertensi "
        else:
            kondisi = "Tekanan darah anda normal"
            dn = int(input("Masukkan  Denyut nadi : "))
            if dn > 100:
                kondisiDn = "Anda disarankan untuk memeriksa kesehatan jantung anda"
            elif 60 <= dn <= 100:
                kondisiDn = "Denyut nadi anda masih normal"
            else:
                kondisiDn = "Apakah ada gejala lain yang mengiringi bradikardia ?"
    isDnExist = f"\nHasil Denyut nadi anda :  {kondisiDn}" if kondisiDn else ""
    print(f"Nama: {nama}\nHasil Tekanan Darah: {kondisi}{isDnExist}\n\n")
    if not retry == 2:
        question_retry = input(
            "Masih ingin diperiksa ? y/Y untuk Ya dan n/N untuk Tidak "
        )
        if question_retry.lower() == "y":
            retry += 1
            kondisi = ""
            print("\n\n")
        elif question_retry.lower() == "n":
            print("Silahkan datang kembali")
            retry = 3
            kondisi = ""
        else:
            print("Jawaban tidak valid, tolong ulangi pemeriksaan")
            continue
    else:
        print("Silahkan datang kembali")
        retry = 3
