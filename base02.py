#numero = int(input("digite um número: "))
#i = 0
#while i < numero:
#  print(numero)
#  numero -= 1
#  i += 1

# 1. Adivinhação de números:
#  • Crie uma lista com 10 números.
#  • Peça ao usuário para adivinhar um número da lista.
#  • Use um loop while para continuar pedindo adivinhações até que o usuário acerte.

# lista = [9, 13, 18,20,15,6,17,7, 4, 11]
# while True:
#   numero = int(input("Adivinhe um número de 1 a 20: como"))
#   if numero in lista:
#     print("Parabéns! Adivinhou...")
#     break
#   print("Errou!")



# 2. Contagem regressiva:
#  • Crie uma lista de contagem regressiva de 10 a 1.
#  • Use um loop while para imprimir cada número da lista.

# lista = [10,9,8,7,6,5,4,3,2,1]
# i = 0
# while i < len(lista):
#   print(lista[i], end=" ")
#   i += 1

# 3. Adição de números:
#  • Crie uma lista vazia para armazenar números.
#  • Peça ao usuário para fornecer números e os adicionem à lista.
#  • Continue pedindo números até que o usuário decida parar.
# numeros = []
# while True:
#   numero = int(input("Digite um número inteiro ou 0 para parar: "))
#   if numero == 0: break
#   numeros.append(numero)
# print(numeros)


# 4. Média de notas:
#  • Crie uma lista vazia para armazenar notas.
#  • Peça ao usuário para fornecer notas e as adicionem à lista.
#  • Calcule e imprima a média das notas quando o usuário decidir parar.

# notas = list()
# while True:
#   nota = float(input("Digite a nota, 0 para sair: "))
#   if nota == 0: break
#   notas.append(nota)
# media = sum(notas) / len(notas)
# print(f"Média: {media:.1f}")

# 5. Busca em lista:
#  • Crie uma lista de cinco nomes.
#  • Peça ao usuário para digitar um nome.
#  • Usem um loop while para verificar se o nome está na lista e informar o resultado.

# nomes = ["Sofia", "Tamires", "Wendy", "Ines", "Sandra"]
# nome = input("Digite um nome para buscar na lista: ")
# i = 0
# achou = False
# while i < len(nomes):
#   if nome in nomes:
#     print(f"O nome {nome} está na lista de nomes.")
#     achou = True
#     break
#   i += 1
# if achou == False:
#   print(f"O nome {nome} não está na lista de nomes.")

# 6. Contador de números:
#  • Solicite ao usuário um número inicial.
#  • Use um loop while para imprimir os números de 1 até o número fornecido pelo usuário.
#  • Exiba uma mensagem indicando que o loop terminou.

# inicial = int(input("Digite um número inteiro: "))
# i = 1
# while i <= inicial:
#   print(i, end=" ")
#   i += 1
# print(f"\nA contagem terminou!")


# 7. Média de idades
#  • Crie um programa que peça ao usuário que insira idades de pessoas até que ele digite um valor negativo.
#  • Em seguida, utilize um loop while para calcular e exibir a média das idades inseridas.
# idades = []
# while True:
#   idade = int(input("Digite uma idade ou um número negativo para sair: "))
#   if idade < 0: break
#   idades.append(idade)

# i = 0
# media = 0
# while i < len(idades):
#   media += idades[i]
#   i += 1
# media = media / len(idades)
# print(f"A média das idades é {media:.0f}")

# 8. Números ímpares
#  • Com a lista numeros = [10, 15, 7, 23, 42, 5, 17, 8, 31, 12, 9, 25, 3, 19, 16, 28, 36, 14, 21, 6], exiba apenas os números ímpares da lista.

# numeros = [10, 15, 7, 23, 42, 5, 17, 8, 31, 12, 9, 25, 3, 19, 16, 28, 36, 14, 21, 6]

# i = 0
# while i < len(numeros):
#   if numeros[i] % 2 > 0:
#     print(numeros[i], end=" ")
#   i += 1

# 9. Números primos
#  • Crie um programa que solicite ao usuário que insira números inteiros positivos até que ele digite zero. 
#  • Use um loop while para determinar quantos números primos foram inseridos.
# primos = []
# while True:
#   numero = int(input("Digite  um inteiro ou 0 para sair: "))
#   if numero == 0: break
#   primos.append(numero)

# i = 0
# totalPrimos = 0
# while i < len(primos):
#   composto = False
#   j = 2
#   while j < primos[i]:
#     if primos[i] % j == 0:
#       composto = True
#     j += 1
#   if composto == False:
#     totalPrimos += 1
#   i += 1
# print(f"Foram inseridos {totalPrimos} número primos!")

# 10. Remoção de itens
#  • Com a lista nomes = ["Maria", "José", "Ana", "Pedro", "João", "Luiza", "Rafael", "João", "Carolina", "Fernando"], remova todos os nomes "João" da lista e exibam a lista resultante.

# nomes = ["Maria", "José", "Ana", "Pedro", "João", "Luiza", "Rafael", "João", "Carolina", "Fernando"]
# while "João" in nomes:
#   nomes.remove("João")
# print(nomes)

# 11. Calcular
#  • Crie um programa que solicite ao usuário que insira alturas (por exemplo, 1,80 m) de pessoas até que ele digite um valor negativo. 
#  • Calcule a média e identifiquem a maior e a menor altura.

# alturas = []
# while True:
#   altura = float(input("Digite uma altura ou um número negativo para sair: "))
#   if altura < 0: break
#   alturas.append(altura)
# media = sum(alturas) / len(alturas)
# print(f"A média das alturas é: {media:.2f}m")
# print(f"A maior altura é {max(alturas):.2f}m")
# print(f"A menor altura é {min(alturas):.2f}")


# 12. Fatorial
#  • Crie um programa que solicite ao usuário que insira um número inteiro positivo. 
#  • use um loop while para calcular e exibir o fatorial desse número.
numero = int(input("Digite um número inteiro positivo: "))

fatorial = 1
i = numero
while i > 1:
  fatorial *= i
  i -= 1
  print(fatorial, end=" ")
print(f"\nO fatorial de {numero} é {fatorial}")

