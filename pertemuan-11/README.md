# Pertemuan 11 - CONSTRUCT dan Hierarki Data

## Langkah 1 - Solution menjadi triple
| Solution | ?d | ?mk | Triple yang dicetak |
|----------|----|-----|---------------------|
| [isi]    | [isi] | [isi] | [isi]           |
- Jumlah solution: [isi]
- Jumlah cetakan triple: [isi]
- Jumlah triple di graf hasil: [isi]
- Triple yang tercetak lebih dari sekali: [isi]

## Langkah 2 - Tebak lalu cek
| Soal | Tebakan | Hasil mesin | Penjelasan bila meleset |
|------|---------|-------------|-------------------------|
| A    | [isi]   | [isi]       | [isi]                   |
| B    | [isi]   | [isi]       | [isi]                   |
| C    | [isi]   | [isi]       | [isi]                   |
| D    | [isi]   | [isi]       | [isi]                   |

## Langkah 3 - Graf kampus lokal
- Berkas sumber dan IRI dasar graf: pertemuan-09/kampus_usu_v2.ttl dengan IRI dasar https://contoh.github.io/web-semantik/251402113/kampus#.
- Kelas dosen dan properti nama: ex:Lecturer dan foaf:name.
- Triple hasil pemetaan: 2 triple, yaitu pemetaan individu dosen ex:ida menjadi schema:Person dan pemetaan namanya menjadi schema:name.
- foaf:Person sebelum / sesudah: 0 / 1
- Triple asli vs triple turunan: Triple asli merupakan triple yang sudah tersedia di graf sumber, sedangkan triple turunan merupakan triple baru yang dihasilkan melalui hierarki kelas. Pada proses ini, ex:ida memperoleh tipe ex:Pegawai dan foaf:Person melalui hierarki ex:Lecturer -> ex:Pegawai -> foaf:Person.
- Dosen baru setelah program selesai: Dosen baru tidak otomatis memperoleh tipe foaf:Person karena proses materialisasi hanya dilakukan ketika program dijalankan. Untuk memasukkan dosen baru ke dalam hasil inferensi, graf harus diperbarui dan program dijalankan kembali.

## Langkah 4 - Wikidata
- Jumlah triple Q6: [isi]
- Jumlah baris Q6 versi SELECT: [isi]
- Penjelasan perbedaan: [isi]
- Q7 dengan + vs *: [isi]
- Kelas yang mengejutkan dan alasannya: [isi]

## Langkah 5 - Graf dari Python
- Jumlah triple universitas.ttl: [isi]
- Jumlah baris universitas_per_kota.csv: [isi]
- setReturnFormat(TURTLE): [isi]
- Graph().parse(data=...): [isi]
- Mengapa q_kota tidak memanggil endpoint: [isi]

## Refleksi
1. Mengapa jumlah triple hasil CONSTRUCT bisa lebih kecil dari jumlah baris SELECT dengan WHERE yang sama?
2. Bila taksonomi di graf kampus Anda berubah bulan depan, apa yang terjadi pada triple turunan di kampus_usu_v4.ttl?
3. Kapan Anda menyimpan hasil query sebagai tabel (CSV), dan kapan sebagai graf (Turtle)?