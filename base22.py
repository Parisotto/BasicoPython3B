from random import randint as r

valores = [[], []]

quantos_numeros = int(input("Digite quantos números serão gerados: "))

i = 1
while i <= quantos_numeros:
  valor = r(1, 100)
  if valor % 2 == 0:
    indice = 0
  else:
    indice = 1
  if valor not in valores[indice]:
    valores[indice].append(valor)
    i += 1

print("Pares: ", sorted(valores[0]))
print("Ímpares: ", sorted(valores[1]))

valores[0].sort()
for par in valores[0]:
  print(par, end=', ')
  