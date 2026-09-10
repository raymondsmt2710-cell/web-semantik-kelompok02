# Pertemuan 2 - Format Dokumen XML

## 1. Profil XML
Struktur XML-nya seperti ini:

1. Deklarasi XML — `<?xml version="1.0" encoding="UTF-8"?>` di baris pertama, wajib ada dan menyatakan versi serta encoding dokumen.
2. Komentar — `<!-- Profil mahasiswa Web Semantik -->` sebagai keterangan, tidak memengaruhi data.
3. Root element — `<profilMahasiswa>`, satu-satunya elemen akar yang membungkus seluruh data (syarat XML well-formed, dimana hanya boleh ada satu root).
4. Element `<profil>` — muncul berulang (5 kali), satu untuk tiap mahasiswa, dengan atribut `nim` berisi Nomor Induk Mahasiswa masing-masing.
5. Child elements di dalam setiap `<profil>`:
   - `<nama>` — nama lengkap mahasiswa
   - `<angkatan>` — tahun angkatan
   - `<programStudi>` — program studi
   - `<hobi>` — muncul dua kali per profil (elemen berulang, karena tiap orang punya 2 hobi)
   - `<deskripsi>` — deskripsi singkat, ditulis dalam blok teks

Semua tag dibuka-tutup dengan benar dan bersarang (nested) secara konsisten, sehingga dokumen memenuhi syarat **well-formed XML**.

## 2. Analisis Kesalahan XML

| No | Bagian yang Salah | Alasan | Perbaikan |
|---|---|---|---|
| 1 | `<nama>Budi Santoso</Nama>` | XML bersifat **case sensitive**, sehingga tag `<nama>` dan `</Nama>` dianggap berbeda. | `<nama>Budi Santoso</nama>` |
| 2 | `<angkatan>2024` | Tag `<angkatan>` tidak memiliki **tag penutup**. | `<angkatan>2024</angkatan>` |
| 3 | `<deskripsi>Saya suka AI & Web Semantik</deskripsi>` | Karakter `&` merupakan karakter khusus dalam XML. Harusnya menggunakan &amp; | `<deskripsi>Saya suka AI &amp; Web Semantik</deskripsi>` |

## 3. Analisis XML Schema
1. Root element: `buku`
2. Tipe data judul: `xs:string`
3. Tipe data tahun: `xs:gYear`
4. Tipe data harga: `xs:decimal`
5. Atribut ISBN: Wajib dituliskan karena menggunakan `use="required"`

## 4. Analisis Namespace
1. Mengapa kedua elemen title tidak sama? 
jawaban:
    Kedua elemen title tersebut tidak dianggap sama karena masing-masing menggunakan namespace yang berbeda.Walaupun nama lokal elemennya sama-sama title, namespace-nya   berbeda sehingga keduanya dianggap sebagai elemen yang berbeda.
2. Apa fungsi prefix buku: dan web:?
jawaban:
    Prefix buku: dan web: digunakan sebagai penanda atau identitas namespace yang digunakan oleh suatu elemen. Dengan adanya prefix tersebut, XML dapat membedakan elemen yang memiliki nama sama tetapi berasal dari namespace yang berbeda.
3. Apa fungsi atribut xmlns?
jawaban:
    Atribut xmlns digunakan untuk mendeklarasikan namespace dalam dokumen XML.
4. Apakah URI namespace harus dapat dibuka sebagai halaman web? Jelaskan.
jawaban:
    Tidak harus. Karena URI namespace berfungsi sebagai identifier (pengenal) unik untuk membedakan satu namespace dengan namespace lainnya, bukan sebagai alamat halaman web yang harus dapat diakses. Oleh karena itu, URI namespace tidak wajib memiliki halaman web atau konten yang dapat dibuka melalui browser.

## 5. Pertanyaan Evaluasi
1. Apa perbedaan utama XML dan HTML?
jawaban:
    XML digunakan untuk menyimpan dan mengatur data, sedangkan HTML digunakan untuk menampilkan data di halaman web.
2. Apa yang dimaksud dokumen XML yang well-formed?
jawaban:
    Well-formed berarti penulisan XML sudah mengikuti aturan dasar XML. Contohnya, setiap tag yang dibuka harus ditutup dan penulisan tag harus benar.
3. Jelaskan perbedaan well-formed dan valid.
jawaban:
    Well-formed berarti struktur dan penulisan XML sudah benar. Sedangkan Valid berarti XML tersebut selain sudah well-formed, juga mengikuti aturan atau struktur yang sudah ditentukan, misalnya menggunakan DTD atau XSD.   
4. Mengapa XSD lebih kuat dibandingkan DTD?
jawaban:
    Karena XSD dapat mengatur tipe data dengan lebih lengkap, seperti teks, angka, tanggal, dan lainnya. XSD juga menggunakan format XML sehingga lebih fleksibel dibandingkan DTD.
5. Mengapa namespace penting ketika data XML berasal dari beberapa kosakata berbeda?
jawaban:
    Namespace penting untuk membedakan elemen yang memiliki nama yang sama tetapi memiliki arti yang berbeda. Misalnya ada dua title dari sumber yang berbeda, namespace dapat menunjukkan bahwa keduanya berasal dari kosakata yang berbeda.
6. Apa kegunaan XPath dalam pengolahan dokumen XML?
jawaban:
    XPath digunakan untuk mencari atau memilih bagian tertentu dari dokumen XML. Misalnya, kita ingin mengambil semua elemen title atau mencari data tertentu berdasarkan strukturnya.
