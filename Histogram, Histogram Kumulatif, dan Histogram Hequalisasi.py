import numpy as np #mengimport/memanggil library numpy
import imageio #mengimport library imageio
import matplotlib.pyplot as plt #mengimport library matplotlib

#membaca gambar
img = imageio.imread("mario.jpg") #membaca gambar yang diinputkan

img_height = img.shape[0] #mendapatkan dimensi ketinggian dalam gambar yang dimasukan
img_width = img.shape[1] #mendapatkan dimensi lebar dalam gambar yang dimasukan
img_channel = img.shape[2] #mendapatkan atau mengakses warna

#mengubah gambar menjadi grayscale
img_grayscale = np.zeros(img.shape, dtype=np.uint8) ##membuat variable horizontal untuk mengubah semua elemen array menjadi 0

for y in range(0, img_height): #variabel y dalam rentang 0 dalam dimensi ketinggian
    for x in range(0, img_width):#variabel x dalam rentang 0 dalam dimensi lebar
        red = img[y][x][0] 
        green = img[y][x][1]
        blue = img[y][x][2]
        gray = (int(red) + int(green) + int(blue)) / 3 #mengkonversi gambar menjadi grayscale
        img_grayscale[y][x] = (gray, gray, gray) 
        
plt.imshow(img_grayscale) #memanggil gambar yang sudah diinputkan
plt.title("Grayscale") 
plt.show() #menampilkan hasil gambar

#Menampilkan Histogram Gambar Grayscale
hg = np.zeros((256)) #Membuat variabel untuk menyimpan data gambar
for x in range(0, 256): #pengulangan dalam rentang 0-256
    hg[x] = 0 #mengisi nilai array dalam hg menjadi 0

#Menghitung nilai dari gambar
for y in range(0, img_height): #variabel x dalam rentang 0 dalam dimensi ketinggian
    for x in range(0, img_width): #variabel x dalam rentang 0 dalam dimensi lebar
        gray = img_grayscale[y][x][0] #Menghitung nilai dari gambar ke grayscale
        hg[gray] += 1 
        
#Menampilkan Histogram
bins = np.linspace(0, 256, 100) #mengelompokan data kepada bagian yang lebih kecil
plt.hist(hg, bins, color="black", alpha=0.5) #membuat grafik histogram 
plt.title("Histogram") #membuat judul
plt.show() #menampilkan hasil histogram

#==============Menampilkan Histogram Gambar RGB==============#
#Membuat variabel untuk menyimpan data gambar
hgr = np.zeros((256)) #menampilkan 1 baris array yang berisi 256 nilai 0 untuk histogram red
hgg = np.zeros((256)) #menampilkan 1 baris array yang berisi 256 nilai 0 untuk histogram green
hgb = np.zeros((256)) #menampilkan 1 baris array yang berisi 256 nilai 0 untuk histogram blue
hgrgb = np.zeros((768)) #menampilkan 1 baris array yang berisi 768 nilai 0 untuk histogram

#Mengisi setiap nilai dalam array hg dengan 0
for x in range(0, 256): #variable x dalam rentang 0 sampai 256
    hgr[x] = 0 
    hgg[x] = 0
    hgb[x] = 0
    
for x in range(0, 768): #variable x dalam rentang 0 sampai 768
    hgrgb[x] = 0
    
#Menghitung nilai dari gambar
for x in range(0, 256): #variable x dalam rentang 0 sampai 256
    hgr[x] = 0
    hgg[x] = 0
    hgb[x] = 0
    
for x in range(0, 768):#variable x dalam rentang 0 sampai 768
    hgrgb[x] = 0

# th = int(256/64)
temp = [0]
for y in range(0, img.shape[0]):#variable y dalam rentang 0 dan image shape untuk menampilkan bentuk 3 dimensi
    for x in range(0, img.shape[1]): #variable x dalam rentang 0 dan image shape untuk menampilkan bentuk 3 dimensi
        red = int(img[y][x][0]) #integer dari red
        green = int(img[y][x][1])  #integer dari green
        blue = int(img[y][x][2])  #integer dari blue
        green = green + 256 #konversi nilai green
        blue = blue + 512 #konversi nilai blue
#         temp.append(green)
        hgrgb[red] += 1 #menambah nilai baru
        hgrgb[green] += 1
        hgrgb[blue] += 1

binsrgb = np.linspace(0, 768, 100) #mengelompokan data kepada bagian yang lebih kecil dalam gambar rgb
plt.hist(hgrgb, binsrgb, color="black", alpha=0.5) #membuat grafik histogram
# plt.plot(hgrgb)
plt.title("Histogram Red Green Blue") #memberikan judul
plt.show() #menampilkan hasil grafik

