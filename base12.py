# MEGASENA

# Faça uma função que retorne números aleatórios para a Megasena.
# O usuário deverá escolher quantos números irá apostar, sendo no mínimo 6 e no máximo 20 números de 1 a 60.
# Lembre-se de que a lista final de escolhas não pode conter um valor repetido. 
# Permita que o usuário continue fazendo outros jogos da Megasena até que ele digite 0 (zero) para parar. 
# Ao final, mostre quanto o usário deverá pagar conforme o número de jogos e de palpites por jogo, de acordo com os valores abaixo:

# Números Escolhidos	Valor da Aposta
# 6	                  R$ 5,00
# 7	                  R$ 35,00
# 8	                  R$ 140,00
# 9	                  R$ 420,00
# 10	                R$ 1.050,00
# 11	                R$ 2.310,00
# 12	                R$ 4.620,00
# 13	                R$ 8.580,00
# 14	                R$ 15.015,00
# 15	                R$ 25.025,00
# 16	                R$ 40.040,00
# 17	                R$ 61.880,00
# 18	                R$ 92.820,00
# 19	                R$ 135.660,00
# 20	                R$ 193.800,00

import random

def gerar_numeros(quantidade):
  numeros = []
  i = 1
  while i <= quantidade:
    numero = random.randint(1, 60)
    if numero not in numeros:
      numeros.append(numero)
      i += 1

  return sorted(numeros)

def valor_aposta(quantidade):
  valores = {
     6: 5.00,
     7: 35.00,
     8: 140.00,
     9: 420.00,
    10: 1050.00,
    11: 2310.00,
    12: 4620.00,
    13: 8580.00,
    14: 15015.00,
    15: 25025.00,
    16: 4004.00,
    17: 61880.00,
    18: 92820.00,
    19: 135660.00,
    20: 193800.00
  }
  return valores.get(quantidade, 0)

def main():
  total_pagar = 0
  total_jogos = 0
  
  print()
  print("=" * 70)
  print(" " * 31 + "MEGASENA")
  print("=" * 70)
  print()
      
  while True:
    try:
      quantidade = int(input("Quantos números deseja apostar? (6 a 20, ou 0 para sair): "))
      if quantidade == 0:
        break
      if quantidade >= 6 and quantidade <= 20:
        jogo = gerar_numeros(quantidade)
        valor = valor_aposta(quantidade)
        total_pagar += valor
        total_jogos += 1
        print(f"Seus núero: {jogo}")
        print(f"Valor da aposta: R$ {valor:.2f}\n")
      else:
        print("Por favor, escolha um número entre 6 e 20.")

    except ValueError:
      print("Entrada inválida! Digite um número inteiro.")
  
  print()
  print("=" * 70)
  print(" " * 31 + "MEGASENA")
  print("=" * 70)
  print()

  print(f"Total de jogos realizados: {total_jogos}")
  print(f"Total a pagarf: R$ {total_pagar:.2f}")
  print()
  
main()