# Pertemuan 11 - CONSTRUCT dan Hierarki Data

## Langkah 1 - Solution menjadi triple

| Solution | ?d | ?mk | Triple yang dicetak |
|----------|----|-----|---------------------|
| 1 | ex:budi | ex:tif2108 | ex:tif2108 a ex:MataKuliahAktif; ex:tif2108 ex:diampuOleh ex:budi |
| 2 | ex:budi | ex:tif2104 | ex:tif2104 a ex:MataKuliahAktif; ex:tif2104 ex:diampuOleh ex:budi |
| 3 | ex:sari | ex:tif2108 | ex:tif2108 a ex:MataKuliahAktif; ex:tif2108 ex:diampuOleh ex:sari |
| 4 | ex:ida | ex:tif2104 | ex:tif2104 a ex:MataKuliahAktif; ex:tif2104 ex:diampuOleh ex:ida |

- Jumlah solution: 4
- Jumlah cetakan triple: 8
- Jumlah triple di graf hasil: 6
- Triple yang tercetak lebih dari sekali:
  - ex:tif2108 a ex:MataKuliahAktif (2 kali).
  - ex:tif2104 a ex:MataKuliahAktif (2 kali).

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
- Jumlah triple universitas.ttl: 134
- Jumlah baris universitas_per_kota.csv: [isi] (tanpa baris judul)
- setReturnFormat(TURTLE): Baris ini meminta balasan dalam format Turtle. Q6 adalah CONSTRUCT, jadi hasilnya berupa graf RDF, bukan tabel. Bersama `setOnlyConneg(True)`, format itu diminta lewat header HTTP `Accept: text/turtle` saja, sehingga Wikidata membalas dengan teks Turtle. Saat berkas Q6 saya masih berisi versi SELECT, Wikidata membalas tabel `application/sparql-results+xml` dan `Graph().parse()` gagal. Ini menunjukkan format Turtle hanya bisa diperoleh dari query yang menghasilkan graf.
- Graph().parse(data=...): `queryAndConvert()` hanya mengembalikan teks Turtle, belum berupa graf. `Graph().parse(data=..., format="turtle")` membaca teks itu langsung dari memori (argumen `data=`, bukan nama berkas) dan mengubahnya menjadi objek Graph rdflib berisi 134 triple. Setelah itu graf bisa dihitung dengan `len(g)`, disimpan dengan `g.serialize("universitas.ttl")`, dan di-query dengan `g.query()`.
- Mengapa q_kota tidak memanggil endpoint: `q_kota` dijalankan dengan `g.query(q_kota)`, yaitu method milik objek Graph lokal. Query itu dieksekusi oleh mesin SPARQL rdflib di laptop atas triple yang sudah ada di memori, yang isinya sama dengan universitas.ttl. Satu-satunya baris yang menghubungi Wikidata adalah `sp.queryAndConvert()`, dan baris itu hanya dipanggil sekali. universitas.ttl menjadi cache: query berikutnya cukup dijalankan pada graf lokal tanpa membebani endpoint publik.
- Catatan: satu universitas bisa punya lebih dari satu nilai `wdt:P131` (misalnya kota dan provinsinya), sehingga ia terhitung di setiap wilayah itu. `COUNT(DISTINCT ?u)` hanya mencegah universitas yang sama terhitung dua kali di wilayah yang sama.

## Refleksi
1. **Mengapa jumlah triple CONSTRUCT bisa lebih kecil dari jumlah baris SELECT?**
   SELECT menghasilkan satu baris per solution, dan baris yang sama boleh muncul berulang. CONSTRUCT mencetak template sekali per solution, tetapi hasilnya graf, yaitu himpunan triple, sehingga triple yang identik hanya disimpan sekali. Di Langkah 1, 4 solution × 2 pola menghasilkan 8 cetakan, tetapi grafnya hanya berisi 6 triple: `ex:tif2108 a ex:MataKuliahAktif` dan `ex:tif2104 a ex:MataKuliahAktif` masing-masing tercetak dua kali karena tiap mata kuliah diampu dua dosen. Di Langkah 2, soal B menghasilkan 4 baris karena Sari muncul dua kali (lewat DosenTetap dan DosenTamu), sedangkan soal C dengan WHERE yang sama hanya menghasilkan 3 triple. Di Langkah 4, Q6 dengan LIMIT 50 dan 3 pola seharusnya maksimal 150 triple, tetapi hasilnya 134. Universitas yang punya beberapa nilai `wdt:P131` muncul di beberapa solution, sehingga triple `a ex:Universitas` dan `ex:nama`-nya tercetak kembar lalu digabung.

2. **Bila taksonomi graf kampus berubah bulan depan?**
   Triple turunan di kampus_usu_v4.ttl tidak ikut berubah. Materialisasi hanya potret saat program dijalankan: triple seperti `?x a ex:Pegawai` dan `?x a foaf:Person` disimpan sebagai triple biasa, bukan sebagai aturan. Misalnya bulan depan `ex:Dosen` tidak lagi subkelas `ex:Pegawai`. Triple `ex:<dosen> a ex:Pegawai` dan `a foaf:Person` tetap ada dan kini salah, sedangkan query `SELECT ?x WHERE { ?x a foaf:Person }` tetap menghitung semua dosen. Masalah lain, kampus_usu_v4.ttl mencampur triple asli dan turunan tanpa penanda, sehingga saya tidak bisa langsung tahu mana yang harus dihapus. Cara yang lebih aman: simpan triple turunan di berkas terpisah, buang berkas itu saat taksonomi berubah, lalu jalankan ulang materialisasi dari graf sumber. Hal yang sama berlaku untuk dosen baru, yang tidak akan menjadi foaf:Person sampai program dijalankan ulang. Pekerjaan inilah yang nantinya dilakukan otomatis oleh reasoner.

3. **Kapan disimpan sebagai tabel (CSV), kapan sebagai graf (Turtle)?**
   Saya menyimpan sebagai CSV bila hasilnya adalah jawaban akhir untuk dibaca manusia atau diolah alat lain, seperti hitungan, ringkasan, atau data untuk grafik dan spreadsheet. Contohnya universitas_per_kota.csv: satu baris per wilayah dengan satu angka, hasil agregasi `GROUP BY` yang langsung bisa dibuka di Excel. Saya menyimpan sebagai Turtle bila hasilnya masih akan di-query, digabung dengan data lain, atau dipakai ulang sebagai data. Contohnya universitas.ttl (134 triple): graf itu sudah memakai kosakata `ex:` saya, IRI Wikidata-nya tetap utuh sehingga bisa ditautkan dengan graf kampus, dan berfungsi sebagai cache sehingga query berikutnya seperti q_kota tidak perlu menghubungi endpoint lagi. Polanya: ambil dari endpoint dan simpan sebagai Turtle sekali, lalu turunkan berbagai CSV dari graf lokal itu sesuai kebutuhan.
