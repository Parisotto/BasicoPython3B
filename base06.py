#  1.Faça um programa que imprima cada elemento da lista [28, 9, 22, -31, -3, -31, 10, 32, 10, 2] usando o for.
# lista1 = [28, 9, 22, -31, -3, -31, 10, 32, 10, 2]
# for item in lista1:
#   print(item)
# print()
# print(lista1)

#  2. Faça um programa que imprima cada elemento da lista [3, 8, 30, 8, 19, -12, -2, -1, -7, -48] usando o for com range.
# lista2 = [3, 8, 30, 8, 19, -12, -2, -1, -7, -48]
# for indice in range(0, len(lista2)):
#   print(lista2[indice], end=" ")
# print()

#  3. Crie uma lista com 10 números inteiros e faça um programa que imprima cada elemento da lista usando o for.
# for item in list(range(1, 11)):
#   print(item, end=" ")
# print()

#  4. Crie uma lista com 10 números inteiros e faça um programa que imprima cada elemento da lista usando o for com range
# for item in list(range(1, 11)):
#   print(item, end=" ")
# print()

# 5. Faça um programa que imprima todos os itens da lista [28, 9, 22, -31, -3, -31, 10, 32, 10, 2] usando while e compare-o com o exercício 1.
# lista5 = [28, 9, 22, -31, -3, -31, 10, 32, 10, 2] 
# i = 0
# while i < len(lista5):
#   print(lista5[i], end=" ")
#   i += 1
# print()

#  6. Faça um programa que imprima todos os números de 5 a 0 usando o for.
# i = 5
# for n in range(0, 6):
#   print(i)
#   i  -= 1
# print()

#  7. Faça um programa que peça para o usuário digitar um número n e imprima uma lista com todos os números de 0 a n-1
# n = int(input("Digite um inteiro: "))
# i = 0
# while i < n:
#   print(i)
#   i += 1

# 8. Faça um programa que imprima o maior número da lista [-8, -6, 3, -1, 7], sem usar o método max(). 
# lista8 = [8, -6, 3, 9, -1, 7]
# maior = lista8[0]
# for item in lista8:
#   if item > maior:
#     maior = item
# print(maior)

# 10. Agora, usando o método max(), faça um programa que imprima os três maiores números da lista [2, 9, -5, 2, -8, 4, -9, -5, 4, 1].
lista10 = [2, 9, -5, 2, -8, 4, -9, -5, 4, 1]
i = 1
while i <= 3:
  print(max(lista10))
  lista10.remove(max(lista10))
  i += 1


