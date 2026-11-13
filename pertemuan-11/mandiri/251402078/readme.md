# Pertemuan 11 - Tugas Mandiri: Dari Endpoint ke Graf Lokal

## Bagian A - LIMIT dan triple
- Triple dengan LIMIT 10: [30]
- Triple dengan LIMIT 30: [90]
- Baris SELECT LIMIT 10 / kota berbeda: [10] / [10]
- Mengapa tidak (atau mengapa tepat) 30 triple: 
    Dari file query (6).json, tercatat terdapat 10 baris data dengan 10 kota yang berbeda (nilai ?kota unik)—yaitu Tubei (Q12504165), Turikale (Q12711944), Bondowoso (Q7680880), Tanah Merah (Q7682227), Kepanjen (Q9104969), Tanjung Selor (Q10855339), Sidoarjo (Q11544714), Jakarta (Q3630), Kupang (Q23823589), dan Pekalongan (Q24847153). Karena setiap entitas kota dalam data tersebut direpresentasikan oleh tepat 3 atribut atau predikat (kota sebagai tipe, namaKota sebagai label, dan populasi), maka jumlah keseluruhan triple dari ke-10 kota unik tersebut adalah tepat 30 triple ($10 \text{ kota} \times 3 \text{ triple per kota} = 30 \text{ triple}$).

## Bagian B - DBpedia ke Turtle
- Output demo_c.py: [48] triple, film tanpa tanggal: [16]
- Sumber data: DBpedia / data contoh film.ttl
- Triple yang tetap tercetak untuk film tanpa tanggal: [3]
- Query lokal tanpa internet: [Q_TANPA_TANGGAL]
- Mengapa dbo:Film memberi 0 pada film_nolan.ttl: [Query CONSTRUCT Demo B menulis ulang data ke kosakata schema.org, jadi di `film_nolan.ttl` film bertipe `schema:Movie`. Triple dengan `dbo:Film` hanya ada di data asli DBpedia, bukan di graf hasil CONSTRUCT, sehingga query yang memakai `dbo:Film` tidak menemukan apa pun dan menghasilkan 0.]

## Bagian C - Materialisasi
- Output demo_d.py:
 sebleum:0
 sesudah:3
- Mengapa Ada Rina bernilai 3: []
Aturan CONSTRUCT hanya dijalankan satu kali, yaitu sebelum Rina ditambahkan. Setelah itu ex:rina a ex:DosenTetap masuk ke graf, tetapi triple turunan ex:rina a foaf:Person belum pernah dibuat, karena aturan tidak dijalankan lagi. Query Q_ORANG hanya menghitung triple ?x a foaf:Person yang benar-benar ada di graf, bukan yang mungkin diturunkan, sehingga Rina belum terhitung dan hasilnya tetap 3. Materialisasi menyimpan kesimpulan pada saat aturan dijalankan, bukan terus diperbarui.
- Output materialisasi_ulang.py:

- Tiga triple yang bukan baru: [
    Putaran 1: 4 triple baru | Person: 3
Rina masuk | Person: 3
Putaran 2 | Person: 4
]
- Kegunaan kampus_turunan.ttl dan langkah manual yang tersisa: Berkas terpisah menyimpan hanya triple hasil kesimpulan (turunan), sehingga kita selalu tahu mana triple yang berasal dari data asli di `kampus.ttl` dan mana yang hasil aturan. Bila suatu hari `ex:Dosen` tidak lagi menjadi subkelas `foaf:Person`, triple turunan yang bergantung pada hubungan itu (misalnya `ex:sari a foaf:Person`) menjadi tidak sah. Karena sudah dipisah, berkas ini bisa dibuang atau dibuat ulang tanpa menyentuh data asli.

## Bagian D - Diagnosis
| Query | Hasil mesin | Gejala | Penyebab (baris yang salah) | Hasil setelah diperbaiki |
|-------|-------------|--------|-----------------------------|--------------------------|
| rusak_a | [0 triple] | [graf kosong, tanpa error] | ["?f dbo:director dbr:Christopher_Nolan ;"] | [?film dbo:director dbr:Christopher_Nolan ;] |
| rusak_b | [0 triple] | [-] | [?o foaf:name|rdfs:label|schema:name ?n .] | [?o foaf:name|rdfs:label|schema:name ?nama . lalu tambah BIND(STR(?nama) AS ?n)
] |
| rusak_c | [o triple] | [superkelas tidak ditemukan] | [?x a ex:Permukiman .] | [?x a/rdfs:subClassOf* ex:Permukiman .] |

## Bagian E - Etika dan diskusi
| Aturan | a_kota_limit.rq | demo_c.py |
|--------|-----------------|-----------|
| 1 User-Agent | Tidak relevan: dijalankan lewat browser di query.wikidata.org, yang mengirim identitasnya sendiri | Terpenuhi: baris `UA = "KelasWebSemantik/1.0 (raymondganda@Students.usu.ac.id)"` dan `SPARQLWrapper(..., agent=UA)` |
| 2 LIMIT | Terpenuhi: baris `LIMIT 10` di akhir query | Tidak ada LIMIT, tetapi hasilnya sudah dibatasi oleh `dbr:Christopher_Nolan` (hanya 16 film, 48 triple) |
| 3 Simpan, jangan ulangi | Tidak relevan: hanya dijalankan untuk eksplorasi LIMIT, hasilnya disimpan sebagai screenshot | Terpenuhi: `g.serialize("film_nolan.ttl", ...)` dan `Graph().parse("film_nolan.ttl")` untuk query lokal |
| 4 Jangkar jalur | Terpenuhi: jalur `wdt:P31/wdt:P279*` berujung pada IRI tertentu (`wd:Q515`) | Tidak relevan: tidak ada jalur `*` atau `+` |

