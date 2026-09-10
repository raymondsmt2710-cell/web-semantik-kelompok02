# Latihan Pertemuan 3 - JSON-LD dan Structured Data

## Identitas
- Nama: ISI_NAMA
- NIM: ISI_NIM

## Struktur Hasil
- `profil_saya.jsonld`
- `profil_perbaikan.jsonld`
- `seminar.html`
- folder `screenshots`

## 1. JSON Biasa dan JSON-LD
1. Perbedaan fungsi kunci: ...
2. Fungsi `@context`, `@type`, dan `@id`: ...
3. Node tanpa `@id`: ...

## 2. Pemeriksaan schema.org
1. Mengapa tipe yang paling spesifik dan masih tepat sebaiknya dipilih?
jawaban: 
    Agar data lebih jelas dan sesuai dengan jenis entitas yang dijelaskan, sehingga lebih mudah dipahami oleh mesin.
2. Mengapa nama properti mengikuti schema.org, sedangkan nilainya boleh berbahasa Indonesia?
jawaban:
    Karena nama properti seperti name, alumniOf, dan knowsAbout harus mengikuti standar schema.org agar dapat dikenali mesin. Nilainya bebas menggunakan bahasa Indonesia sesuai isi data.
3. Apa manfaat array pada knowsAbout?
jawaban:
    Array memungkinkan kita memasukkan dan menyimpan lebih dari satu topik yang diketahui atau dikuasai oleh seseorang.

## 3. Perbaikan Lima Kesalahan
| No. | Bagian Salah | Alasan | Perbaikan |
|---|---|---|---|
| 1 | ... | ... | ... |
| 2 | ... | ... | ... |
| 3 | ... | ... | ... |
| 4 | ... | ... | ... |
| 5 | ... | ... | ... |

## 4. Triple dari JSON-LD Playground
Tuliskan satu baris N-Quads yang terbentuk:

```text
<https://usu.ac.id/mhs/251402113> <http://schema.org/alumniOf> _:b0 .
```

## 5. Hasil Validasi
- Schema Markup Validator: ...
- Rich Results Test: ...
- JSON-LD Playground: ...

## 6. Refleksi
1. Mengapa `@context` disebut jembatan menuju makna?
2. Apa perbedaan fungsi Schema Markup Validator dan Rich Results Test?
3. Mengapa isi JSON-LD harus sama dengan konten yang terlihat pada halaman?

## Bukti
![Schema Markup Validator](screenshots/profil-schema-validator.png)
![JSON-LD Playground](screenshots/profil-playground.png)
![Rich Results Test](screenshots/seminar-rich-results.png)