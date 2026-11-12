# Pertemuan 11 - Tugas Mandiri: Dari Endpoint ke Graf Lokal

## Bagian A - LIMIT dan triple
- Triple dengan LIMIT 10: [30]
- Triple dengan LIMIT 30: [90]
- Baris SELECT LIMIT 10 / kota berbeda: [10] / [10]
- Mengapa tidak (atau mengapa tepat) 30 triple: Hasilnya tepat 30 triple karena terdapat 10 solution dan setiap solution mencetak 3 pola template. Tidak ada triple kembar karena semua kota yang muncul berbeda.

## Bagian B - DBpedia ke Turtle
- Output demo_c.py: [48] triple, film tanpa tanggal: [16]
- Sumber data: Data diperoleh dari endpoint SPARQL DBpedia.
- Triple yang tetap tercetak untuk film tanpa tanggal: Informasi seperti schema:Movie, schema:name, dan schema:director tetap dibuat. Namun, schema:datePublished tidak muncul jika data tanggal rilis tidak tersedia. Ini karena penggunaan OPTIONAL pada query.
- Query lokal tanpa internet: Query masih bisa dijalankan meskipun tidak terhubung ke internet karena data DBpedia sudah disimpan dalam file film_nolan.ttl. RDFLib kemudian membaca file tersebut secara langsung.
- Mengapa dbo:Film memberi 0 pada film_nolan.ttl: Pada query CONSTRUCT, tipe film diubah menjadi schema:Movie. Oleh karena itu, graf hasil tidak lagi menggunakan tipe dbo:Film, sehingga pencarian dengan tipe tersebut tidak menemukan data.

## Bagian C - Materialisasi
- Output demo_d.py: Sebelum: 0, Sesudah: 3, Ada Rina: 3.
- Mengapa Ada Rina bernilai 3: karena aturan materialisasi hanya dijalankan sebelum Rina ditambahkan ke dalam graf. Akibatnya, tipe foaf:Person milik Rina belum terbentuk. Walaupun ex:DosenTetap merupakan turunan dari foaf:Person, hubungan tersebut belum diproses kembali setelah Rina masuk. Jadi, query masih menemukan 3 orang dari hasil materialisasi sebelumnya.
- Output materialisasi_ulang.py: 
Putaran 1: 4 triple baru | Person: 3
Rina masuk | Person: 3
Putaran 2 | Person: 4
Triple turunan disimpan terpisah: 6
- Tiga triple yang bukan baru: Tiga triple lainnya merupakan triple yang sudah ada di dalam kampus.ttl, yaitu hubungan tipe awal setiap individu dengan kelasnya. Triple tersebut dihasilkan oleh bagian a pada jalur a/rdfs:subClassOf*, yang mengambil tipe langsung dari setiap individu tanpa melewati hubungan subclass. Karena ketiga triple itu sudah tersimpan di graf, ketiganya tidak dihitung sebagai triple baru.
- Kegunaan kampus_turunan.ttl dan langkah manual yang tersisa: Berkas kampus_turunan.ttl memudahkan pengelolaan triple hasil penurunan secara terpisah. Jika aturan subclass berubah, kita harus menjalankan ulang materialisasi dan menghapus triple yang sudah tidak sesuai secara manual.

## Bagian D - Diagnosis

| Query | Hasil mesin | Gejala | Penyebab (baris yang salah) | Hasil setelah diperbaiki |
|---|---|---|---|---|
| rusak_a | [isi hasil terminal] | Graf kosong | Variabel `?film` pada template tidak terikat karena WHERE menggunakan `?f`. | 3 triple |
| rusak_b | [isi hasil terminal] | Triple lebih banyak dari target | Beberapa predikat dapat menghasilkan lebih dari satu nama untuk setiap orang. | 3 triple |
| rusak_c | [isi hasil terminal] | Triple lebih sedikit dari target | WHERE hanya mencari tipe langsung `ex:Permukiman`, bukan kelas turunannya. | 3 triple |

