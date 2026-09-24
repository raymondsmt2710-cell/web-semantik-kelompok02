# Semantic Web Layer Cake

| Lapis | Peran | Contoh Anda |
| --- | --- | --- |
| URI dan Unicode | Identitas global dan representasi karakter | URI sumber `https://ecommons.luc.edu/facultybooks/189/` dan encoding UTF-8 pada HTML |
| XML | Sintaks pertukaran data | XML digunakan untuk menyusun dan bertukar data secara terstruktur |
| RDF dan RDFS | Pernyataan graph dan kosakata dasar | RDF/Turtle pada `metadata-sumber.ttl` dengan properti `dcterms:title`, `dcterms:creator`, dan lainnya |
| Ontology / OWL | Makna domain dan penalaran lebih kaya | OWL digunakan untuk mendefinisikan kelas, properti, dan hubungan antarentitas dalam suatu domain |
| SPARQL | Query graph RDF | SPARQL digunakan untuk mencari atau mengambil informasi dari graph RDF berdasarkan pola triple |
| Rules, Proof, Trust | Aturan, pembuktian, dan kepercayaan | Rules dapat digunakan untuk menghasilkan fakta baru berdasarkan aturan dari data RDF |

## Jawab singkat

Ontology berada di atas RDF/RDFS karena RDF/RDFS menyediakan dasar untuk merepresentasikan data dan hubungan, sedangkan ontology seperti OWL memberikan makna domain yang lebih kompleks serta kemampuan penalaran. Ontology berada di bawah SPARQL karena SPARQL digunakan untuk mengambil atau menanyakan data yang telah direpresentasikan dalam graph RDF dan dapat menggunakan struktur serta kosakata yang didefinisikan oleh ontology.