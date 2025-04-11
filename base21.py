# Como acrescentar novos inteiros a uma lista já na posição da ordem crescente

lista = []
while True:
  valor = input("Digite um inteiro ou 's' para sair: ")
  if valor == 's': break
  if valor.isnumeric():
    valor = int(valor)
    if valor not in lista:
      if len(lista) == 0 or valor > lista[-1]:
        lista.append(valor)
      else:
        indice = 0
        while indice < len(lista):
          if valor < lista[indice]:
            lista.insert(indice, valor)
            break
          indice += 1

print("=" * 30)
print(lista)
lista.reverse()
print(lista)

