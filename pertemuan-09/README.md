# Pertemuan 9 - SPARQL Dasar: Tell & Ask dan Endpoint

## Langkah 1 - Tabel binding
| Tahap | ?dosen | ?mk | ?namaMK |
|Pola 1,baris 1|ex:budi|ex:tif2305|---------|
|Pola 1, baris lain|ex:sari (dan ex:sari)|ex:tif2410 (dan ex:tif2305)|---------|
|Pola 2|--------|ex:tif2305 (dan ex:tif2410)|"Web Semantik" (dan "Data Mining")|
|Hasil akhir|ex:budi, ex:sari, ex:sari|ex:tif2305, ex:tif2410, ex:tif2305|"Web Semantik", "Data Mining","Web Semantik"|

- Jumlah baris hasil akhir: 3 baris.
- Peran ?mk:karena ?mk tidak ada di SELECT, tapi muncul di kedua pola sehingga jadi penghubung join. Hanya baris dengan ?mk yang sama di kedua pola yang lolos.

## Langkah 2 - ASK dan dunia terbuka
1. [jawaban]
2. [jawaban]
3. [jawaban]

## Langkah 3 - Query lokal
- IRI dasar graf: https://contoh.github.io/web-semantik/251402113/kampus# (dibaca otomatis dari prefix ex: di ../pertemuan-06/kampus_usu.ttl)
- Jumlah triple awal / akhir: 10 / 12
- Fakta yang ditambahkan:
    1. ex:ida ex:mengajar ex:tif3501 .
    2. ex:tif3501 foaf:name "Rekayasa Ontologi"@id .

## Langkah 4 - Wikidata
- Jumlah baris Q1 dengan wdt:P31: [20]
- Jumlah baris Q1 dengan wdt:P31/wdt:P279*: [20]
- Penjelasan perbedaan: [Jumlah hasil yang ditampilkan tetap 20 baris karena query menggunakan LIMIT 20 artinya hasil yang ditampilkan dibatasi maksimal 20 baris.
    - wdt:P31 wd:Q3918 berfungsi untuk mencari universitas yang secara langsung memiliki tipe university.
    - Sedangkan wdt:P31/wdt:P279* wd:Q3918 juga menelusuri hubungan kelas turunan (subclass) dari university. Karena itu, hasil pencarian bisa mencakup institusi pendidikan yang lebih spesifik yaitu politeknik yang artinya klasifikasinya terhubung ke kelas university melalui hubungan subclass di Wikidata.]

## Langkah 5 - Endpoint dari Python
- agent=UA: [isi]
- setReturnFormat(JSON): [isi]
- b.get("kotaLabel", {}): [isi]

## Refleksi
1. Di titik mana SPARQL berbeda dari SQL?
2. Kapan Anda memakai graf lokal (rdflib) dan kapan endpoint publik?
3. Sebutkan satu hasil query yang mengejutkan dan jelaskan penyebabnya.