## Bagian E - Etika dan diskusi
| Aturan | a_kota_limit.rq | demo_c.py |
|--------|-----------------|-----------|
| 1 User-Agent | Tidak digunakan karena query dijalankan langsung melalui Wikidata Query Service. | Mengatur User-Agent melalui parameter `agent=UA` pada SPARQLWrapper. |
| 2 LIMIT | Memakai LIMIT 10 untuk membatasi hasil pencarian. | Tidak memakai LIMIT saat mengambil data film. |
| 3 Simpan, jangan ulangi | Hasil query perlu disimpan secara manual jika ingin digunakan kembali. | Menyimpan hasil ke `film_nolan.ttl` agar bisa diproses secara lokal. |
| 4 Jangkar jalur | Menggunakan `wd:Q515` sebagai IRI tujuan pada property path. | Tidak menggunakan property path hierarki. |
- Versi yang melanggar aturan 4 (tidak dijalankan) dan alasannya: Query tersebut tidak memiliki IRI tetap sebagai tujuan jalur. Akibatnya, endpoint perlu memeriksa lebih banyak kemungkinan hubungan kelas dan membutuhkan pemrosesan lebih besar.

### Diskusi 1 - Taksonomi berubah
Perubahan taksonomi dapat membuat hasil inferensi sebelumnya tidak lagi sesuai. Contohnya, jika ex:Dosen tidak lagi menjadi subkelas foaf:Person, triple hasil inferensi yang menyatakan dosen sebagai foaf:Person perlu diperiksa dan diperbarui.

Untuk mengatasinya, graf perlu diperiksa berdasarkan aturan taksonomi terbaru. Triple lama yang sudah tidak sesuai harus dihapus atau dihitung ulang agar tidak menghasilkan informasi yang keliru.

Pada Bagian C, kampus_v4.ttl menyimpan data asli dan hasil inferensi dalam satu graf. Sementara itu, kampus_turunan.ttl menyimpan hasil inferensi secara terpisah. Menurut saya, cara kedua lebih mudah dikelola karena hasil penurunan dapat diperiksa dan diperbarui tanpa mencampuri data utama.

### Diskusi 2 - SELECT atau CONSTRUCT

Untuk dashboard populasi kota, saya memilih SELECT karena hasilnya berbentuk tabel sehingga lebih mudah digunakan untuk membuat grafik, membandingkan, dan mengurutkan data.

Pada Bagian A, SELECT LIMIT 10 menghasilkan 10 baris, sedangkan CONSTRUCT LIMIT 10 menghasilkan 30 triple. Hal ini terjadi karena setiap solusi menghasilkan tiga triple sesuai template CONSTRUCT.

Namun, untuk menggabungkan data kota dari tiga sumber, CONSTRUCT lebih cocok karena dapat menyusun data menjadi graf RDF dengan struktur yang seragam.

Pada Bagian D, rusak_b.rq juga menunjukkan bahwa satu orang dapat memiliki beberapa bentuk nama karena perbedaan predikat atau tag bahasa. Karena itu, data dari beberapa sumber perlu diperiksa dan diseragamkan sebelum digabungkan.

### Cek diri

| Pernyataan | Bukti dari tugas ini |
|------------|----------------------|
| 1 | Bagian A: CONSTRUCT menghasilkan 30 triple dari 10 solusi. |
| 2 | Bagian D: `rusak_a.rq` menghasilkan 0 triple karena variabel `?film` tidak terikat. |
| 3 | Bagian D: `rusak_b.rq` menggunakan VALUES dan property path `\|` untuk mencari nama melalui beberapa predikat. |
| 4 | Bagian C dan D: Menggunakan property path `*` untuk menelusuri hubungan subclass. |
| 5 | Bagian C: Hasil materialisasi disimpan dalam `kampus_turunan.ttl` dan perlu diperbarui jika aturan berubah. |