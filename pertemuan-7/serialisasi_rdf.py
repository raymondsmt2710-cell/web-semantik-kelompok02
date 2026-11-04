<<<<<<< HEAD
@prefix ex: <https://contoh.github.io/web-semantik/251402113/kampus#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
=======
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, DCTERMS, XSD
>>>>>>> e107de60a16b2170b8f7026d27003d9cdcb09919

<<<<<<< HEAD
ex:alvin a ex:Student ;
    foaf:name "Alvin Benyamin Sigalingging"@id ;
    ex:berasalDari ex:teknologi_informasi ;
    ex:mengambil ex:web_semantik .

ex:ida a ex:Lecturer ;
    foaf:name "Muhammad Isa Dadi Hasibuan S.Kom., M.Kom"@id ;
    ex:mengajar ex:web_semantik .

ex:teknologi_informasi a ex:Department .

ex:web_semantik a ex:Course ;
    foaf:name "Web Semantik"@id .


=======
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
>>>>>>> e107de60a16b2170b8f7026d27003d9cdcb09919