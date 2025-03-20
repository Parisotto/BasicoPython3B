# Exercícios BASE 08

#  1. Escreva uma função que retorne o maior de dois números.

# def maior(n1 :int, n2 :int):
#   if n1 > n2:
#     return n1
#   else:
#     return n2

# print("O número maior entre 7 e 9 é: ", maior(7, 9))
# print("O número maior entre 13 e 11 é: ", maior(13, 11))

#  2. Escreva uma função que receba dois números e retorne True, se o primeiro número for múltiplo do segundo.

# def multiplo(n1:int, n2:int):
#   return n1 % n2 == 0

# print("O número 9 é múltiplo de 3?: ", multiplo(9, 3))
# print("O número 9 é múltiplo de 2?: ", multiplo(9, 2))

#  3. Escreva uma função que receba o lado (l) de um quadrado e retorne sua área (A = lado²).

# def area(lado :float):
#   return lado * lado

# print("Área do quadrado de lado 5: ", area(5))
# print(f"Área do quadrado de lado 3,7: {area(3.7):.2f}")

#  4. Escreva uma função que receba a base e a altura de um triângulo e retorne sua área (A = (base x altura)/2).

# def areaTriangulo(base:float, altura:float):
#   area = base * altura / 2
#   return area

# print(f"A área do triângulo de base 3 e altura 5 é {areaTriangulo(3, 5):.2f}")

# print(f"A área do triângulo de base 4.2 e altura 5.5 é {areaTriangulo(4.2, 5.5):.2f}")

#  5. Faça uma função que recebe um nome e imprime “Olá, [nome]”.
# def ola(nome: str):
#   print("Olá,", nome)

# ola("Asdrúbal")

#  6. Faça uma função que recebe um nome e um horário e imprime “Bom dia, [nome]”, caso seja antes de 12h; “Boa Tarde, [nome]”, caso seja entre 12h e 18h; e “Boa noite, [nome]” caso seja após às 18h.

# def cumprimento(nome: str, horario: int):
#   if horario > 18:
#     print("Bom noite,", nome)
#   elif horario > 12:
#     print("Boa tarde,", nome)
#   else:
#     print("Bom dia,", nome)

# cumprimento("Tamires", 19)
# cumprimento("Tales", 14)
# cumprimento("Sofia", 9)

#  7. Faça uma função que recebe um número e retorna True, se ele for par, ou False, se ele for ímpar.

# def parOuImpar(numero: int):
#   return numero % 2 == 0

# if parOuImpar(2): print("2 é par!")

# if not parOuImpar(9): print("9 é impar!")

#  8. Escreva uma função para validar uma variável string. Essa função recebe como parâmetro a string, os números mínimo e máximo de caracteres. Retorne verdadeiro,se o tamanho da string estiver entre os valores de máximo e mínimo, e falso em caso contrário.

# def palavra(word: str, minimo: int, maximo: int):
#   return len(word) >= minimo and len(word) <= maximo

# word = input("Digite uma palavra qualquer: ")
# resposta = palavra(word, 5, 12)

# if resposta:
#   print(f"A palavra {word} foi aceita!")
# else:
#   print(f"A palavra {word} é menor que 5 ou maior que 12 letras!")

#  9. Escreva uma função que receba uma string e uma lista. A função deve comparar a string passada com os elementos da lista, também passada como parâmetro. Retorne verdadeiro, se a string for encontrada dentro da lista, e falso, em caso contrário.
nomes = ["Tamires", "Tales", "Sofia", "Geovana", "Ines"]
nome = input("Digite um nome: ")

def procurarNome(nome: str, nomes: list):
  return nome in nomes

if procurarNome(nome, nomes):
  print(f"O nome {nome} está na lista.")
else:
  print(f"O nome {nome} não foi encontrado na lista")
