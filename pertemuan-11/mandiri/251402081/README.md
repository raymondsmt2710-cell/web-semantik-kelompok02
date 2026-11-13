# Pertemuan 11 - Tugas Mandiri: Dari Endpoint ke Graf Lokal

Nama: Charles
NIM: 251402081

## Bagian A - LIMIT dan triple
- Triple dengan LIMIT 10: [isi]
- Triple dengan LIMIT 30: [isi]
- Baris SELECT LIMIT 10 / kota berbeda: [isi] / [isi]
- Mengapa tidak (atau mengapa tepat) 30 triple: Karena template berisi 3 pola, 10 solution paling banyak menghasilkan 30 triple. Saya memperoleh [isi] triple sebab 10 baris SELECT itu hanya memuat [isi] kota yang berbeda. Kota [isi nama kota yang muncul lebih dari sekali] tampil di [isi] baris, masing-masing dengan nilai `?populasi` yang lain, karena di Wikidata kota tersebut memiliki lebih dari satu pernyataan P1082. Pada baris-baris dengan kota yang sama, pola `?kota a ex:Kota` dan `?kota rdfs:label ?namaKota` menghasilkan triple yang identik. Graf RDF bersifat himpunan, sehingga triple yang identik itu hanya disimpan sekali. Satu-satunya pola yang menghasilkan triple berbeda di tiap baris adalah `?kota ex:populasi ?populasi`. Dengan demikian, jumlah triple = 2 × (kota berbeda) + (baris) = 2 × [isi] + 10 = [isi], sama dengan angka CONSTRUCT di atas. Penalaran yang sama berlaku untuk LIMIT 30: batas maksimumnya 90, sedangkan hasil saya [isi].

## Bagian B - DBpedia ke Turtle
- Output demo_c.py: 12 triple, film tanpa tanggal: 1
- Sumber data: data contoh film.ttl (`python jalankan.py film.ttl q_demo_b.rq`, 12 triple; hasilnya disimpan sebagai film_nolan.ttl)
- Triple yang tetap tercetak untuk film tanpa tanggal: Dalam data contoh, film yang tidak memiliki `dbo:releaseDate` adalah Insomnia. Untuk film ini, tiga pola template tetap menghasilkan triple: `dbr:Insomnia a schema:Movie`, `schema:name "Insomnia"@en`, dan `schema:director dbr:Christopher_Nolan`. Pola `?film schema:datePublished ?rilis` tidak dicetak karena `?rilis` terletak di dalam OPTIONAL dan tidak memiliki nilai pada solution tersebut. Hal ini tidak menimbulkan error, sebab aturan CONSTRUCT menetapkan bahwa triple template dengan variabel tak terikat cukup dilompati. Itu bukan kesalahan, dan pola-pola lain pada solution yang sama tetap dicetak. Perhitungannya: ada 4 solution (Memento memiliki dua tanggal sehingga menjadi dua solution) × 4 pola = 16 cetakan. Dari jumlah itu dikurangi 1 cetakan yang dilompati (Insomnia) dan 3 cetakan Memento yang kembar lalu digabung, sehingga tersisa 12 triple.
- Query lokal tanpa internet: Berhasil, dan hasilnya tetap 1. `Graph().parse("film_nolan.ttl")` hanya membaca berkas yang ada di disk, sedangkan `lokal.query(...)` dijalankan oleh mesin SPARQL rdflib di laptop. Karena itu tidak ada satu pun permintaan ke jaringan. Jika seluruh demo_c.py dijalankan ulang dalam keadaan offline, program akan berhenti dengan galat koneksi (URLError) di baris `sp.queryAndConvert()`, karena baris inilah yang mengirim query ke https://dbpedia.org/sparql. Baris-baris setelahnya tidak sempat dijalankan, sehingga film_nolan.ttl yang lama tetap utuh.
- Mengapa dbo:Film memberi 0 pada film_nolan.ttl: Isi film_nolan.ttl hanyalah triple yang dihasilkan oleh template CONSTRUCT, dan template itu menuliskan `?film a schema:Movie`, bukan `?film a dbo:Film`. Triple `a dbo:Film` hanya berperan di bagian WHERE untuk mencocokkan data di endpoint, dan tidak ikut disalin ke hasil. Saya sudah mengujinya: `SELECT (COUNT(?f) AS ?n) WHERE { ?f a dbo:Film }` pada film_nolan.ttl menghasilkan 0, sedangkan bila memakai `schema:Movie` hasilnya 3 film. Graf lokal sudah menggunakan kosakata schema.org, sehingga query lokal juga harus memakai kosakata tersebut.