- Versi yang melanggar aturan 4 (tidak dijalankan) dan alasannya: [lihat di bawah]

### Diskusi 1 - Taksonomi berubah
Setelah taksonomi berubah, triple turunan yang sudah tersimpan tidak ikut berubah, sehingga sebagian menjadi basi. Pada Bagian C, aturan `a/rdfs:subClassOf*` menurunkan `ex:rina a ex:Dosen` dan `ex:rina a foaf:Person` dari fakta bahwa Rina adalah `ex:DosenTetap`. Seandainya `ex:Dosen` tidak lagi menjadi subkelas `foaf:Person`, triple `ex:rina a foaf:Person` kini salah, padahal masih ada di graf produksi dan masih terhitung oleh query `Q_ORANG`. Cara menemukannya adalah membandingkan `kampus_v4.ttl` dari C1 dengan `kampus_turunan.ttl` dari C2. Berkas `kampus_v4.ttl` mencampur data asli dan hasil turunan, jadi dari berkas itu saja saya tidak bisa membedakan triple mana yang boleh dibuang. Sebaliknya, `kampus_turunan.ttl` hanya berisi 6 triple hasil kesimpulan. Setelah taksonomi diubah, saya menjalankan ulang aturan pada `kampus.ttl` yang baru ke graf kosong, lalu membandingkan hasilnya dengan berkas turunan lama. Triple yang hanya ada di berkas lama adalah triple basi. Triple itu harus dihapus secara manual, atau berkas turunan dibuat ulang, karena `materialisasi()` hanya menambah triple dan tidak pernah menarik kembali kesimpulan lama. Pemisahan berkas inilah yang membuat pembersihan itu mungkin dilakukan.

### Diskusi 2 - SELECT atau CONSTRUCT
Untuk dashboard populasi kota saya memakai CONSTRUCT di tahap penggabungan data, lalu SELECT di tahap penyajian. Dashboard yang menampilkan angka membutuhkan tabel baris dan kolom, jadi SELECT cocok untuk itu. Namun data kota berasal dari tiga sumber dengan skema berbeda, sehingga CONSTRUCT lebih tepat untuk menyeragamkannya ke satu template graf (`a ex:Kota`, `rdfs:label`, `ex:populasi`) yang disimpan sekali dan diolah secara lokal. Temuan Bagian A menunjukkan perlunya kehati-hatian: `LIMIT 10` menghasilkan [N] triple, bukan 30, karena satu kota muncul di beberapa baris akibat punya beberapa nilai populasi (P1082). Triple kembar menyatu, tetapi nilai populasi yang berbeda tetap menjadi triple terpisah. Jika langsung ditampilkan, kota yang sama akan muncul dengan angka ganda. Temuan `rusak_b.rq` menambah risiko lain: nama yang sama dari tiga predikat dengan tag bahasa atau tipe data berbeda dihitung sebagai nilai berbeda. Pada tiga sumber, satu kota bisa tampil dengan beberapa nama yang tampak sama. Karena itu template CONSTRUCT harus menormalkan nilai, misalnya dengan `STR()` atau `FILTER(LANG(?nama) = "id")`, dan memilih satu populasi per kota. Dengan graf yang sudah bersih, SELECT di dashboard cukup sederhana dan tidak membebani endpoint.

### Cek diri
| Pernyataan | Bukti dari tugas ini |
|------------|----------------------|
| 1 | Bagian A: `LIMIT 10` menghasilkan [N] triple, bukan 30 (3 pola × 10 solution), karena satu kota muncul di beberapa baris SELECT akibat punya beberapa nilai populasi, dan triple kembar (`a ex:Kota`, `rdfs:label`) digabung menjadi satu. |
| 2 | Bagian B: `demo_c.py` menghasilkan 48 triple untuk 16 film tanpa tanggal (16 × 3), tanpa satu pun `schema:datePublished` dan tanpa pesan error. Bagian D: `rusak_a.rq` menghasilkan [N] triple karena `?film` di template tidak terikat oleh WHERE (`?f`). |
| 3 | Bagian D: `rusak_b.rq` memakai jalur `foaf:name\|rdfs:label\|schema:name` dan `VALUES` untuk tiga orang, sehingga nama dari tiga predikat berbeda terkumpul dan menghasilkan [N] triple, bukan 3. |
| 4 | Bagian C: aturan `a/rdfs:subClassOf*` pada putaran 1 menemukan 7 triple, 4 di antaranya baru, tanpa menyebut kedalaman hierarki. Bagian D: `rusak_c.rq` baru menghasilkan 3 triple (Medan, Surabaya, Tomok) setelah ditambah `rdfs:subClassOf*`. |
| 5 | Bagian C: `demo_d.py` menunjukkan `Ada Rina: 3` karena materialisasi hanya berlaku saat dijalankan, lalu `materialisasi_ulang.py` baru menghasilkan `Putaran 2 \| Person: 4` setelah aturan dijalankan ulang. Triple turunan (6) disimpan terpisah di `kampus_turunan.ttl`. |