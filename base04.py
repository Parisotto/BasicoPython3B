# Escreva um programa que use um loop while para preencher uma lista com os N números pares aleatórios, em que N é um número inserido pelo usuário. Em seguida exiba a lista resultante.

import random

def numeros_pares():
  pares = []
  quantidade = int(input("Digite quantos número pares deve ter sua lista: "))
  contador = 1
  while contador <= quantidade:
    try:
      aleatorio = random.randint(1, 1000)
      if aleatorio % 2 == 0:
        pares.append(aleatorio)
      contador += 1
    except ValueError:
      print("ERRO! Digite apenas um número inteiro!")
      
  print(pares)

numeros_pares()