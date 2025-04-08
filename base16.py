# CONJUNTO (set) X LISTA

lista = [] # ou list()
tupla = () # ou tuple()
conjunto = set()

print(lista)
print(tupla)
print(conjunto)

lista.append("item lista")
tupla = ("item tupla")

conjunto = {"Ana", "Abgail", "Ines"}
print(conjunto)
# print(conjunto[0])

conjunto.add("Geovane")
print(conjunto)

lista = ["SP", "RJ", "MG"]

i = 0
while i < len(lista):
  print(lista[i])
  i += 1

for item in lista:
  print(item)

print()
for item in conjunto:
  print(item)

print()
for indice, item in enumerate(conjunto):
  print(indice, item)

conjuntoA = {"Abgail", "Ines", "Geovanna"}
conjuntoB = {"Geovane", "Patricio", "Ines"}

diferenca = conjuntoA.difference(conjuntoB)
print(diferenca)

print(conjuntoA.intersection(conjuntoB))

print(conjuntoA.union(conjuntoB))

