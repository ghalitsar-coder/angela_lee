try:
    # Input untuk memilih opsi konversi suhu
    option = int(
        input(
            "Masukkan Opsi mana yang akan dipilih (C ke F: 1, F ke C: 2, C ke K: 3): "
        )
    )
    
    # Input untuk suhu, dan coba konversi ke float
    temp = float(input("Masukkan temperature: "))
    
    # Inisialisasi variabel
    result = 0
    temp_name = []
    
    # Cek apakah opsi valid
    if option in [1, 2, 3]:
        if option == 1:
            result = (temp * 9 / 5) + 32
            temp_name.extend(["Celcius", "Fahrenheit"])
        elif option == 2:
            result = (temp - 32) * 5 / 9
            temp_name.extend(["Fahrenheit", "Celcius"])
        else:
            result = temp + 273.15
            temp_name.extend(["Celcius", "Kelvin"])
    else:
        # Jika opsi salah
        raise ValueError("Opsi salah, silakan masukkan 1, 2, atau 3.")
    
    # Cetak hasil konversi
    print(
        f"Temperature dari {temp_name[0]} di konversi menjadi {temp_name[1]} adalah {result}"
    )

# Tangani error jika input bukan angka untuk opsi
except ValueError as ve:
    print(f"Input tidak valid: {ve}")

# Tangani kesalahan yang tidak terduga
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
