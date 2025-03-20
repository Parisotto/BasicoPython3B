# enumarte e range

lista = list(range(1,11,2))
print(lista)

for valor in lista:
  print(valor)

nomes = ["Ana", "Paula", "Ines"]
for nome in nomes:
  print(nome)

for nome in enumerate(nomes):
  print(nome)

for indice, nome in enumerate(nomes, start=1):
  print(f"Índice: {indice} - Nome: {nome}")

dicionario = {"SP":"São Paulo", "RJ":"Rio de Janeiro", "MG":"Minas Gerais"}
for n in enumerate(dicionario.keys()):
  print(n)

for n, k in enumerate(dicionario.keys(), start=1):
  print(n, k)

for n, v in enumerate(dicionario.values(), start=1):
  print(n, v)

for n, i in enumerate(dicionario.items(), start=1):
  print(n, i)

for n, (k, v) in enumerate(dicionario.items(), start=1):
  print(n, k, v)

