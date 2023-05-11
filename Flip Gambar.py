import numpy as np #memanggil library numpy
import imageio #memanggil library imageio
import matplotlib.pyplot as plt #memanggil library matplotlib

img = imageio.imread("mario.jpg") #membaca gambar yang diupload 

img_height = img.shape[0]  # Mendapatkan dimensi tinggi dari gambar yang diinputkan
img_width = img.shape[1]  # Mendapatkan dimensi lebar dari gambar yang diinputkan
img_channel = img.shape[2]  # Mendapatkan jumlah saluran warna dalam gambar
img_type = img.dtype  # Mendapatkan tipe data dari gambar (misalnya, uint8, float32)


img_flip_horizontal = np.zeros(img.shape, img_type)  # Membuat variabel untuk menyimpan gambar yang dibalik secara horizontal, dengan semua elemen array diinisialisasi sebagai 0.
img_flip_vertical = np.zeros(img.shape, img_type)  # Membuat variabel untuk menyimpan gambar yang dibalik secara vertikal, dengan semua elemen array diinisialisasi sebagai 0.

for y in range(0, img_height):  # Melakukan iterasi untuk setiap baris (y) dalam dimensi tinggi gambar.
    for x in range(0, img_width):  # Melakukan iterasi untuk setiap kolom (x) dalam dimensi lebar gambar.
        for c in range(0, img_channel):  # Melakukan iterasi untuk setiap saluran warna (c) dalam gambar.
            img_flip_horizontal[y][x][c] = img[y][img_width-1-x][c]  # Membalikkan gambar secara horizontal dengan mengganti setiap piksel dengan piksel yang sesuai dari sisi kanan.

for y in range(0, img_height):  # Melakukan iterasi untuk setiap baris (y) dalam dimensi tinggi gambar.
    for x in range(0, img_width):  # Melakukan iterasi untuk setiap kolom (x) dalam dimensi lebar gambar.
        for c in range(0, img_channel):  # Melakukan iterasi untuk setiap saluran warna (c) dalam gambar.
            img_flip_vertical[y][x][c] = img[img_height-1-y][x][c]  # Membalikkan gambar secara vertikal dengan mengganti setiap piksel dengan piksel yang sesuai dari sisi bawah.

plt.imshow(img_flip_horizontal) #memanggil gambar yang sudah diinputkan dengan gambar horizontal
plt.title("Flip Horizontal")  #memberikan judul hasil plot di grafik
plt.show() #menampilkan gambar
plt.imshow(img_flip_vertical) #menampilkan gambar yang sidah diinputkan dengan gambar vertikal
plt.title("Flip Vertical") #memberi judul
plt.show() # menampilkan gambar dengan fungsi plot