from pathlib import Path
from rdflib import Graph

g = Graph()
g.parse(Path("../pertemuan-06/kampus_usu.ttl"), format="turtle")
print("Jumlah triple awal:", len(g))

IRI_DEFAULT = "https://raymondsmt2710-cell.github.io/web-semantik-kelompok02/WS_251402078/usu#"
EX_IRI = str(dict(g.namespaces()).get("ex", IRI_DEFAULT))
print("IRI dasar graf:", EX_IRI)

PREFIX = f"""
PREFIX ex:   <{EX_IRI}>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
"""

q_select = PREFIX + """
SELECT ?namaDosen ?namaMK WHERE {
  ?dosen ex:mengajar ?mk ;
         foaf:name   ?namaDosen .
  ?mk    foaf:name   ?namaMK .
}
ORDER BY ?namaDosen
"""
print("\n=== SELECT: dosen - mata kuliah ===")
hasil = list(g.query(q_select))
for row in hasil:
    print(row.namaDosen, "-", row.namaMK)
print("Jumlah baris SELECT:", len(hasil))

q_ask = PREFIX + "ASK { ex:ida ex:mengajar ex:tif3501 }"
print("\n=== ASK ===")
print("Sebelum INSERT:", g.query(q_ask).askAnswer)

g.update(PREFIX + """
INSERT DATA {
  ex:ida     ex:mengajar ex:tif3501 .
  ex:tif3501 foaf:name   "Rekayasa Ontologi"@id .
}
""")
print("Sesudah INSERT:", g.query(q_ask).askAnswer)
print("Jumlah triple akhir:", len(g))

g.serialize("kampus_usu_v2.ttl", format="turtle")
print("\nFile kampus_usu_v2.ttl berhasil dibuat.")
