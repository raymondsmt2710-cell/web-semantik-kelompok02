# Pertemuan 11 - Tugas Mandiri: Dari Endpoint ke Graf Lokal

## Bagian A - LIMIT dan triple
- Triple dengan LIMIT 10: 30
- Triple dengan LIMIT 30: 90
- Baris SELECT LIMIT 10 / kota berbeda: 10 / 10
- Mengapa tidak (atau mengapa tepat) 30 triple: karena template construct punya 3 pola sedangkan limit 10 membatasi solution, maka batas atasnya 10x3. Karena itu mengapa tepat 30.

## Bagian B - DBpedia ke Turtle
- Output demo_c.py: 48 triple, film tanpa tanggal: 16
- Sumber data: DBpedia
- Triple yang tetap tercetak untuk film tanpa tanggal: a schema:Movie, schema:name, schema:director
- Query lokal tanpa internet: Q_TANPA_TANGGAL berhasil dijalankan meskipun tanpa internet. Ini karena film_nolan.ttl sudah tersimpan di laptop dan rdflib membacanya langsung ke memori tanpa jaringan. Tapi jika menjalankan seluruhnya tanpa internet, maka akan menghasilkan error `urllib.error.URLError: <urlopen error [Errno 11001] getaddrinfo failed>`.
- Mengapa dbo:Film memberi 0 pada film_nolan.ttl: karena film_nolan.ttl hanya berisi schema:Movie dan tidak ada triple bertipe dbo:Film.

## Bagian C - Materialisasi
- Output demo_d.py: Sebelum: 0, Sesudah: 3, Ada Rina: 3
- Mengapa Ada Rina bernilai 3: karena triple turunan hanya dibuat sekali, sebelum Rina masuk, sehingga ex:rina a foaf:Person belum pernah ada. Query tidak membaca rdfs:subClassOf, jadi Rina tidak terhitung dan hasilnya tetap 3.
- Output materialisasi_ulang.py: Putaran 1: 4 triple baru | Person: 3, Rina masuk | Person: 3, Putaran 2 | Person: 4, Triple turunan disimpan terpisah: 6
- Tiga triple yang bukan baru: 3 triple yg bukan baru adalah ex:sari a ex:Dosen, ex:andi a ex:Mahasiswa, dan ex:budi a ex:DosenTetap. Ketiga triple sudah ada di kampus.ttl. Triple itu tercetak oleh bagian rdfs:subClassOf* yang boleh 0 langkah. Pada 0 langkah, hasilnya adalah kelas asli individu itu sendiri, jadi sama dengan triple awal
- Kegunaan kampus_turunan.ttl dan langkah manual yang tersisa: berisi hasil kesimpulan, sedangkan data aslinya ada di kampus.ttl. Kalau ex:Dosen tidak lagi menjadi subKelas foaf:Person, maka foaf:Person milik budi, sari, dan rina menjadi salah. Karena kesimpulan terpisah, saya bisa menghapusnya tanpa mengubah data asli. Yang harus saya lakukan sendiri mengubah hubungan kelas di kampus.ttl, menghapus kesimpulan lama dari graf, lalu menjalankan materialisasi_ulang.py lagi.

## Bagian D - Diagnosis
| Query | Hasil mesin | Gejala | Penyebab (baris yang salah) | Hasil setelah diperbaiki |
|-------|-------------|--------|-----------------------------|--------------------------|
| rusak_a | 0 triple | Graf kosong, tanpa error | Baris CONSTRUCT { ?film ex:judul ?j . } memakai ?film, padahal WHERE hanya mengikat ?f | 3 triple, satu judul per film Nolan (Following, Insomnia, Memento). Perbaikan: ?film di CONSTRUCT diganti ?f |
| rusak_b | 4 triple | 2 nilai yang tampak sama | Baris ?o foaf:name\|rdfs:label\|schema:name ?n . mengambil dua nama Nolan, satu tanpa tag bahasa dan satu @en | 3 triple, satu ex:nama per orang. Perbaikan: tambah BIND(STR(?n0) AS ?n) sehingga tag bahasa hilang |
| rusak_c | 0 triple | Superkelas tidak ditemukan | Baris ?x a ex:Permukiman . tidak memakai jalur rdfs:subClassOf* | 3 triple: Medan, Surabaya, Tomok. Perbaikan: pola diganti ?x a/rdfs:subClassOf* ex:Permukiman |

## Bagian E - Etika dan diskusi
| Aturan | a_kota_limit.rq | demo_c.py |
|--------|-----------------|-----------|
| 1 User-Agent | tdk relevan, query dijalankan lewat browser di query.wikidata.org | Baris UA="KelasWebSemantik/1.0 (...)" |
| 2 LIMIT | ada LIMIT 10 di baris terakhir | tidak ada LIMIT, tidak perlu karena query terikat ke 1 sutradara (hasilnya 16 film) |
| 3 Simpan, jangan ulangi | tidak relavan, dijalankan sekali untuk eksplorasi | baris `g.serialize("film_nolan.ttl")` menyimpan graf, lalu query kedua dijalankan di berkas lokal |
| 4 Jangkar jalur | `wdt:P31/wdt:P279* wd:Q515` berangkat dari IRI tertentu (Q515) | tidak relavan, tidak ada jalur * atau + |
- Versi yang melanggar aturan 4 (tidak dijalankan) dan alasannya: ganti wd:Q515 di a_kota_limit.rq dengan variabel, misalnya ?kelas, lalu tulis versinya di README. ini mahal harus kedua ujung jalur wdt:P279* jadi variabel, sehingga endpoint harus menelusuri rantai subkelas dari semua item Wikidata, bukan dari satu kelas

