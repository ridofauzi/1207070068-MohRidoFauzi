import numpy as np #memanggil library numpy
import imageio #memanggil library imageio
import matplotlib.pyplot as plt #mengimport library matplotlib

# Membaca gambar
img = imageio.imread("mario.jpg")  # Membaca gambar yang diinputkan

img_height = img.shape[0]  # Mendapatkan dimensi ketinggian dalam gambar yang dimasukkan
img_width = img.shape[1]  # Mendapatkan dimensi lebar dalam gambar yang dimasukkan
img_channel = img.shape[2]  # Mendapatkan atau mengakses warna/saluran

# Membuat variabel img_inversi
img_inversi = np.zeros(img.shape, dtype=np.uint8)  # Membuat variabel untuk menyimpan hasil inversi gambar menjadi png,
                                                  # dengan semua elemen array diinisialisasi sebagai 0

# Membuat fungsi untuk inversi grayscale
def inversi_grayscale(nilai):
    for y in range(0, img_height):  # Iterasi untuk setiap baris (y) dalam dimensi tinggi gambar
        for x in range(0, img_width):  # Iterasi untuk setiap kolom (x) dalam dimensi lebar gambar
            red = img[y][x][0]  # Mendapatkan nilai saluran merah (red)
            green = img[y][x][1]  # Mendapatkan nilai saluran hijau (green)
            blue = img[y][x][2]  # Mendapatkan nilai saluran biru (blue)
            gray = (int(red) + int(green) + int(blue)) / 3  # Menghitung rata-rata saluran RGB untuk mendapatkan grayscale
            gray = nilai - gray
            img_inversi[y][x] = (gray, gray, gray)  # Menghasilkan inversi gambar menjadi grayscale

# Membuat fungsi untuk inversi RGB
def inversi_rgb(nilai):
    for y in range(0, img_height):  # Iterasi untuk setiap baris (y) dalam dimensi tinggi gambar
        for x in range(0, img_width):  # Iterasi untuk setiap kolom (x) dalam dimensi lebar gambar
            red = img[y][x][0]  # Mendapatkan nilai saluran merah (red)
            red = nilai - red
            green = img[y][x][1]  # Mendapatkan nilai saluran hijau (green)
            green = nilai - green
            blue = img[y][x][2]  # Mendapatkan nilai saluran biru (blue)
            blue = nilai - blue
            img_inversi[y][x] = (red, green, blue)  # Menghasilkan inversi gambar pada saluran RGB
            
#Menampilkan hasil inversi
inversi_grayscale(255) #inversi untuk grayscale
plt.imshow(img_inversi) #memanggil gambar yang sudah dikonversi
plt.title("Inversi Grayscale") #membuat judul
plt.show() #menampilkan hasilnya

inversi_rgb(255) #inversi untuk rgb
plt.imshow(img_inversi) #memanggil gambar yang sudah dikonversi
plt.title("Inversi RGB")  #membuat judul
plt.show() #menampilkan hasilnya

#==================Log====================#

#Membuat variabel img_log untuk menampung hasil
img_log = np.zeros(img.shape, dtype=np.uint8)

#Mendefinisikan fungsi untuk log
def log(c): #blok program fungsi log
    for y in range(0, img_height): #variable y untuk tinggi
        for x in range(0, img_width): #variable x untuk lebar
            red = img[y][x][0] #konversi channel red rata rata
            green = img[y][x][1] #konversi channel green rata-rata
            blue = img[y][x][2] #konversi channel blue rata-rata
            gray = (int(red) + int(green) + int(blue)) / 3 #konversi channel menjadi grayscale dari rata-rata RGB
            gray = int(c * np.log(gray + 1)) #konversi menggunakan rumus log
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_log[y][x] = (gray, gray, gray) #hasil dari log menjadi gray
#Menampilkan hasil log
log(30) #hasil log
plt.imshow(img_log) #memanggil gambar yang sudah dikonversi
plt.title("Log") #membuat judul
plt.show() #menampilkan hasilnya dari konversi ke log