## Bagian C - Materialisasi
- Output demo_d.py:
  ```
  Sebelum: 0
  Sesudah: 3
  Ada Rina: 3
  ```
- Mengapa Ada Rina bernilai 3: Materialisasi hanya merekam keadaan pada satu saat. CONSTRUCT dijalankan sekali saja, ketika Rina belum ada, dan hasilnya (budi, sari, andi `a foaf:Person`) dimasukkan ke graf sebagai triple biasa. Saat `ex:rina a ex:DosenTetap` ditambahkan, aturan tersebut tidak dijalankan lagi, sehingga triple `ex:rina a foaf:Person` tidak pernah terbentuk. `Q_ORANG` hanya mencocokkan triple `?x a foaf:Person` yang tertulis secara eksplisit tanpa menelusuri `rdfs:subClassOf`, dan rdflib sendiri tidak melakukan penalaran. Akibatnya Rina tidak ikut terhitung, padahal secara logika ia adalah seorang Person.
- Output materialisasi_ulang.py:
  ```
  Putaran 1: 4 triple baru | Person: 3
  Rina masuk | Person: 3
  Putaran 2 | Person: 4
  Triple turunan disimpan terpisah: 6
  ```
- Tiga triple yang bukan baru: `ex:budi a ex:DosenTetap`, `ex:sari a ex:Dosen`, dan `ex:andi a ex:Mahasiswa`. Ketiganya adalah triple tipe asli yang memang sudah tercantum di kampus.ttl. Triple ini tercetak ulang karena tanda `*` pada `rdfs:subClassOf*`. Bintang berarti nol langkah atau lebih; pada nol langkah, `?super` sama dengan kelas langsung `?x`, sehingga template mencetak kembali triple aslinya. Empat triple yang benar-benar baru berasal dari satu atau dua langkah: budi → Dosen, budi → Person, sari → Person, andi → Person.
- Kegunaan kampus_turunan.ttl dan langkah manual yang tersisa: Berkas ini memuat tepat 6 triple hasil simpulan (budi dan rina masing-masing `a ex:Dosen` dan `a foaf:Person`; sari dan andi `a foaf:Person`), dan disimpan terpisah dari fakta asli. Jika suatu saat `ex:Dosen` tidak lagi menjadi subkelas `foaf:Person`, saya bisa langsung tahu triple mana yang dihasilkan aturan dan aman untuk dibuang, tanpa risiko menghapus fakta yang memang ditulis manusia. Di kampus_v4.ttl hal ini tidak bisa dilakukan karena triple asli dan triple turunan sudah tercampur. Langkah yang masih harus dikerjakan secara manual: (1) mengubah taksonomi di data sumber, (2) menghapus triple turunan lama dari graf produksi, karena tidak ada mekanisme yang mencabutnya secara otomatis, (3) menjalankan kembali materialisasi lalu menyimpan ulang kedua berkas, dan (4) mengulangi langkah tersebut setiap kali ada data atau taksonomi baru.

## Bagian D - Diagnosis
| Query | Hasil mesin | Gejala | Penyebab (baris yang salah) | Hasil setelah diperbaiki |
|-------|-------------|--------|-----------------------------|--------------------------|
| rusak_a | 0 triple, tanpa error | Graf kosong, tanpa error (semua pola template memakai variabel tak terikat) | Baris `CONSTRUCT { ?film ex:judul ?j . }` menggunakan `?film`, sedangkan WHERE mengikat `?f`. Karena `?film` tidak pernah mendapat nilai, satu-satunya pola template selalu dilompati. `SELECT *` dengan WHERE yang sama menghasilkan 3 baris, jadi bagian WHERE sudah benar. | `?film` diganti `?f`: 3 triple (Following, Insomnia, Memento) |
| rusak_b | 4 triple; Christopher Nolan mendapat dua `ex:nama` | Dua nilai yang tampak sama (beda tag bahasa) | Baris `?o foaf:name\|rdfs:label\|schema:name ?n .` mengambil `"Christopher Nolan"` dari foaf:name dan `"Christopher Nolan"@en` dari rdfs:label. Keduanya merupakan literal yang berbeda, sehingga tidak digabung. | Ditambahkan `BIND ( STR(?n) AS ?nama )` dan template memakai `?nama`: 3 triple, satu nama untuk setiap orang |
| rusak_c | 0 triple, tanpa error | Superkelas tidak ditemukan (pola tanpa jalur subClassOf*) | Baris `?x a ex:Permukiman .` hanya cocok dengan tipe langsung, padahal Medan, Surabaya, dan Tomok bertipe subkelasnya (KotaMetropolitan, KotaDiIndonesia, Desa). | Diganti `?x a/rdfs:subClassOf* ex:Permukiman .`: 3 triple (Medan, Surabaya, Tomok) |

