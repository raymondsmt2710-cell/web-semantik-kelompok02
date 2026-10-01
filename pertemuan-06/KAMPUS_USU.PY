from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, FOAF, XSD

g = Graph()

EX = Namespace("https://contoh.github.io/web-semantik/251402113/kampus#")

g.bind("ex", EX)
g.bind("foaf", FOAF)

# Dosen dan mata kuliah
g.add((EX.ida, RDF.type, EX.Lecturer))
g.add((EX.ida, FOAF.name, Literal("Muhammad Isa Dadi Hasibuan S.Kom., M.Kom", lang="id")))
g.add((EX.web_semantik, RDF.type, EX.Course))
g.add((EX.web_semantik, FOAF.name, Literal("Web Semantik", lang="id")))
g.add((EX.ida, EX.mengajar, EX.web_semantik))

g.add((EX.alvin, RDF.type, EX.Student))
g.add((EX.alvin, FOAF.name, Literal("Alvin Benyamin Sigalingging", lang="id")))
g.add((EX.alvin, EX.mengambil, EX.web_semantik))

g.add((EX.teknologi_informasi, RDF.type, EX.Department))
g.add((EX.alvin, EX.berasalDari, EX.teknologi_informasi))

print(g.serialize(format="turtle"))

g.serialize("kampus_usu.ttl", format="turtle")
g.serialize("kampus_usu.jsonld", format="json-ld", indent=2)