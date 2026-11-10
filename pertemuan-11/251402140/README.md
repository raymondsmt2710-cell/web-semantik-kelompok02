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
- Mengapa Ada Rina bernilai 3: karena triple turunan hanya dibuat sekali, seblum Rina masuk, sehingga ex:rina a foaf:Person belum pernah ada. Query tidak membaca rdfs:subClassOf, jadi Rina tidak terhitung dan hasilnya tetap 3.
- Output materialisasi_ulang.py: Putaran 1: 4 triple baru | Person: 3, Rina masuk | Person: 3, Putaran 2 | Person: 4, Triple turunan disimpan terpisah: 6
- Tiga triple yang bukan baru: 3 triple yg bukan baru adalah ex:sari a ex:Dosen, ex:andi a ex:Mahasiswa, dan ex:budi a ex:DosenTetap. Ketiga triple sudah ada di kampus.ttl. Triple itu tercetak oleh bagian rdfs:subClassOf* yang boleh 0 langkah. Pada 0 langkah, hasilnya adalah kelas asli individu itu sendiri, jadi sama dengan triple awal
- Kegunaan kampus_turunan.ttl dan langkah manual yang tersisa: berisi hasil kesimpulan, sedangkan data aslinya ada di kampus.ttl. Kalau ex:Dosen tidak lagi menjadi subKelas foaf:Person, maka foaf:Person milik budi, sari, dan rina menjadi salah. Karena kesimpulan terpisah, saya bisa menghapusnya tanpa mengubah data asli. Yang harus saya lakukan sendiri mengubah hubungan kelas di kampus.ttl, menghapus kesimpulan lama dari graf, lalu menjalankan materialisasi_ulang.py lagi.

## Bagian D - Diagnosis
| Query | Hasil mesin | Gejala | Penyebab (baris yang salah) | Hasil setelah diperbaiki |
|-------|-------------|--------|-----------------------------|--------------------------|
| rusak_a | [isi] | [isi] | [isi] | [isi] |
| rusak_b | [isi] | [isi] | [isi] | [isi] |
| rusak_c | [isi] | [isi] | [isi] | [isi] |

## Bagian E - Etika dan diskusi
| Aturan | a_kota_limit.rq | demo_c.py |
|--------|-----------------|-----------|
| 1 User-Agent | [isi] | [isi] |
| 2 LIMIT | [isi] | [isi] |
| 3 Simpan, jangan ulangi | [isi] | [isi] |
| 4 Jangkar jalur | [isi] | [isi] |
- Versi yang melanggar aturan 4 (tidak dijalankan) dan alasannya: [isi]

### Diskusi 1 - Taksonomi berubah
[150-250 kata]

### Diskusi 2 - SELECT atau CONSTRUCT
[150-250 kata]

### Cek diri
| Pernyataan | Bukti dari tugas ini |
|------------|----------------------|
| 1 | [isi] |
| 2 | [isi] |
| 3 | [isi] |
| 4 | [isi] |
| 5 | [isi] |