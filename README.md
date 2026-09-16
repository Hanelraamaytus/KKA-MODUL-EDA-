Analisis 1: Operasi NumPy Array vs List PythonHasil
[5000, 7000, 3000] * 0.9: Menghentikan program dengan pesan kesalahan (TypeError),karena List Python tidak bisa dikalikan secara langsung dengan tipe data desimal (float). 

Analisi 2 : Identifikasi data kosong & resiko
Kolom Kosong: Kolom menu pada indeks ke-4 dan kolom terjual pada indeks ke-2 mengandung nilai None.  Risiko Analisis: Mengolah data mentah ini secara langsung dapat menghasilkan agregasi statistik yang salah/bias, berisiko memicu error saat kalkulasi, dan menghasilkan laporan yang tidak berguna akibat adanya catatan transaksi tanpa nama menu. 

Analisis 3 : Interprstasi Output
Arti Indikator: Kolom dengan jumlah entitas non-null lebih sedikit dari total baris menandakan terdapat nilai hilang (missing value) atau sel kosong pada kolom tersebut.

Analisis 4 : Logika pembersihan data
Pengisian (fillna) pada terjual: Kolom numerik jumlah transaksi logis diganti angka 0, berasumsi bahwa tidak ada penjualan yang terjadi untuk item tersebut tanpa merusak perhitungan agregat.  
Penghapusan (dropna) pada menu: Nama menu merupakan variabel kategori utama. Data penjualan tanpa kejelasan nama produk tidak memiliki nilai analisis bisnis, sehingga barisnya lebih aman dibuang.

Analisis 5 : Dampak duplikat dan ketempatan Tipe data
Perubahan Baris: Jumlah baris berkurang dari 5 menjadi 4 karena satu baris data 'Es Teh' yang identik dibersihkan.  
Pentingnya dtypes: Memastikan fungsi agregasi numerik (seperti perkalian harga dan jumlah terjual) berjalan lancar. Jika kolom angka tersimpan dalam format teks (string/object), operasi aritmatika akan gagal atau hanya menggabungkan karakter

Analisis 6 : Agregasi data & pengambilan keputusan 
Pendapatan Tertinggi: Es Teh mendatangkan total pendapatan terbesar (Rp300.000 dari total 75 porsi x Rp4.000, melampaui Nasi Goreng sebesar Rp276.000).  
Dampak Keputusan: Pengelola kantin dapat memastikan stok bahan Es Teh selalu memadai, membuat paket hemat (bundling) Es Teh dengan makanan yang kurang laku, atau menambah varian minuman serupa.
