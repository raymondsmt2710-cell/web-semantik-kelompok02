# Pertemuan 11 - Tugas Mandiri: Dari Endpoint ke Graf Lokal

## Bagian A - LIMIT dan triple
- Triple dengan LIMIT 10: 30
- Triple dengan LIMIT 30: 90
- Baris SELECT LIMIT 10 / kota berbeda: 10 / 10
- Mengapa tidak (atau mengapa tepat) 30 triple: Hasil CONSTRUCT dengan LIMIT 10 menghasilkan tepat 30 triple karena setiap solusi yang dihasilkan oleh klausa WHERE membentuk tiga triple, yaitu tipe kota, label kota, dan populasi kota. Dengan demikian, 10 solusi menghasilkan 10 × 3 = 30 triple. LIMIT membatasi jumlah solusi query, bukan jumlah triple yang dihasilkan.

## Bagian B - DBpedia ke Turtle
- Output demo_c.py: 48 triple, film tanpa tanggal: 16
- Sumber data: DBpedia (endpoint SPARQL).
- Triple yang tetap tercetak untuk film tanpa tanggal: Movie, schema:name, dan schema:director tetap dihasilkan. Triple schema:datePublished tidak dihasilkan karena tanggal rilis tidak tersedia. Hal ini terjadi karena penggunaan OPTIONAL.
- Query lokal tanpa internet: Tetap dapat dijalankan karena data sudah disimpan dalam file film_nolan.ttl. RDFLib membaca dan memproses data tersebut secara lokal tanpa mengakses DBpedia.
- Mengapa dbo:Film memberi 0 pada film_nolan.ttl: Karena query CONSTRUCT mengubah tipe film dari dbo:Film menjadi schema:Movie. Akibatnya, graf hasil hanya menyimpan tipe schema:Movie, bukan dbo:Film.

## Bagian C - Materialisasi
- Output demo_d.py: Sebelum: 0, Sesudah: 3, Ada Rina: 3.
- Mengapa Ada Rina bernilai 3: Karena materialisasi dilakukan sebelum Rina ditambahkan. Tiga individu yang sudah memiliki tipe foaf:Person adalah Budi, Sari, dan Andi. Setelah Rina ditambahkan sebagai ex:DosenTetap, aturan materialisasi tidak dijalankan ulang sehingga Rina belum dihitung sebagai foaf:Person.
- Output materialisasi_ulang.py: 
    Putaran 1: 4 triple baru | Person: 3
    Rina masuk | Person: 3
    Putaran 2 | Person: 4
    Triple turunan disimpan terpisah: 6
- Tiga triple yang bukan baru: ex:budi a ex:DosenTetap, ex:sari a ex:Dosen, dan ex:andi a ex:Mahasiswa. Ketiga triple tersebut sudah ada di kampus.ttl. Query dengan jalur a/rdfs:subClassOf* menghasilkan kembali tipe kelas asal karena tanda * memperbolehkan jalur dengan panjang nol.
- Kegunaan kampus_turunan.ttl dan langkah manual yang tersisa: File kampus_turunan.ttl menyimpan triple hasil materialisasi secara terpisah dari data utama. Hal ini memudahkan identifikasi dan pengelolaan triple turunan jika struktur kelas berubah. Jika suatu saat ex:Dosen tidak lagi menjadi subkelas foaf:Person, triple turunan yang menyimpulkan dosen sebagai foaf:Person bisa menjadi tidak valid. Langkah manual yang harus dilakukan adalah menghapus atau memperbarui triple turunan yang sudah tidak sesuai, kemudian menjalankan kembali proses materialisasi berdasarkan struktur kelas terbaru.

## Bagian D - Diagnosis
| Query | Hasil mesin | Gejala | Penyebab (baris yang salah) | Hasil setelah diperbaiki |
|-------|-------------|--------|-----------------------------|--------------------------|
| rusak_a | 0 triple | Graf kosong tanpa error | Variabel ?film pada template CONSTRUCT tidak terikat pada bagian WHERE. Seharusnya menggunakan ?f. | 3 triple: Following, Memento, dan Insomnia. |
| rusak_b | 4 triple | Dua nilai nama yang tampak sama menghasilkan triple berbeda. | Pola ?o foaf:name|rdfs:label|schema:name ?n mengambil dua label Christopher Nolan, yaitu "Christopher Nolan" dan "Christopher Nolan"@en. Perbedaan tag bahasa membuat keduanya dianggap berbeda. | 3 triple: satu nama untuk setiap orang. |
| rusak_c | 0 triple | Superkelas tidak ditemukan | Pola ?x a ex:Permukiman hanya mencari tipe langsung dan tidak menelusuri hubungan rdfs:subClassOf. | 3 triple: Medan, Surabaya, dan Tomok |

## Bagian E - Etika dan diskusi
| Aturan | a_kota_limit.rq | demo_c.py |
|--------|-----------------|-----------|
| 1 User-Agent | Tidak relevan karena file ini hanya berisi query yang dijalankan melalui Wikidata Query Service. | Menggunakan User-Agent `KelasWebSemantik/1.0 (ryanfredryck@students.usu.ac.id)` dan meneruskannya melalui parameter `agent=UA` pada SPARQLWrapper. |
| 2 LIMIT | Menggunakan LIMIT 10 untuk membatasi jumlah solusi saat eksplorasi. | Tidak menggunakan LIMIT pada proses pengambilan data film. |
| 3 Simpan, jangan ulangi | Tidak menyimpan hasil secara otomatis karena hanya berupa file query. | Menyimpan hasil ke film_nolan.ttl, kemudian memproses data secara lokal tanpa mengulang permintaan ke DBpedia. |
| 4 Jangkar jalur | Menggunakan jalur wdt:P31/wdt:P279* yang berakhir pada IRI tetap wd:Q515. | Tidak relevan jika query yang digunakan tidak memakai property path hierarki. |
- Versi yang melanggar aturan 4 (tidak dijalankan) dan alasannya: Mengubah jalur `?kota wdt:P31/wdt:P279* wd:Q515` menjadi `?kota wdt:P31/wdt:P279* ?kelas`. Perubahan ini membuat kedua ujung property path menggunakan variabel sehingga tidak memiliki IRI sebagai jangkar. Akibatnya, endpoint harus menelusuri lebih banyak kemungkinan hubungan kelas dan membutuhkan pemrosesan yang lebih besar. Query ini sengaja tidak dijalankan karena dapat membebani endpoint publik.

