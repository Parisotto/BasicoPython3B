# Crie um programa em o o computador selecione um número aleatório entre 1 e 100 e solicite ao usuário que adivinhe o número. O programa deve fornecer dicas se o palpite do usuário estiver muito alto ou muito baixo. O usuário deve continuar tentando adivinhar até acertar.

import random

def adivinhar():
  numero_secreto = random.randint(1, 100)
  tentativas = 0

  print("Tente adivinhar o número entre 1 e 100!")

  while True:
    try:
      palpite = int(input(" Digite seu palpite: "))
      tentativas += 1
      if palpite < numero_secreto:
        print("Você tentou um número abaixo do secreto!")
      elif palpite > numero_secreto:
        print("Você tentou um número acima do secreto!")
      else:
        print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas!")
        break
    except ValueError:
      print("Estrada inválida. Digite um número inteiro")


adivinhar()