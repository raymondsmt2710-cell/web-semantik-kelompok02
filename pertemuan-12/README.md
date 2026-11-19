# Pertemuan 12 - Inferensi dan Reasoning

## Langkah 1 - Closure dengan tangan
| # | Triple turunan | Aturan | Premis |
|---|----------------|--------|--------|
| [isi] | [isi] | [isi] | [isi] |
- Jumlah triple turunan bermakna: [isi]
- Triple yang baru ditemukan di putaran kedua: [isi]
- Triple asserted yang tidak menurunkan apa pun, dan alasannya: [isi]

## Langkah 2 - Tebak lalu cek
| Soal | Profil | Tebakan | Hasil mesin | Penjelasan bila meleset |
|------|--------|---------|-------------|-------------------------|
| A | RDFS | [isi] | [isi] | [isi] |
| B | OWL RL | [isi] | [isi] | [isi] |
| C | RDFS | [isi] | [isi] | [isi] |
| C | OWL RL | [isi] | [isi] | [isi] |
| D | OWL RL | [isi] | [isi] | [isi] |

## Langkah 3 - Reasoner pada graf kampus
- Berkas sumber dan IRI dasar graf: ../pertemuan-09/kampus_usu_v2.ttl, https://contoh.github.io/web-semantik/251402113/kampus#
- Asserted / closure / inferred / bermakna: 16 / 56 / 40 / 5
- Triple di v4 yang tidak ada di asserted: 2
- Turunan yang muncul karena domain dan range ex:mengajar: ex:tif3501 a ex:MataKuliah dan ex:web_semantik a ex:MataKuliah, berdasarkan aturan range. Aturan domain juga menyimpulkan ex:ida a ex:Lecturer, tetapi triple tersebut sudah ada di asserted.
- Bila menambah dosen baru: menambahkan data dosen beserta triple ex:mengajar yang menghubungkan dosen dengan mata kuliah. Reasoner akan menghasilkan inferensi berdasarkan schema domain, range, dan subclass secara otomatis.

## Langkah 4 - Wikidata
- ?n Q8 / Q9: 877 / 1343
- Penyebab selisih: Q8 hanya menghitung entitas yang langsung berstatus universitas. Q9 juga menghitung entitas yang bertipe subkelas universitas, karena memakai P31/P279*. Hierarki kelasnya sama untuk kedua query. Bedanya, hanya Q9 yang menelusurinya. Selisihnya 466 universitas yang terhubung lewat subkelas saja
- Satu subkelas yang menyumbang selisih: politeknik. Ada 375 entitas di Indonesia yang bertipe langsung politeknik, dan Wikidata mencatat politeknik sebagai subkelas universitas. Entitas itu tidak terhitung di Q8, tetapi terhitung di Q9 karena jalur P279*. Subkelas lain yang juga muncul adalah universitas swasta dan universitas negeri
- WDQS: materialisasi, saat query, atau tidak keduanya: WDQS tidak melakukan materialisasi. Kalau kesimpulan "bertipe universitas" tersimpan di data, Q8 akan sama dengan Q9, padahal Q8 hanya 877. WDQS juga tidak menalar sendiri. Subkelas baru ditelusuri saat query berjalan, dan itu terjadi karena saya menulis P279*
- Yang menjalankan rdfs9 di Q9: penulis query. Jalur P31/P279* meniru aturan rdfs9 secara manual, dan mesin hanya mengeksekusi jalur itu

## Langkah 5 - Konsistensi
- Pesan galat RDFS / OWL RL: [isi] / [isi]
- Individu yang disebut pesan: [isi]
- Setelah baris terbalik dihapus: [isi]
- Isi laporan_kelas.csv sebelum dan sesudah: [isi]
- Dari mana dosen menjadi mata kuliah: [jawaban]

## Refleksi
1. Mengapa graf asserted disimpan terpisah dari graf inferred, dan apa akibatnya bila keduanya dicampur seperti kampus_usu_v4.ttl?
2. Pada Langkah 2, profil RDFS tidak memberi tahu bahwa aksioma OWL diabaikan. Bagaimana Anda akan memastikan profil yang dipakai sudah tepat untuk data Anda?
3. Kapan Anda memilih menulis jalur seperti wdt:P279* di query, dan kapan memilih menjalankan reasoner lalu menyimpan closure?