## Bagian E - Etika dan diskusi
| Aturan | a_kota_limit.rq | demo_c.py |
|--------|-----------------|-----------|
| 1 User-Agent | Tidak berlaku untuk berkas ini: query dijalankan melalui query.wikidata.org, dan User-Agent dikirim oleh browser. Aturan ini baru relevan jika query dikirim dari program. | Terpenuhi: baris `UA = "KelasWebSemantik/1.0 (...)"` mencantumkan nama aplikasi dan email, kemudian digunakan di `SPARQLWrapper("https://dbpedia.org/sparql", agent=UA)`. |
| 2 LIMIT | Terpenuhi: baris terakhir berisi `LIMIT 10` (kemudian 30). Yang dibatasi adalah jumlah solution, bukan jumlah triple. | Tidak memakai LIMIT, tetapi query ini bukan eksplorasi: WHERE sudah dikunci dengan `dbo:director dbr:Christopher_Nolan`, sehingga hasilnya kecil dan terbatas. |
| 3 Simpan, jangan ulangi | Query tidak memuat baris penyimpanan, tetapi hasilnya dapat diunduh dari browser. Untuk tugas ini query memang dijalankan beberapa kali dengan LIMIT kecil. | Terpenuhi: `sp.queryAndConvert()` hanya dipanggil sekali, `g.serialize("film_nolan.ttl", ...)` menyimpan grafnya, lalu `Graph().parse("film_nolan.ttl")` memprosesnya secara lokal. |
| 4 Jangkar jalur | Terpenuhi: `?kota wdt:P31/wdt:P279* wd:Q515` memiliki ujung berupa IRI `wd:Q515`, dan `wdt:P17 wd:Q252` mempersempit hasil ke Indonesia. | Tidak berlaku: q_demo_b.rq tidak menggunakan jalur `*` maupun `+`. |

- Versi yang melanggar aturan 4 (tidak dijalankan) dan alasannya:
  ```sparql
  PREFIX ex: <http://contoh.id/>
  CONSTRUCT {
    ?kota a ex:Kota ;
          rdfs:label ?namaKota ;
          ex:populasi ?populasi .
  }
  WHERE {
    ?kota wdt:P31/wdt:P279* ?kelas ;      # kedua ujung jalur adalah variabel
          wdt:P1082 ?populasi ;
          rdfs:label ?namaKota .
    FILTER ( LANG(?namaKota) = "id" )
  }
  LIMIT 10
  ```
  Pada versi aslinya, endpoint cukup memulai dari `wd:Q515`, menelusuri subkelas-subkelasnya, kemudian mengambil instans yang berada di Indonesia. Pada versi ini `wd:Q515` digantikan oleh `?kelas` dan `wdt:P17 wd:Q252` dihapus, sehingga jalur tidak lagi memiliki titik awal. Endpoint terpaksa memeriksa setiap entitas yang memiliki P31 (lebih dari seratus juta item), dan untuk masing-masing entitas menelusuri seluruh rantai `P279*` ke atas. Jumlah pasangan (`?kota`, `?kelas`) membengkak, dan query hampir pasti berakhir dengan timeout sambil menghabiskan sumber daya yang digunakan bersama oleh pengguna lain.

### Diskusi 1 - Taksonomi berubah
Andaikan setahun kemudian `ex:Dosen` tidak lagi menjadi subkelas `foaf:Person`. Triple yang menjadi salah adalah semua simpulan Person yang diturunkan melalui Dosen, yaitu `ex:budi a foaf:Person`, `ex:sari a foaf:Person`, dan `ex:rina a foaf:Person`. Triple `ex:andi a foaf:Person` tetap benar karena diturunkan melalui `ex:Mahasiswa`. Demikian pula `ex:budi a ex:Dosen` dan `ex:rina a ex:Dosen` tetap benar selama DosenTetap masih merupakan subkelas Dosen.

