# Praktikum-Tegraf-C10
### Anggota kelompok
| Nama | NRP |
| --- | --- |
| Hanif Aqil Janardana | 5025241111 |
| Rafa Huga Nirando | 5025241114 |
| Felix Aldorino | 5025241162 |

## The Knight's Tour

<br>

## Largest Monotonically Increasing Subsequence

### Cara Kerja
Program ini menggunakan Binary Search Tree untuk mencari sequence paling besar. Setiap kali sebuah bilangan baru dimasukkan ke dalam tree, akan langsung mencari apakah bilangan tersebut termasuk dalam sebuah sequence atau awal dari sequence baru yang akan disimpan dalam node tersebut. Setiap ada bilangan baru, root akan mengecek jika ada Largest Monotonically sequence yang baru. Fungsi cek sequence akan membandingkan nilai dari sebuah node dengan nilai bilangan yang baru. Jika nilai node sekarang lebih kecil dari bilangan yang baru, fungsi akan melakukan pengecekan terhadap node di kanannya kemudian melakukan pengecekan sequence dari node di kirinya. Jika tidak akan langsung mengecek sequence dari node dikirinya. Fungsi akan mereturn sequence paling besar di akhir fungsi yang akhirnya akan di simpan di node root. 

### Input
Sebuah array dari bilangan bulat yang dipisahkan spasi dan diakhiri dengan enter

### Output
Sebuah sequence yang berisi Largest Monotonically Inreasing Sequence yang pertama kali ditemukan jika ada beberapa sequence dengan panjang yang sama. Contoh:

Sequence [2, 1, 3, 4] akan menghasilkan [2, 3, 4]