#===============Inversi & Log============#
#Membuat variabel img_inlog untuk menampung hasil
img_inlog = np.zeros(img.shape, dtype=np.uint8)
#Mendefinisikan fungsi untuk inversi log
def inlog(c): #definisi fungsi untuk inversi log
    for y in range(0, img_height): #variable y untuk tinggi
        for x in range(0, img_width): #variable x untuk lebar
            red = img[y][x][0] #konversi channel red rata rata
            green = img[y][x][1] #konversi channel green rata-rata
            blue = img[y][x][2] #konversi channel blue rata-rata
            gray = (int(red) + int(green) + int(blue)) / 3 #konversi channel menjadi grayscale dari rata-rata RGB
            gray = int(c * np.log(255 - gray + 1)) #konversi menggunakan rumus log
            if gray > 255: #memasukan variable nilai jika lebih kecil dari 255
                gray = 255
            if gray < 0: #memasukan variable nilai jika nilai sama dengan 0
                gray = 0
            img_inlog[y][x] = (gray, gray, gray) #hasil dari log menjadi gray
#Menampilkan hasil inversi log
inlog(30) #hasil inversi log
plt.imshow(img_inlog) #memanggil gambar yang sudah dikonversi
plt.title("Inversi & Log") #membuat judul
plt.show() #menampilkan hasilnya dari konversi ke log

#Nth Power
#Membuat variabel img_nthpower untuk menampung hasil
img_nthpower = np.zeros(img.shape, dtype=np.uint8)
#Mendefinisikan fungsi untuk nth power
def nthpower(c, y): #definisi fungsi untuk nth power
    thc = c / 100 
    thy = y / 100
    for y in range(0, img_height): #variable y untuk tinggi
        for x in range(0, img_width): #variable x untuk lebar
            red = img[y][x][0] #konversi channel red rata rata
            green = img[y][x][1] #konversi channel green rata-rata
            blue = img[y][x][2] #konversi channel blue rata-rata
            gray = (int(red) + int(green) + int(blue)) / 3 #konversi channel menjadi grayscale dari rata-rata RGB
            gray = int(thc * pow(gray, thy)) #konversi menggunakan rumus nth power
            if gray > 255: #memasukan variable nilai jika lebih kecil dari 255
                gray = 255
            if gray < 0: #memasukan variable nilai jika nilai sama dengan 0
                gray = 0
            img_nthpower[y][x] = (gray, gray, gray) #hasil dari log menjadi nthpower
#Menampilkan hasil
nthpower(50, 100) #hasil dengan matriks range 50,100
plt.imshow(img_nthpower) #memanggil gambar yang sudah dikonversi
plt.title("Nth Power") #membuat judul
plt.show() #menampilkan hasilnya dari konversi ke log

#Nth Root Power
#Membuat variabel img_nthrootpower
img_nthrootpower = np.zeros(img.shape, dtype=np.uint8)
#Membuat fungsi untuk nth root power
def nthrootpower(c, y): #definisi fungsi untuk nth root power
    thc = c / 100
    thy = y / 100
    for y in range(0, img_height): #variable y untuk tinggi
        for x in range(0, img_width): #variable x untuk lebar
            red = img[y][x][0] #konversi channel red rata rata
            green = img[y][x][1] #konversi channel green rata-rata
            blue = img[y][x][2] #konversi channel blue rata-rata
            gray = (int(red) + int(green) + int(blue)) / 3 #konversi channel menjadi grayscale dari rata-rata RGB
            gray = int(thc * pow(gray, 1./thy)) #konversi menggunakan rumus nth root power
            if gray > 255: #memasukan variable nilai jika lebih kecil dari 255
                gray = 255
            if gray < 0: #memasukan variable nilai jika nilai sama dengan 0
                gray = 0
            img_nthpower[y][x] = (gray, gray, gray) 
#Menampilkan hasil
nthrootpower(50, 100) #hasil dengan matriks range 50,100
plt.imshow(img_nthrootpower) #memanggil gambar yang sudah dikonversi
plt.title("Nth Root Power") #membuat judul
plt.show() #menampilkan hasilnya dari konversi ke log