Di kampus_v4.ttl hasil C1, triple-triple tersebut sulit dilacak. Berkas itu memuat 13 triple: 9 triple asli dan 4 triple turunan yang bercampur tanpa penanda apa pun. `ex:budi a foaf:Person` terlihat persis seperti fakta yang ditulis tangan, dan demo_d.py bahkan menambahkan kembali 3 triple yang sudah ada tanpa mencatat mana yang baru. Satu-satunya jalan adalah membandingkannya dengan kampus.ttl asli, itu pun jika berkas tersebut masih disimpan.

Di C2, kampus_turunan.ttl memuat tepat 6 triple hasil aturan, sehingga cara menemukannya menjadi mekanis: hapus keenam triple itu dari graf produksi, perbaiki taksonomi, lalu jalankan kembali `materialisasi()`. Hasil yang baru hanya berisi `ex:andi a foaf:Person` dan dua triple Dosen. Selisih antara berkas turunan lama dan berkas turunan baru itulah daftar triple yang salah, yaitu tiga triple Person tadi. Pelajaran yang saya ambil: simpulan perlu disimpan terpisah dari fakta, dan seperti tampak pada "Rina masuk | Person: 3", materialisasi tidak pernah memperbarui dirinya sendiri.

### Diskusi 2 - SELECT atau CONSTRUCT
Untuk dashboard populasi kota, saya memilih SELECT. Dashboard memerlukan tabel, yaitu satu baris per kota dengan satu angka, yang dapat diurutkan dan diagregasi. Temuan di Bagian A memperlihatkan alasannya: 10 baris SELECT hanya memuat [isi] kota berbeda karena ada kota yang memiliki beberapa nilai populasi. Dalam SELECT, masalah ini langsung terlihat sebagai baris ganda dan dapat diatasi di dalam query, misalnya dengan `GROUP BY ?kota` dan `MAX(?populasi)`. CONSTRUCT malah menyamarkannya: triple tipe dan label yang kembar digabung, sehingga saya memperoleh [isi] triple, bukan 30, dan kota tersebut tanpa disadari memiliki dua `ex:populasi` di dalam graf. Dashboard yang membaca graf itu akan menampilkan angka ganda.

Untuk menggabungkan data kota dari tiga sumber, saya memilih CONSTRUCT. Tujuannya adalah membentuk graf baru dengan satu kosakata, seperti q_demo_b.rq yang mengubah `dbo:Film` menjadi `schema:Movie`; hasilnya bisa disimpan sebagai film_nolan.ttl lalu digabungkan dengan `g.parse()`. Tabel SELECT dari tiga sumber dengan kolom yang berlainan tidak bisa digabungkan semudah itu. Meski begitu, rusak_b.rq menunjukkan bahwa penggabungan otomatis hanya terjadi pada triple yang benar-benar identik: `"Christopher Nolan"` dan `"Christopher Nolan"@en` dianggap berbeda, sehingga hasilnya 4 triple, bukan 3. Oleh karena itu, sebelum tiga sumber digabungkan, nilai-nilainya perlu dinormalkan terlebih dahulu di template, misalnya memakai `STR()` seperti di perbaikan_b.rq, dan untuk populasi ganda harus dipilih satu nilai saja.

### Cek diri
| Pernyataan | Bukti dari tugas ini |
|------------|----------------------|
| 1 | Bagian A: 10 solution × 3 pola semestinya 30, tetapi hasil saya [isi] triple karena cetakan yang kembar digabung. Bagian B: 4 solution × 4 pola = 16 cetakan, menghasilkan 12 triple (Memento memiliki dua tanggal). |
| 2 | Bagian B: Insomnia tidak memiliki tanggal, sehingga triple `schema:datePublished` tidak dicetak, sementara 3 triple lainnya tetap ada, tanpa error. Bagian D: rusak_a.rq menghasilkan 0 triple tanpa error karena `?film` tidak terikat. |
| 3 | Bagian D: pada rusak_b.rq, jalur `foaf:name\|rdfs:label\|schema:name` bersama `VALUES` menyatukan tiga predikat menjadi `ex:nama` untuk 3 orang (4 triple, menjadi 3 setelah diperbaiki). |
| 4 | Bagian D: perbaikan_c.rq dengan `a/rdfs:subClassOf*` menemukan Medan, Surabaya, dan Tomok (dari 0 menjadi 3 triple) tanpa menyebut ex:Kota atau ex:Desa. Bagian C: budi (DosenTetap) menjadi Person melalui Dosen. |
| 5 | Bagian C: demo_d.py menunjukkan "Sesudah: 3" tetapi "Ada Rina: 3"; di materialisasi_ulang.py, jumlah Person baru naik menjadi 4 setelah Putaran 2, dan triple turunan bertambah dari 4 menjadi 6. |