# Praktikum-Tegraf-C10
### Anggota kelompok
| Nama | NRP |
| --- | --- |
| Hanif Aqil Janardana | 5025241111 |
| Rafa Huga Nirando | 5025241114 |
| Felix Aldorino | 5025241162 |

## The Knight's Tour ( OPEN )

### Cara Kerja :

Program ini menyelesaikan persoalan Knight’s Tour pada papan catur 8×8 menggunakan algoritma Warnsdorff’s Rule. Dengan  tujuan sehingga setiap kotak dikunjungi tepat satu kali oleh Knight.

Algoritma mulai dengan menandai kotak awal sebagai langkah pertama. Pada setiap langkah berikutnya, program mencari semua kotak yang bisa dicapai knight. Untuk setiap kotak kandidat tersebut, dihitung berapa banyak langkah lanjutan yang mungkin dari kotak tersebut (degree).

Warnsdorff’s Rule menyatakan bahwa knight harus bergerak ke kotak yang memiliki degree paling kecil, karena kotak yang memiliki sedikit pilihan lanjutan sebaiknya dikunjungi lebih awal untuk menghindari kebuntuan.

### Input 

Sepasang Bilangan Bulat yang dimasukkan terpisah untuk Koordinat X dan Y

### Output 
Sebuah Map yang memperlihatkan perjalanan Knight mengelilingi papan catur

Contoh : Input (x,y) = (4,2) 

<img width="291" height="293" alt="image" src="https://github.com/user-attachments/assets/7a5ac04f-ae6e-4f52-91c6-b6d883543731" />



## The Knight's Tour ( Closed )

### Cara Kerja :

Program ini mencari closed knight’s tour pada papan catur 8×8, yaitu rute langkah kuda yang kembali lagi ke kotak awal setelah mengunjungi semua kotak sekali. Algoritma yang digunakan adalah Depth-First Search (DFS) dengan bantuan Warnsdorff’s Rule, yaitu memilih langkah dengan derajat (jumlah opsi langkah berikutnya) yang paling kecil untuk mengurangi kemungkinan buntu.

Pertama, program meminta user memasukkan koordinat awal kuda. Namun, dalam proses pencarian, algoritma selalu memulai dari posisi tetap yaitu (3,3) karena titik ini paling stabil untuk menemukan closed tour. Setelah closed tour ditemukan, program melakukan rotasi jalur sehingga urutan langkah dimulai dari koordinat yang dimasukkan user.

Setiap langkah dicari dengan fungsi ordered_moves, yaitu daftar langkah yang sudah diurutkan berdasarkan derajat terkecil. Ketika DFS menemukan kotak terakhir (movei == 63), program mengecek apakah kuda bisa kembali ke posisi awal (closed condition). Jika bisa, rute valid telah ditemukan.

Setelah rute ditemukan, program menyusun ulang rute agar urutannya dimulai dari titik yang diinput user. Kemudian program membuat mapping closed tour dan mengisi nomor langkah dari 0 hingga 63 sesuai rute yang sudah diputar.

### Input 
Sepasang Bilangan Bulat yang dimasukkan terpisah untuk Koordinat X dan Y

### Output 
Sebuah Map yang memperlihatkan perjalanan Knight mengelilingi papan catur

Contoh : untuk (x,y) = (3,7), output adalah

<img width="355" height="274" alt="image" src="https://github.com/user-attachments/assets/1f0a2a52-4e41-45f0-9da4-3d8e1391a553" />


<br>

## Largest Monotonically Increasing Subsequence

### Cara Kerja
Program ini menggunakan Binary Search Tree untuk mencari sequence paling besar. Setiap kali sebuah bilangan baru dimasukkan ke dalam tree, akan langsung mencari apakah bilangan tersebut termasuk dalam sebuah sequence atau awal dari sequence baru yang akan disimpan dalam node tersebut. Setiap ada bilangan baru, root akan mengecek jika ada Largest Monotonically sequence yang baru. Fungsi cek sequence akan membandingkan nilai dari sebuah node dengan nilai bilangan yang baru. Jika nilai node sekarang lebih kecil dari bilangan yang baru, fungsi akan melakukan pengecekan terhadap node di kanannya kemudian melakukan pengecekan sequence dari node di kirinya. Jika tidak akan langsung mengecek sequence dari node dikirinya. Fungsi akan mereturn sequence paling besar di akhir fungsi yang akhirnya akan di simpan di node root. 

### Input
Sebuah array dari bilangan bulat yang dipisahkan spasi dan diakhiri dengan enter

### Output
Sebuah sequence yang berisi Largest Monotonically Inreasing Sequence yang pertama kali ditemukan jika ada beberapa sequence dengan panjang yang sama. Contoh:

<img width="555" height="57" alt="image" src="https://github.com/user-attachments/assets/1d9e932c-87bd-4d1b-beb7-78911949c3af" />

