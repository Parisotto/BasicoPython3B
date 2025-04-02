# TUPLA X LISTA

lista = []
print(lista)
lista.append("Ana")
lista.append("Abgail")
print(lista)

tupla = ()
print(tupla)
tupla = ("Anna", "Abgail", "Ines")
tupla = list(tupla)
tupla.append("Geovane")
tupla = tuple(tupla)
print(tupla)

print(tupla.count("Abgail"))
print(tupla.index("Ines"))

print(lista[0])
print(tupla[0])
