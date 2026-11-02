## Langkah 1 – Perbandingan Serialisasi RDF

| Format | Kekuatan utama | Skenario tepat |
|---|---|---|
| Turtle | Ringkas dan mudah dibaca manusia | Menulis dan menyunting graf secara manual, dokumentasi, materi ajar, serta ontologi kecil–menengah yang sering dibaca orang. Prefix dan singkatan (`;`, `,`, `a`) membuat struktur graf mudah dipahami. |
| JSON-LD | Cocok web/API dan HTML | Menyajikan data lewat REST API atau menyisipkan metadata ke halaman web (`<script type="application/ld+json">`, misalnya schema.org untuk SEO). Developer web bisa memakainya sebagai JSON biasa tanpa memahami RDF. |
| RDF/XML | Kompatibilitas data lama | Bertukar data dengan sistem atau tool lama yang hanya menerima RDF/XML (misalnya ontologi OWL lawas, beberapa versi Protégé, atau repositori yang dibangun di era awal Web Semantik). |
| N-Triples | Satu triple per baris; stabil untuk diff | Version control (git diff), pemrosesan streaming dan bulk loading dataset besar ke triple store, serta pengolahan baris per baris dengan `grep`, `sort`, atau `split`. Tidak ada prefix sehingga tiap baris berdiri sendiri. |
| N-Quads | Menambahkan konteks graf | Mengekspor atau memuat dataset yang terdiri dari beberapa named graph (misalnya data kampus dan fakultas dari sumber berbeda) sambil tetap menyimpan asal graf setiap triple. Cocok untuk dump/backup triple store. |

**Catatan:** JSON-LD tidak selalu paling tepat. Pemilihan format didasarkan pada siapa konsumen datanya:
- manusia → Turtle,
- aplikasi web/API → JSON-LD,
- sistem lama → RDF/XML,
- mesin dan git → N-Triples,
- data multi-graf → N-Quads.
