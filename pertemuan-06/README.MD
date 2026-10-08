# Pertemuan 6 - RDF Dasar

## IRI dasar graf
[isi IRI dasar]

## Ringkasan graf
- Jumlah triple: [isi]
- Namespace yang digunakan: [isi]
- Entitas: [isi]

## Contoh triple
1. `ex:ida` - `rdf:type` - `ex:Lecturer`
2. `ex:ida` - `ex:teaches` - `ex:WebSemantik`
3. `ex:WebSemantik` - `ex:name` - `"Web Semantik"`

## Perbandingan serialisasi
- Turtle: memakai sintaks yang ringkas dan mudah dibaca, penanda 'a' untuk menyatakan kelas entitas
- JSON-LD: memakai struktur data json dengan objek '@context' untuk atribut ke IRI/URI RDF
- Pernyataan yang sama: jika turtle pernyataanya ditulis secara ringkas menggunakan prefix, sedangkan json-ld pernyataannya ditulis dalam struktur objek

## Langakah 2
1.Identifikasi jenis node untuk ex:ida, "Ida Adi"@id, dan [ ex:kota "Medan" ].  
=> 1.ex:ida adalah IRI
   2."Ida Adi"@id adalah literal (bertag bahasa)
   3._:b1 adalah blank node. Blank node berarti sesuatu ada, tetapi tidak punya IRI.

2.Mengapa literal tidak boleh menjadi subject RDF?  
=> Subject harus berupa sesuatu yang bisa diidentifikasi dan dirujuk (IRI atau blank node). Literal hanyalah nilai, bukan entitas, sehingga tidak bisa "memiliki properti".

3.Buat IRI dasar untuk graf Anda dengan pola HTTP, misalnya https://contoh.github.io/web-semantik/ISI_NIM/kampus#.  
=> https://raymondsmt2710-cell.github.io/web-semantik-kelompok02/WS_251402078/usu#

4.Tuliskan kepanjangan namespace rdf, rdfs, xsd, dan foaf.  
=> 1.Resource Description Framework|http://www.w3.org/1999/02/22-rdf-syntax-ns#
   2.Resource Description Framework Schema |http://www.w3.org/2000/01/rdf-schema#
   3.XML Schema Definition |http://www.w3.org/2001/XMLSchema#
   4.Friend of a Friend |http://xmlns.com/foaf/0.1/


## Refleksi
1. Kapan object harus berupa IRI dan kapan berupa literal?  
=>Object berupa **IRI** jika ia adalah entitas yang bisa menjadi subject di triple lain, misalnya `ex:web_semantik` pada `ex:ida ex:mengajar ex:web_semantik`. Object berupa **literal** jika ia hanya nilai akhir, seperti nama, angka, atau tanggal, misalnya `"Web Semantik"@id` atau `"3"^^xsd:integer`.

2. Mengapa prefix membantu keterbacaan tanpa mengubah IRI?  
=>Prefix hanya singkatan dari namespace yang panjang. `ex:ida` lebih mudah dibaca, tetapi tetap diperluas menjadi IRI lengkap yang sama, sehingga identitas dan makna data tidak berubah.


3. Sebutkan satu kesalahan pemodelan yang Anda hindari pada graf ini.  
=>Saya menghindari penulisan entitas sebagai string, misalnya `ex:ida ex:mengajar "Web Semantik"`. Mata kuliah dimodelkan sebagai IRI (`ex:web_semantik`) agar bisa dihubungkan dengan triple lain seperti nama, SKS, dan mahasiswa yang mengambilnya.