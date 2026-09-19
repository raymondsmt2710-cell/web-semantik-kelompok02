# Pertemuan 4 — Metadata dan Interoperabilitas

## Identitas sumber
- Judul: An Introduction to Computer Networks, 2nd Edition
- Pembuat: Peter L. Dordal
- URI sumber: https://ecommons.luc.edu/facultybooks/189/
- Jenis sumber: Text / LearningResource

## Pemetaan Dublin Core Terms
| Properti | Nilai | Alasan pemilihan |
| --- | --- | --- |
| dcterms:title | An Introduction to Computer Networks, 2nd Edition | Judul adalah identitas utama sumber; tanpa properti ini sumber tidak dapat dikenali atau dirujuk secara unik dalam katalog maupun daftar pustaka. |
| dcterms:creator | Peter L. Dordal | Menyatakan pihak yang secara intelektual bertanggung jawab atas isi buku (penulis), sehingga atribusi akademik dan sitasi menjadi jelas dan dapat dipertanggungjawabkan. |
| dcterms:description | Buku pembelajaran yang membahas dasar-dasar jaringan komputer, termasuk LAN, internetworking, TCP/IP, transport layer, keamanan jaringan, dan manajemen jaringan. | Memberi ringkasan cakupan materi sehingga pengguna dapat menilai relevansi sumber dengan cepat tanpa harus membuka seluruh dokumen. |
| dcterms:created | 2020-07 | Menunjukkan periode pembuatan konten, penting untuk menilai kekinian materi teknis yang berkembang cepat seperti jaringan komputer. |
| dcterms:type | Text / LearningResource | Mengklasifikasikan sifat sumber agar sistem temu kembali (search/filter) dapat mengenali jenis dokumen secara terstruktur. |
| dcterms:language | en | Menentukan bahasa penyajian sumber, krusial bagi pengguna yang mencari materi dalam bahasa tertentu. |
| dcterms:rights | CC BY-NC-ND 3.0 | Menyatakan lisensi dan batasan penggunaan ulang (non-komersial, tanpa turunan) sejak awal, sehingga hak pakai jelas bagi siapa pun yang mengakses sumber. |

## Hasil validasi
- JSON-LD Playground: Dokumen JSON-LD berhasil di-parse tanpa error sintaks; struktur `@context` (mengarah ke `http://purl.org/dc/terms/`) dan `@id` (URI sumber) terbaca dengan benar, dan tab "Expanded"/"N-Quads" menampilkan triple yang sesuai dengan pemetaan properti di atas.
- Schema Markup Validator: Markup terdeteksi valid tanpa error kritis; seluruh properti terbaca sebagai item terstruktur. Tidak ditemukan warning yang berkaitan dengan properti wajib, karena field inti (nama, deskripsi, tipe) telah dilengkapi.

## Refleksi
1. **Mengapa URI yang sama penting untuk Turtle dan JSON-LD?**
   URI yang sama memastikan kedua serialisasi merujuk pada entitas (sumber) yang identik, sehingga data dari format berbeda dapat digabungkan (linked) dan dianggap sebagai satu sumber yang sama oleh mesin maupun sistem lain, bukan dua entitas terpisah.

2. **Apa perbedaan peran DC Terms dan schema.org pada pekerjaan ini?**
   DC Terms berfungsi sebagai standar deskripsi metadata generik untuk sumber daya (dokumen, buku, materi pembelajaran) yang umum dipakai di dunia perpustakaan dan akademik, sedangkan schema.org menambahkan kosakata yang lebih spesifik dan dipahami langsung oleh mesin pencari (search engine) untuk keperluan rich snippet dan penemuan konten di web.

3. **Sebutkan satu risiko jika metadata HTML, Turtle, dan JSON-LD tidak konsisten.**
   Jika ketiga format menyajikan nilai yang berbeda untuk properti yang sama (misalnya judul atau pembuat berbeda), mesin pencari maupun sistem pengindeks dapat menampilkan informasi yang saling bertentangan atau keliru, sehingga menurunkan kepercayaan dan akurasi temu kembali sumber tersebut.

## Catatan akhir
Metadata sumber ini disusun agar konsisten di tiga representasi (HTML, Turtle, JSON-LD) dengan menggunakan URI sumber yang sama sebagai penanda identitas tunggal. Konsistensi nilai pada properti inti (title, creator, description, created, type, language, rights) dijaga di seluruh format agar interoperabilitas antar sistem tetap terjamin dan tidak menimbulkan ambiguitas saat data digabungkan atau diproses ulang oleh aplikasi lain.
