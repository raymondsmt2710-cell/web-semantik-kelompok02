from rdflib import Graph

ATURAN = """PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
CONSTRUCT { ?x a ?super }
WHERE { ?x a/rdfs:subClassOf* ?super }"""

Q_ORANG = """PREFIX foaf: <http://xmlns.com/foaf/0.1/>
SELECT ?x WHERE { ?x a foaf:Person }"""

def materialisasi(g):
    """Menambahkan triple yang belum ada."""
    baru = Graph()

    for t in g.query(ATURAN):
        if t not in g:
            baru.add(t)

    for t in baru:
        g.add(t)

    return baru


g = Graph().parse("kampus.ttl")

turunan = materialisasi(g)
print("Putaran 1:", len(turunan), "triple baru | Person:", len(list(g.query(Q_ORANG))))

RINA = "@prefix ex: <http://contoh.id/kampus/> . ex:rina a ex:DosenTetap ."
g.parse(data=RINA, format="turtle")

print("Rina masuk | Person:", len(list(g.query(Q_ORANG))))

turunan += materialisasi(g)
print("Putaran 2 | Person:", len(list(g.query(Q_ORANG))))

turunan.serialize("kampus_turunan.ttl", format="turtle")
g.serialize("kampus_v4.ttl", format="turtle")

print("Triple turunan disimpan terpisah:", len(turunan))