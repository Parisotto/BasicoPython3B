# Exercícios

#  1. Crie duas variáveis do tipo string, uma contendo “Olá” e outra contendo “Mundo”. Concatene-as e imprima o resultado.
# string1 = "Olá"
# string2 = "Mundo"
# print(string1 + " " + string2 + "!")

#  2. Dada a string “Python”, imprima o caractere que está no índice 2.
# string = "Python"
# print(string[2])

#  3. Crie uma string qualquer. Substitua um dos caracteres por outro e imprima a nova string resultante.
# string = "Gato"
# string = string.replace("G", "F")
# print(string)

#  4. Solicite ao usuário que digite seu nome. Em seguida, imprima o comprimento do nome fornecido.
# nome = input("Digite seu nome: ")
# print(len(nome))

#  5. Crie uma string que represente uma frase. Verifique se a palavra “gato” está presente na frase e imprima o resultado (verdadeiro ou falso)
# frase = "O sorriso do gato de Alice."
# if "gato" in frase:
#   print("Verdadeiro")
# else:
#   print("Falso")

#  6. Peça ao usuário que digite uma frase. Conte o número de palavras na frase e imprima o resultado.
# frase = input('Digite uma frase: ')
# palavras = frase.split()
# print(palavras)
# print(len(palavras))

#  7. Crie uma função que receba uma frase como parâmetro e retorne a mesma frase com as palavras invertidas. Por exemplo, “Olá Mundo” deve ser transformado em “Mundo Olá”.
# frase = "Olá mundo de estudantes!"
# def inverter(frase):
#   return ' '.join(reversed(frase.split()))

# invertida = inverter(frase)
# print(invertida)

#  8. Solicite ao usuário que digite uma string que contenha espaços em branco no início e no final. Remova esses espaços e imprima a string resultante.
# string_com_espacos = input("Digite uma frase com espaços antes e depois: ")
# print(string_com_espacos + "!")
# string_sem_espacos = string_com_espacos.strip()
# print(string_sem_espacos + "!")

#  9. Crie uma função que receba um número inteiro e retorne uma string que o represente com separadores de milhares. Por exemplo, para o número 1234567, a função deve retornar “1,234,567”.
# def formatar(numero):
#   return f"{numero:,}"

# print(formatar(1234567))

#  10. Implemente uma função que receba uma string e um número (chamado de “deslocamento”) como parâmetros e retorne a string cifrada, usando a Cifra de César. Cada letra na string deve ser deslocada pelo número fornecido. Por exemplo, com um deslocamento de 3, “ABC” seria cifrado como “DEF”
def cifra_cesar(string, deslocamento):
  resultado = ""
  for letra in string:
    if letra.isalpha():
      base = 65 if letra.isupper() else 97
      resultado += letra((ord(letra) - deslocamento + base) % 26 + base)
    else:
      resultado += letra
  return resultado

texto = "ABC"
deslocamento = 3
print(cifra_cesar(texto, deslocamento))


# 11. Escreva um programa que receba uma palavra ou frase do usuário e determine se ela é um palíndromo ou não. O programa deve ignorar maiúsculas e minúsculas, bem como espaços em branco
