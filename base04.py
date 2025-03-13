# Escreva um programa que use um loop while para preencher uma lista com os N números pares aleatórios, em que N é um número inserido pelo usuário. Em seguida exiba a lista resultante.

import random

def numeros_pares():
  pares = []
  try: 
    quantidade = int(input("Digite quantos número pares deve ter sua lista: "))
  except ValueError:
    print("ERRO! Digite apenas um número inteiro!")
    exit()
  contador = 1
  while contador <= quantidade:
      aleatorio = random.randint(1, 1000)
      if aleatorio % 2 == 0:
        pares.append(aleatorio)
      contador += 1

  print(pares)

numeros_pares()