#Menampilkan Histogram
for y in range(0, img_height): #variable y untuk ketinggian
    for x in range(0, img_width): #variable x untuk lebar
        red = img[y][x][0] #integer dari red
        green = img[y][x][1] #integer dari green
        blue = img[y][x][2] #integer dari blue
        hgr[red] += 1 #menambah nilai baru histogram red
        hgg[green] += 1 #menambah nilai baru histogram green
        hgb[blue] += 1 #menambah nilai baru histogram blue

bins = np.linspace(0, 256, 100) #mengelompokan data kepada bagian yang lebih kecil
plt.hist(hgr, bins, color="red", alpha=0.5) #membuat grafik histogram
plt.title("Histogram Red") #memberikan judul
plt.show() #menampilkan hasil grafik

plt.hist(hgg, bins, color="green", alpha=0.5) #membuat grafik histogram
plt.title("Histogram Green") #memberikan judul
plt.show() #menampilkan hasil grafik

plt.hist(hgb, bins, color="blue", alpha=0.5) #membuat grafik histogram
plt.title("Histogram Blue") #memberikan judul
plt.show() #menampilkan hasil grafik

#Menampilkan Histogram Kumulatif
hgk = np.zeros((256)) #menampilkan 1 baris array yang berisi 256 nilai 0 untuk histogram komulatif
c = np.zeros((256)) #variable c untuk berisi array nilai 0 sebanyak 256

for x in range(0, 256): #nilai x dalam range 0,256
    hgk[x] = 0
    c[x] = 0

for y in range(0, img_height):#nilai y untuk tinggi
    for x in range(0, img_width): #nilai x untuk lebar
        gray = img_grayscale[y][x][0] #Menghitung nilai dari gambar ke grayscale
        hgk[gray] += 1
                
c[0] = hgk[0]
for x in range(1, 256): #nilai x dalam range matriks 1 sampai 256
     c[x] = c[x-1] + hgk[x]

hmaxk = c[255]

for x in range(0, 256): #nilai x dalam range matriks 1 sampai 256
    c[x] = 190 * c[x] / hmaxk #konversi nilainya

plt.hist(c, bins, color="black", alpha=0.5) #membuat grafik histogram
plt.title("Histogram Grayscale Kumulatif") #memberikan judul
plt.show() #menampilkan hasil grafik

#Menampilkan Histogram Hequalisasi
hgh = np.zeros((256)) #menampilkan 1 baris array yang berisi 256 nilai 0 untuk histogram hequalisasi
h = np.zeros((256)) #variable h untuk 1 baris array yang berisi 256 nilai 0 untuk histogram hequalisasi
c = np.zeros((256)) #variable c untuk 1 baris array yang berisi 256 nilai 0 untuk histogram hequalisasi

for x in range(0, 256): #nilai x dalam range matriks 1 sampai 256
    hgh[x] = 0
    h[x] = 0
    c[x] = 0

for y in range(0, img_height): #nilai y untuk tinggi
    for x in range(0, img_width): #nilai x untuk lebar
        gray = img_grayscale[y][x][0] #Menghitung nilai dari gambar ke grayscale
        hgh[gray] += 1
                
h[0] = hgh[0]
for x in range(1, 256): #variable x dalam rentang 1-256
     h[x] = h[x-1] + hgh[x] #konversi histogram

for x in range(0, 256): #variable x dalam rentang 0-256
     h[x] = h[x] / img_height / img_width #konversi histogram

for x in range(0, 256): #variable x dalam rentang 0-256
    hgh[x] = 0 
    
for y in range(0, img_height): #variable nilai y untuk tinggi
    for x in range(0, img_width): #variable nilai x untuk lebar
        gray = img_grayscale[y][x][0] #Menghitung nilai dari gambar ke grayscale
        gray = h[gray] * 255
        hgh[int(gray)] += 1

c[0] = hgh[0]
for x in range(1, 256): #variable x dalam rentang 1 -256
     c[x] = c[x-1] + hgh[x] #konversi histogram

hmaxk = c[255] #nilai konversi histogram kumulatif

for x in range(0, 256): #variable x dalam rentang 0 -256
    c[x] = 190 * c[x] / hmaxk

plt.hist(c, bins, color="black", alpha=0.5) #memanggil dan membuat grafik histogram
plt.title("Histogram Grayscale Hequalisasi") #memberi judul
plt.show() #menampilkan hasil grafik gambarnya