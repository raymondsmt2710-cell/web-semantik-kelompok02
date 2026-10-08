from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, FOAF, XSD

g = Graph()

EX = Namespace("https://contoh.github.io/web-semantik/251402113/kampus#")

g.bind("ex", EX)
g.bind("foaf", FOAF)

g.add((EX.ida, RDF.type, EX.Lecturer))
g.add(
    (EX.ida, FOAF.name, Literal("Muhammad Isa Dadi Hasibuan S.Kom., M.Kom", lang="id"))
)
g.add((EX.web_semantik, RDF.type, EX.Course))
g.add((EX.web_semantik, FOAF.name, Literal("Web Semantik", lang="id")))
g.add((EX.ida, EX.mengajar, EX.web_semantik))

g.add((EX.alvin, RDF.type, EX.Student))
g.add((EX.alvin, FOAF.name, Literal("Alvin Benyamin Sigalingging", lang="id")))
g.add((EX.alvin, EX.mengambil, EX.web_semantik))

g.add((EX.teknologi_informasi, RDF.type, EX.Department))
g.add((EX.alvin, EX.berasalDari, EX.teknologi_informasi))

g.add((EX.raymond, RDF.type, EX.Lecturer))
g.add((EX.raymond, FOAF.name, Literal("Raymond Ganda", lang="id")))
g.add((EX.ryan_dani, RDF.type, EX.Lecturer))
g.add((EX.ryan_dani, FOAF.name, Literal("Ryan Dani", lang="id")))

g.add((EX.basis_data, RDF.type, EX.Course))
g.add((EX.basis_data, FOAF.name, Literal("Basis Data", lang="id")))
g.add((EX.kecerdasan_buatan, RDF.type, EX.Course))
g.add((EX.kecerdasan_buatan, FOAF.name, Literal("Kecerdasan Buatan", lang="id")))

g.add((EX.raymond, EX.mengajar, EX.basis_data))
g.add((EX.ryan_dani, EX.mengajar, EX.kecerdasan_buatan))

g.add((EX.web_semantik, EX.jumlahKredit, Literal(3, datatype=XSD.integer)))
g.add((EX.basis_data, EX.jumlahKredit, Literal(3, datatype=XSD.integer)))
g.add((EX.kecerdasan_buatan, EX.jumlahKredit, Literal(2, datatype=XSD.integer)))

g.add((EX.ryan_fedryck, RDF.type, EX.Student))
g.add((EX.ryan_fedryck, FOAF.name, Literal("Ryan Fedryck", lang="id")))
g.add((EX.ryan_fedryck, EX.mengambil, EX.basis_data))
g.add((EX.alvin, EX.mengambil, EX.kecerdasan_buatan))

print(g.serialize(format="turtle"))

g.serialize("kampus_usu.ttl", format="turtle")
g.serialize("kampus_usu.jsonld", format="json-ld", indent=2)

print("Daftar dosen:")
for subject, predicate, obj in g.triples((None, RDF.type, EX.Lecturer)):
    print(subject)
