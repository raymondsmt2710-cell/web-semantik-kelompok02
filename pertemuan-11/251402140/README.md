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
- Query lokal tanpa internet: ketika seluruh demo_c.py dijalankan tanpa internet, program berhenti di baris 15. Error yg muncul adalah `urllib.error.URLError: <urlopen error [Errno 11001] getaddrinfo failed>`, karena komputer tidak bisa menemukan alamat dbpedia.org. Program berhenti sebelum sampai baris serialize dan baris yang membaca film_nolan.ttl. Jadi kedua baris tidak pernah dijalankan
- Mengapa dbo:Film memberi 0 pada film_nolan.ttl: karena film_nolan.ttl hanya berisi schema:Movie dan tidak ada triple bertipe dbo:Film.

## Bagian C - Materialisasi
- Output demo_d.py: [isi]
- Mengapa Ada Rina bernilai 3: [jawaban]
- Output materialisasi_ulang.py: [isi]
- Tiga triple yang bukan baru: [jawaban]
- Kegunaan kampus_turunan.ttl dan langkah manual yang tersisa: [jawaban]

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