# Pertemuan 11 - CONSTRUCT dan Hierarki Data

## Langkah 1 - Solution menjadi triple
| Solution | ?d | ?mk | Triple yang dicetak |
|----------|----|-----|---------------------|
| [isi]    | [isi] | [isi] | [isi]           |
- Jumlah solution: [isi]
- Jumlah cetakan triple: [isi]
- Jumlah triple di graf hasil: [isi]
- Triple yang tercetak lebih dari sekali: [isi]

## Langkah 2 - Tebak lalu cek
| Soal | Tebakan | Hasil mesin | Penjelasan bila meleset |
|------|---------|-------------|-------------------------|
| A    | 3 baris   | 3 baris       | tidak meleset. Hasil mencakup DosenTetap, DosenTamu, dan Dosen                   |
| B    | 3 baris   | 4 baris       | tidak meleset. Sari muncul dua kali karena memiliki dua tipe, yaitu DosenTetap dan DosenTamu                   |
| C    | 3 triple   | 3 triple       | tidak meleset. CONSTRUCT menghasilkan tiga triple Pegawai untuk Budi, Sari, dan Rudi                   |
| D    | 0 triple   | 0 triple       | tidak meleset. Variabel ?n tidak terikat karena Rudi tidak memiliki ex:nama, sehingga triple tidak dibuat tanpa pesan error                   |

Saya kira setiap individu hanya muncul satu kali. Ternyata Sari muncul dua kali karena memiliki dua tipe, yaitu DosenTetap dan DosenTamu.

## Langkah 3 - Graf kampus lokal
- Berkas sumber dan IRI dasar graf: pertemuan-09/kampus_usu_v2.ttl dengan IRI dasar https://contoh.github.io/web-semantik/251402113/kampus#.
- Kelas dosen dan properti nama: ex:Lecturer dan foaf:name.
- Triple hasil pemetaan: 2 triple, yaitu pemetaan individu dosen ex:ida menjadi schema:Person dan pemetaan namanya menjadi schema:name.
- foaf:Person sebelum / sesudah: 0 / 1
- Triple asli vs triple turunan: Triple asli merupakan triple yang sudah tersedia di graf sumber, sedangkan triple turunan merupakan triple baru yang dihasilkan melalui hierarki kelas. Pada proses ini, ex:ida memperoleh tipe ex:Pegawai dan foaf:Person melalui hierarki ex:Lecturer -> ex:Pegawai -> foaf:Person.
- Dosen baru setelah program selesai: Dosen baru tidak otomatis memperoleh tipe foaf:Person karena proses materialisasi hanya dilakukan ketika program dijalankan. Untuk memasukkan dosen baru ke dalam hasil inferensi, graf harus diperbarui dan program dijalankan kembali.

## Langkah 4 - Wikidata
- Jumlah triple Q6: [142]
- Jumlah baris Q6 versi SELECT: [50]
- Penjelasan perbedaan:
1.Bentuk keluaran berbeda.
 SELECT menghasilkan tabel (baris dan kolom), sedangkan CONSTRUCT menghasilkan graf RDF, yaitu kumpulan triple subjek-predikat-objek yang dibentuk dari template di blok CONSTRUCT { ... }.

2.Satu baris menghasilkan tiga triple. Template CONSTRUCT berisi tiga pola: ?univ a ex:Universitas, ?univ ex:nama ?nama, dan ?univ ex:lokasi ?kota. Jadi setiap baris solusi dari WHERE menghasilkan hingga 3 triple. Dengan 50 baris, maksimalnya 150 triple.

3.Graf RDF adalah himpunan, sehingga triple identik hanya dihitung sekali. Dari 50 baris hanya ada 46 universitas unik. Beberapa universitas muncul di lebih dari satu baris karena punya lebih dari satu nilai ?kota (properti wdt:P131).

- Q7 dengan + vs *:
Pada Q7, operator wdt:P279+ dan wdt:P279* sama-sama menelusuri rantai relasi subclass of dari Q3918 (universitas), tetapi berbeda pada batas langkahnya. Operator + berarti satu langkah atau lebih sehingga hanya menghasilkan kelas turunan (subkelas) universitas, sedangkan * berarti nol langkah atau lebih sehingga selain semua subkelas, hasilnya juga menyertakan Q3918 itu sendiri karena nol langkah berarti dirinya sendiri. Dengan kata lain, himpunan hasil * sama dengan himpunan hasil + ditambah satu elemen, yaitu Q3918. Pada percobaan ini, kedua query menampilkan 30 baris yang berbeda isinya (misalnya university in Manitoba dan Early decision pada +, serta Jesuit university dan junior college in Japan pada *) karena memakai LIMIT 30 tanpa ORDER BY, sementara jumlah subkelas universitas di Wikidata jauh lebih banyak dari 30, sehingga yang tampil hanyalah cuplikan acak dan Q3918 tidak kebetulan muncul pada hasil *.
- Kelas yang mengejutkan dan alasannya: 

kelas yang mengejutkan:Early decision (Q5326799)
alasan:
Early decision adalah skema penerimaan mahasiswa (daftar lebih awal dan wajib mendaftar bila diterima), bukan jenis universitas.
Subkelas universitas seharusnya berupa jenis lembaga, misalnya technological university. Sebuah early decision bukan universitas.
Operator + menelusuri P279 secara transitif, jadi satu pernyataan subclass of yang terlalu longgar di tengah rantai sudah membuat kelas ini ikut terhitung sebagai subkelas universitas.
Kemungkinan penyebabnya adalah kesalahan pemodelan di Wikidata (over-generalized subclass link).

## Langkah 5 - Graf dari Python
- Jumlah triple universitas.ttl: [isi]
- Jumlah baris universitas_per_kota.csv: [isi]
- setReturnFormat(TURTLE): [isi]
- Graph().parse(data=...): [isi]
- Mengapa q_kota tidak memanggil endpoint: [isi]

## Refleksi
1. Mengapa jumlah triple hasil CONSTRUCT bisa lebih kecil dari jumlah baris SELECT dengan WHERE yang sama?
2. Bila taksonomi di graf kampus Anda berubah bulan depan, apa yang terjadi pada triple turunan di kampus_usu_v4.ttl?
3. Kapan Anda menyimpan hasil query sebagai tabel (CSV), dan kapan sebagai graf (Turtle)?