### Diskusi 1 - Taksonomi berubah
Jika hasil materialisasi Bagian C disimpan langsung ke graf produksi, perubahan taksonomi dapat menyebabkan beberapa triple hasil inferensi menjadi tidak valid. Contohnya, apabila ex:Dosen tidak lagi menjadi subkelas foaf:Person, maka triple yang menyatakan individu bertipe ex:Dosen juga bertipe foaf:Person harus diperiksa kembali. Triple tersebut sebelumnya benar karena mengikuti hubungan subkelas, tetapi menjadi salah setelah hubungan taksonomi diubah.

Untuk menemukan triple yang terdampak, saya akan membandingkan graf produksi dengan struktur taksonomi terbaru. Saya juga dapat memeriksa individu bertipe ex:Dosen, kemudian mencari triple foaf:Person yang dihasilkan dari hubungan tersebut. Hasil materialisasi lama perlu dihapus atau dihitung ulang agar tidak menyimpan kesimpulan yang sudah tidak berlaku.

Perbedaan kampus_v4.ttl dan kampus_turunan.ttl pada Bagian C menunjukkan pentingnya memisahkan data utama dan data hasil inferensi. kampus_v4.ttl berisi graf lengkap setelah materialisasi, sehingga triple asli dan hasil inferensi bercampur. Sebaliknya, kampus_turunan.ttl menyimpan enam triple hasil materialisasi secara terpisah. Dengan pemisahan ini, triple hasil inferensi lebih mudah diperiksa dan diperbarui ketika taksonomi berubah.

### Diskusi 2 - SELECT atau CONSTRUCT
Untuk membuat dashboard populasi kota, saya akan menggunakan SELECT. Alasannya, dashboard membutuhkan data dalam bentuk baris dan kolom agar mudah dihitung, dibandingkan, dan ditampilkan. Misalnya, jumlah populasi dapat diurutkan, dijumlahkan, atau dikelompokkan berdasarkan wilayah. SELECT juga memudahkan pemeriksaan apabila satu kota memiliki lebih dari satu nilai populasi.

Hal ini berkaitan dengan temuan pada Bagian A. Query CONSTRUCT dengan LIMIT 10 menghasilkan 30 triple karena setiap solusi membentuk tiga triple. Artinya, jumlah triple tidak selalu sama dengan jumlah solusi query. Untuk kebutuhan analisis angka pada dashboard, hasil SELECT lebih mudah dikendalikan dan diperiksa.

Namun, jika saya harus menggabungkan data kota dari tiga sumber berbeda, saya akan mempertimbangkan CONSTRUCT. Query tersebut dapat mengubah data dari berbagai sumber menjadi struktur RDF dengan kosakata dan bentuk triple yang seragam. Hasilnya juga dapat disimpan sebagai graf baru untuk digunakan kembali.

Temuan pada rusak_b.rq di Bagian D menunjukkan bahwa "Christopher Nolan" dan "Christopher Nolan"@en dianggap sebagai literal berbeda karena memiliki tag bahasa yang berbeda. Oleh karena itu, sebelum menggabungkan data dari beberapa sumber, format nilai dan tag bahasanya perlu diperiksa atau diseragamkan agar tidak menghasilkan data ganda yang sebenarnya memiliki makna sama.

### Cek diri
| Pernyataan | Bukti dari tugas ini |
|------------|----------------------|
| 1. CONSTRUCT menghasilkan template sekali per solusi dan menggabungkan triple duplikat. | Bagian A: CONSTRUCT LIMIT 10 menghasilkan 30 triple dari 10 solusi. Jika triple yang dihasilkan sama, graf RDF hanya menyimpannya satu kali. |
| 2. Triple dengan variabel yang tidak terikat tidak dihasilkan tanpa error. | Bagian D: rusak_a.rq menghasilkan 0 triple karena ?film pada template tidak terikat di bagian WHERE. |
| 3. UNION, property path \|, dan VALUES dapat menggabungkan pencarian melalui beberapa predikat. | Bagian D: rusak_b.rq menggunakan VALUES untuk menentukan tiga orang dan property path foaf:name\|rdfs:label\|schema:name untuk mencari nama melalui beberapa predikat. UNION tidak digunakan secara langsung dalam query yang diuji. |
| 4. Jalur + dan * dapat menelusuri hierarki tanpa menyebutkan kelas perantara. | Bagian C dan D: penggunaan rdfs:subClassOf* memungkinkan pencarian kelas induk. Pada perbaikan_c.rq, query berhasil menemukan tiga permukiman. |
| 5. Materialisasi menyimpan kesimpulan, tetapi perlu dihitung ulang jika aturan berubah | Bagian C: kampus_turunan.ttl menyimpan enam triple hasil materialisasi. Jika taksonomi berubah, triple turunan yang sudah tidak sesuai harus diperbarui atau dihitung ulang. |