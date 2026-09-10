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
| 1 | `"@type": "person"` | Penulisan tipe `Person` pada Schema.org bersifat case-sensitive. | Ubah menjadi `"@type": "Person"` |
| 2 | `'name': "Rina Anggraini"` | JSON menggunakan tanda kutip ganda (`"`), seharusnya menggunakan tanda kutip tunggal (`'`). | Ubah menjadi `"name": "Rina Anggraini"` |
| 3 | `"birthDate": "12 September 2004"` | Format tanggal tidak menggunakan standar ISO 8601. | Ubah menjadi `"birthDate": "2004-09-12"` |
| 4 | `"nomorInduk": "221401001"` | `nomorInduk` bukan tipe yang terdaftar di Schema.org. | Menghapus `nomorInduk` |
| 5 | Koma di properti terakhir | JSON tidak boleh memiliki koma setelah properti terakhir. | Koma setelah `birthDate` dihapus |

## 4. Triple dari JSON-LD Playground
Tuliskan satu baris N-Quads yang terbentuk:

```text
ISI_TRIPLE
```

## 5. Hasil Validasi
- Schema Markup Validator: ...
- Rich Results Test: ...
- JSON-LD Playground: ...

## 6. Refleksi
1. Mengapa `@context` disebut jembatan menuju makna?   
**Jawaban:** Karena `@context` menghubungkan istilah dalam JSON-LD dengan schema yang memiliki makna tertentu, seperti Schema.org. Dengan begitu, mesin atau komputer dapat memahami arti dari setiap data.

2. Apa perbedaan fungsi Schema Markup Validator dan Rich Results Test?  
**Jawaban:** Schema Markup Validator digunakan untuk memeriksa apakah struktur dan sintaks Schema Markup sudah benar, sedangkan Rich Results Test digunakan untuk mengetahui apakah data terstruktur dapat memenuhi syarat untuk ditampilkan sebagai rich result di Google.

3. Mengapa isi JSON-LD harus sama dengan konten yang terlihat pada halaman?  
**Jawaban:** Agar informasi yang diberikan kepada mesin pencari sesuai dengan informasi yang dilihat oleh pengguna. Jika berbeda, data terstruktur dapat dianggap menyesatkan dan berpotensi tidak digunakan oleh mesin pencari.

## Bukti
![Schema Markup Validator](screenshots/profil-schema-validator.png)
![JSON-LD Playground](screenshots/profil-playground.png)
![Rich Results Test](screenshots/seminar-rich-results.png)