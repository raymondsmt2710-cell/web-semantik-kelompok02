# Pertemuan 5 - Ontology dan Arsitektur Web Semantik

## Ontology mini kampus
- IRI dasar: https://kelas.usu.ac.id/ontology#
- Domain: Universitas Sumatera Utara

## Komponen ontology
| Komponen | Isi yang dibuat |
| --- | --- |
| Class | Person, Course, Department, Faculty, Room, Semester |
| Subclass | Student subClassOf Person, Lecturer subClassOf Person, UndergraduateStudent subClassOf Student |
| Object property | Teaches |
| Datatype property | hasCredit |
| Individual | mahasiswa_anda bertipe Student, dosen_anda bertipe Lecturer, matkul_ws bertipe Course |
| Axiom/disjointness | Student disjointWith Lecturer |

## Layer Cake
Jelaskan posisi ontology dalam Semantic Web Layer Cake: [isi jawaban]

## Perbandingan serialisasi
- Turtle: [dua pengamatan sintaks]
- RDF/XML: [dua pengamatan sintaks]
- Kesamaan makna: [isi]

## Refleksi
1. Apa perbedaan ontology dan taksonomi?
2. Mengapa domain pada OWL bukan constraint database?
3. Mengapa kosakata yang sudah ada sebaiknya dipakai kembali sebelum membuat yang baru?