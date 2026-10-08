from rdflib import Dataset

g = Dataset()

g.parse("kampus_tergabung.trig", format="trig")

print("Jumlah triple:", len(g))

print(g.serialize(format="trig"))