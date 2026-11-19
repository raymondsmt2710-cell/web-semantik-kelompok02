
from pathlib import Path
from rdflib import Graph, RDF, RDFS
from owlrl import DeductiveClosure, RDFS_Semantics

BASE = "https://contoh.github.io/web-semantik/251402113/kampus#"
SUMBER = Path("../pertemuan-09/kampus_usu_v2.ttl")

# 1. Graf asserted: data asli + schema
asserted = Graph().parse(SUMBER, format="turtle")

asserted.update(f"""
PREFIX ex: <{BASE}>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

INSERT DATA {{
    ex:Lecturer rdfs:subClassOf ex:Pegawai .
    ex:Pegawai rdfs:subClassOf foaf:Person .

    ex:mengajar rdfs:domain ex:Lecturer ;
                 rdfs:range ex:MataKuliah .
}}
""")

print("Sumber:", SUMBER)
print("Asserted:", len(asserted))

# 2. Closure dihitung pada salinan graf
closure = Graph() + asserted
DeductiveClosure(RDFS_Semantics).expand(closure)

inferred = closure - asserted

# 3. Ambil hanya triple hasil inferensi yang bermakna
TRIVIAL = {RDFS.Resource, RDF.Property}

bermakna = Graph()

for s, p, o in inferred:
    if str(s).startswith(BASE) and o not in TRIVIAL and s != o:
        bermakna.add((s, p, o))

print("Closure:", len(closure))
print("Inferred:", len(inferred))
print("Bermakna:", len(bermakna))

# 4. Simpan graf asserted dan inferred
asserted.serialize("kampus_usu_v5.ttl", format="turtle")
bermakna.serialize("kampus_usu_inferred.ttl", format="turtle")

# 5. Bandingkan dengan graf Pertemuan 11
V4 = Path("../pertemuan-11/kampus_usu_v4.ttl")

if V4.exists():
    v4 = Graph().parse(V4, format="turtle")
    tercampur = [t for t in v4 if t not in asserted]

    print("Triple di v4 yang tidak ada di asserted:", len(tercampur))
