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

