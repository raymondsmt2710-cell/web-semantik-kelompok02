from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, DCTERMS, XSD

g = Graph()
g.parse("kampus_usu.ttl", format="turtle")
print(f"Jumlah triple awal: {len(g)}")

EX = Namespace("https://contoh.github.io/web-semantik/251402113/kampus#")
stmt = URIRef(EX + "stmt-01")

g.add((stmt, RDF.type, RDF.Statement))
g.add((stmt, RDF.subject, EX.ida))
g.add((stmt, RDF.predicate, EX.mengajar))
g.add((stmt, RDF.object, EX.web_semantik))
g.add((stmt, DCTERMS.creator, EX.ida))
g.add((stmt, DCTERMS.date, Literal("2026-10-01", datatype=XSD.date)))
g.add((stmt, DCTERMS.source, Literal("Data akademik kampus")))

g.serialize("kampus_usu.jsonld", format="json-ld", indent=2)
g.serialize("kampus_usu.nt", format="nt")

print(f"Jumlah triple: {len(g)}")
print(g.serialize(format="turtle"))