### Diskusi 1 - Taksonomi berubah
Kalau hasil materialisasi Demo D disimpan ke graf produksi lalu ex:Dosen tidak lagi subkelas foaf:Person, triple foaf:Person milik budi, sari, dan rina jadi salah. Triple itu dulu benar karena mengikuti jalur subClassOf, tetapi tidak ada yang mencabutnya saat taksonomi berubah. Triple andi a foaf:Person tetap benar karena ex:Mahasiswa masih di bawah foaf:Person. Jadi jumlah Person turun dari 4 menjadi 1.  
  
Untuk menemukannya, saya bandingkan graf produksi dengan taksonomi terbaru. Cara paling mudah: cari semua triple foaf:Person milik individu bertipe ex:Dosen atau ex:DosenTetap, lalu cek apakah masih ada jalur subClassOf yang menghubungkannya. Yang tidak punya jalur itu harus dibuang.  
  
Di sini kampus_v4.ttl menyulitkan. Isinya 16 triple, dan fakta asli bercampur dengan kesimpulan tanpa penanda, jadi saya harus menebak mana yang basi. kampus_turunan.ttl lebih aman: isinya hanya 6 triple hasil materialisasi, sehingga bisa dihapus seluruhnya, lalu aturan dijalankan ulang pada 10 triple asli. Langkah manualnya tetap ada: memperbaiki hubungan subClassOf di data asli, lalu menjalankan materialisasi_ulang.py lagi.

### Diskusi 2 - SELECT atau CONSTRUCT
Untuk dashboard populasi kota saya pakai SELECT, karena dashboard butuh baris dan angka. Di Bagian A, SELECT LIMIT 10 menghasilkan 10 baris untuk 10 kota berbeda, langsung cocok untuk tabel atau grafik. Hasil CONSTRUCT saya 30 dan 90 triple, tepat 10 x 3 dan 30 x 3, jadi di data Wikidata saya tidak menemukan kota dengan populasi kembar. Contohnya ada di kota.ttl: Medan punya dua nilai, 2435252 dan 2097610. Dengan SELECT, Medan muncul dua baris dan bisa terhitung dua kali di dashboard, jadi saya harus memilih satu nilai dulu.  
  
Untuk menggabungkan data kota dari tiga sumber saya pakai CONSTRUCT, karena hasilnya graf dengan predikat seragam seperti ex:populasi dan rdfs:label. rusak_b menunjukkan perlunya normalisasi: foaf:name, rdfs:label, dan schema:name dipetakan ke satu ex:nama, tetapi hasilnya 4 triple karena “Christopher Nolan” tanpa tag dan “Christopher Nolan”@en dianggap beda. Setelah STR() hasilnya 3 triple. Dengan tiga sumber, perbedaan tag bahasa seperti ini pasti sering muncul. Nilai yang benar-benar beda, seperti dua populasi Medan, tidak akan menyatu dan tetap harus diputuskan manual.

### Cek diri
| Pernyataan | Bukti dari tugas ini |
|------------|----------------------|
| 1 | Bagian A: LIMIT 10 menghasilkan 30 triple dan LIMIT 30 menghasilkan 90, tepat 10 x 3 dan 30 x 3, artinya template dicetak sekali per solution. Di data saya tidak ada triple yang tergabung. Bukti penggabungan ada di rusak_b: setelah STR(), dua nama Christopher Nolan menjadi satu triple, sehingga 4 triple menjadi 3 |
| 2 | rusak_a menghasilkan 0 triple tanpa error karena ?film di template tidak terikat di WHERE. Pada demo_c.py, 16 film tidak punya dbo:releaseDate, sehingga tiap film hanya mencetak 3 triple (16 x 3 = 48) tanpa schema:datePublished, juga tanpa error |
| 3 | rusak_b memakai VALUES untuk tiga orang dan jalur foaf:name|rdfs:label|schema:name untuk menyatukan tiga predikat ke satu ex:nama. Hasilnya 4 triple untuk 3 orang |
| 4 | perbaikan_c memakai ?x a/rdfs:subClassOf* ex:Permukiman dan menghasilkan 3 triple (Medan, Surabaya, Tomok) tanpa menyebut ex:Kota, ex:Desa, atau ex:KotaMetropolitan. Versi rusak_c tanpa jalur menghasilkan 0 |
| 5 | Person tetap 3 setelah Rina masuk, lalu menjadi 4 pada putaran 2 setelah aturan dijalankan ulang. Kesimpulannya tersimpan di kampus_turunan.ttl (6 triple), tetapi harus dihitung ulang tiap ada data baru |