# CRIANDO UMA TUPLA DINAMICAMENTE

from random import randint as r

tupla = (r(1,100), r(1,100), r(1, 100), r(1,100))
print(tupla)

inteiros = (int(input("Digite um inteiro: ")), int(input("Digite um inteiro: ")), int(input("Digite um inteiro: ")), int(input("Digite um inteiro: ")))
print(sorted(inteiros))
print(inteiros)

numeros = ()
while True:
  numero = input("Digite um inteiro ou 's' para sair: ")
  if numero == 's': break
  if numero.isnumeric():
    numero = int(numero)
    if numero not in numeros:
      numeros += (numero,)

print(numeros)
nova_tupla = tuple(sorted(numeros))
print(nova_tupla)
print(numeros)
