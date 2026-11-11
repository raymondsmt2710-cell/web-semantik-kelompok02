
from pathlib import Path
from rdflib import Graph

# Mengambil lokasi folder tempat file Python berada
BASE_DIR = Path(__file__).resolve().parent

# Menggunakan v3 terlebih dahulu, lalu v2 jika v3 tidak tersedia
SUMBER = BASE_DIR.parent / "pertemuan-10" / "kampus_usu_v3.ttl"

if not SUMBER.exists():
    SUMBER = BASE_DIR.parent / "pertemuan-09" / "kampus_usu_v2.ttl"

if not SUMBER.exists():
    raise FileNotFoundError("File kampus_usu_v3.ttl maupun kampus_usu_v2.ttl tidak ditemukan.")

g = Graph().parse(SUMBER, format="turtle")

print("Sumber:", SUMBER)
print("Triple awal:", len(g))

PREFIX = """
PREFIX ex: <https://contoh.github.io/web-semantik/251402113/kampus#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX schema: <https://schema.org/>
"""

# A. Pemetaan ke schema.org
q_peta = PREFIX + """
CONSTRUCT {
    ?d a schema:Person ;
       schema:name ?nama .
}
WHERE {
    ?d a ex:Lecturer ;
       foaf:name ?nama .
}
"""

peta = Graph()

for triple in g.query(q_peta):
    peta.add(triple)

print("Triple hasil pemetaan:", len(peta))

peta.serialize(
    destination=BASE_DIR / "dosen_schema.ttl",
    format="turtle"
)

# B. Menambahkan hierarki kelas
g.update(PREFIX + """
INSERT DATA {
    ex:Lecturer rdfs:subClassOf ex:Pegawai .
    ex:Pegawai rdfs:subClassOf foaf:Person .
}
""")

q_orang = PREFIX + """
SELECT ?x
WHERE {
    ?x a foaf:Person .
}
"""

sebelum = list(g.query(q_orang))
print("foaf:Person sebelum:", len(sebelum))

# C. Materialisasi
q_turunan = PREFIX + """
CONSTRUCT {
    ?x a ?super .
}
WHERE {
    ?x a/rdfs:subClassOf+ ?super .
}
"""

turunan = g.query(q_turunan)

baru = [triple for triple in turunan if triple not in g]

for triple in baru:
    g.add(triple)

print("Triple turunan baru:", len(baru))

sesudah = list(g.query(q_orang))
print("foaf:Person sesudah:", len(sesudah))

# D. Menyimpan graf hasil materialisasi
g.serialize(
    destination=BASE_DIR / "kampus_usu_v4.ttl",
    format="turtle"
)

print("File hasil berhasil dibuat.")
