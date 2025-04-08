# DICIONÁRIO x CONJUNTO x LISTA

dicionario = {}
print(dicionario)

dicionario[55] = "Brasil"
dicionario[1] = "USA"
print(dicionario)

dicionario = {"SP":"São Paulo", "RJ":"Rio", "MG":"Minas"}
print(dicionario)

print(dicionario['SP'])

print(dicionario.get("ES"))
print(dicionario.get("ES", "Não encontrei."))

dicionario['ES'] = "Espírito Santo"

print(dicionario)

print(dicionario.pop("MG"))
print(dicionario)

del dicionario["ES"]
print(dicionario)

for chave in dicionario:
  print(chave)

for chave in dicionario.keys():
  print(chave)

for valor in dicionario.values():
  print(valor)

dicionario["RJ"] = "Rio de Janeiro"
dicionario["MG"] = "Minas Gerais"

for chave, valor in dicionario.items():
  print(chave, valor)

print()
for item in dicionario.items():
  print(item)

for indice, (chave, valor) in enumerate(dicionario.items(), start=1):
  print(indice, chave, valor)

