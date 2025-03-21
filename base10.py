#  Exercícios

lista = [8, 20, 50, 40, 1, 43, 32, 29, 47, 12, 9, 4]

#  1. Faça um programa que olhe todos os itens da lista acima e diga quantos deles são ímpares. 
impares = 0
for i in lista:
  if i % 2 != 0:
    impares += 1

print("A lista tem ", impares, " números ímpares")

# 2. Com a mesma lista, diga quais deles são pares.
pares = 0
for i in lista:
  if i % 2 == 0:
    pares += 1

print("A lista tem ", pares, " números pares")

#  3. Da lista acima, copie todos os elementos em outra lista com o nome nova_lista.
nova_lista = lista.copy()
print(nova_lista)

outra_lista = []
for i in lista:
  outra_lista.append(i)

print(outra_lista)

#  4. Da lista acima, crie uma nova lista copiando cada elemento em ordem crescente. Obs.: não usar sorted().
lista_crescente = []
while lista:
  menor = lista[0]
  for num in lista:
    if num < menor:
      menor = num
  lista_crescente.append(menor)
  lista.remove(menor)

print(lista_crescente)

#  5. Da lista acima, transforme todos os elementos em string.
lista = [8, 20, 50, 40, 1, 43, 32, 29, 47, 12, 9, 4]
i = 0
for item in lista:
  lista[i] = str(lista[i])
  i += 1

print(lista)

#  6. Faça um programa que, dadas duas listas de mesmo tamanho, crie uma nova lista com cada elemento igual à soma dos elementos da lista 1 com os da lista 2, na mesma posição
lista1 = [12, 8, 5, 7]
lista2 = [7, 4, 3, 9]
lista3 = []
i = 0
for elemento in lista1:
  soma = lista1[i] + lista2[i]
  lista3.append(soma)
  i += 1

print(lista3)

# 7. Faça um programa que, dadas duas listas de mesmo tamanho, imprima o produto escalar entre elas.
lista1 = [12, 8, 5, 7]
lista2 = [7, 4, 3, 9]
for i, n in enumerate(lista1):
  print(lista1[i] * lista2[i])

#  8. Faça um programa que peça para o usuário digitar 5 números e, ao final, imprima uma lista com os 5 números digitados pelo usuário (sem converter os números para int ou float).
lista = []
i = 0
while i < 5:
  numero = input("Digite um número: ")
  lista.append(numero)
  i += 1

print(lista)

#  9. Pegue a lista gerada no exercício anterior e transforme cada um dos itens dessa lista em um float.
for indice, valor in enumerate(lista):
  lista[indice] = float(lista[indice])

print(lista)

#  10. Usando listas, faça um programa que peça as 4 notas bimestrais e mostre a média

notas = []
media = 0
i = 0
while i < 4:
  nota = float(input(f"Digite a {i + 1}ª nota:"))
  notas.append(nota)
  media += nota
  i += 1

media /= 4
print(f"A média das notas é: {media}")
