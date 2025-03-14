# O laço de repetição "for" (loop for)

sequencia = ["Ana", "Abgail", "Ines", "Isa"]

for elemento in sequencia:
  print(elemento)

numeros = [2 , 7, 1, 9, 15]
numeros.sort()
for numero in numeros:
  print(numero, end=" ")
print()

tupla = ("Palmeiras", "Corinthians", "São Paulo", "Santos")
for time in tupla:
  print(time, end=", ")

print()
dicionario = {'SP':"São Paulo", "RJ":"Rio", "MG":"Minas"}
for estado in dicionario:
  print(estado)

print()
# FUNÇÃO RANGE
# range(inicio, fim, passo)
pontos = range(3, 9, 2)
for ponto in pontos:
  print(ponto)

print()
for valor in range(20):
  print(valor)

lista_numerica = list(range(1, 51))
for n in lista_numerica:
  print(n)

print(lista_numerica)

# FUNÇÃO ENUMERATE()
print()
paises = ["Brasil", "Itália", "Espanha", "França", "Alemanha"]
for indice, valor in enumerate(paises):
  print(f"Índice: {indice} - Valor: {valor}")

for i, v in enumerate(dicionario):
  print(f"{i} - {v}")

