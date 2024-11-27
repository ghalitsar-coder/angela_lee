import numpy as np
import matplotlib.pyplot as plt
import time
from collections import deque

def create_mushroom_boundary(grid_size_x=15, grid_size_y=15):
    # Inisialisasi grid kosong
    grid = np.zeros((grid_size_y, grid_size_x))
    
    # Membuat bentuk jamur (10x8)
    # Kepala jamur
    # Garis horizontal atas (lebar 8)
    for i in range(3, 11):
        grid[2][i] = 1
    
    # Garis horizontal bawah kepala yang terhubung dengan batang
    for i in range(3, 5):  # sisi kiri
        grid[5][i] = 1
    for i in range(9, 11):  # sisi kanan
        grid[5][i] = 1
    
    # Garis vertikal kiri kepala
    for i in range(2, 6):
        grid[i][2] = 1
    
    # Garis vertikal kanan kepala
    for i in range(2, 6):
        grid[i][11] = 1
    
    # Batang jamur
    # Garis vertikal kiri batang
    for i in range(5, 12):
        grid[i][5] = 1
    
    # Garis vertikal kanan batang
    for i in range(5, 12):
        grid[i][8] = 1
    
    # Garis horizontal bawah batang
    for i in range(5, 9):
        grid[11][i] = 1
    
    return grid

def plot_current_state(grid, title):
    plt.clf()
    colors = ['white', 'black', 'red']
    cmap = plt.matplotlib.colors.ListedColormap(colors)
    
    plt.imshow(grid, cmap=cmap)
    plt.grid(True, color='gray', linewidth=0.5, alpha=0.5)
    plt.xticks(range(15))
    plt.yticks(range(15))
    plt.title(title)
    plt.draw()
    plt.pause(0.5)

def boundary_fill_8(grid, start_x, start_y, fill_value, boundary_value):
    if grid[start_x][start_y] == boundary_value or grid[start_x][start_y] == fill_value:
        return
    
    # Menggunakan queue untuk implementasi non-recursive
    queue = deque([(start_x, start_y)])
    
    # Definisi 8 arah tetangga
    neighbors_8 = [
        (-1, 0),  # atas
        (1, 0),   # bawah
        (0, -1),  # kiri
        (0, 1),   # kanan
        (-1, -1), # diagonal kiri atas
        (-1, 1),  # diagonal kanan atas
        (1, -1),  # diagonal kiri bawah
        (1, 1)    # diagonal kanan bawah
    ]
    
    while queue:
        x, y = queue.popleft()
        
        if (x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])):
            continue
            
        if grid[x][y] == boundary_value or grid[x][y] == fill_value:
            continue
            
        # Fill current pixel
        grid[x][y] = fill_value
        plot_current_state(grid, f"Proses Pengisian (x={x}, y={y})")
        time.sleep(0.5)
        
        # Tambahkan semua tetangga valid ke queue
        for dx, dy in neighbors_8:
            next_x, next_y = x + dx, y + dy
            if (0 <= next_x < len(grid) and 
                0 <= next_y < len(grid[0]) and 
                grid[next_x][next_y] != boundary_value and 
                grid[next_x][next_y] != fill_value):
                queue.append((next_x, next_y))

def boundary_fill_4(grid, start_x, start_y, fill_value, boundary_value):
    if grid[start_x][start_y] == boundary_value or grid[start_x][start_y] == fill_value:
        return
    
    queue = deque([(start_x, start_y)])
    
    # Definisi 4 arah tetangga
    neighbors_4 = [
        (-1, 0),  # atas
        (1, 0),   # bawah
        (0, -1),  # kiri
        (0, 1)    # kanan
    ]
    
    while queue:
        x, y = queue.popleft()
        
        if (x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])):
            continue
            
        if grid[x][y] == boundary_value or grid[x][y] == fill_value:
            continue
            
        # Fill current pixel
        grid[x][y] = fill_value
        plot_current_state(grid, f"Proses Pengisian (x={x}, y={y})")
        time.sleep(0.5)
        
        # Tambahkan semua tetangga valid ke queue
        for dx, dy in neighbors_4:
            next_x, next_y = x + dx, y + dy
            if (0 <= next_x < len(grid) and 
                0 <= next_y < len(grid[0]) and 
                grid[next_x][next_y] != boundary_value and 
                grid[next_x][next_y] != fill_value):
                queue.append((next_x, next_y))

# Set up plot
plt.figure(figsize=(8, 8))

# Buat dan tampilkan grid awal
grid = create_mushroom_boundary()
plot_current_state(grid, "Outline Jamur (Hitam)")
plt.pause(2)

# Tanyakan user ingin menggunakan 4-connected atau 8-connected
print("Pilih metode pengisian:")
print("1. 4-connected")
print("2. 8-connected")
choice = input("Masukkan pilihan (1/2): ")

# Mulai proses pengisian
print("Mengisi jamur...")
if choice == "1":
    boundary_fill_4(grid, 3, 6, 2, 1)
else:
    boundary_fill_8(grid, 3, 6, 2, 1)

# Tampilkan hasil akhir
plot_current_state(grid, "Hasil Akhir")
plt.show()

print("Proses pengisian warna selesai!")