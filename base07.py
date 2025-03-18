# FUNCÕES def

def minhaFuncao():
  lista = list(range(1, 11))
  print(len(lista))

minhaFuncao()

def outraFuncao(parametro):
  print(parametro)

outraFuncao(9)
outraFuncao("Texto")
lista = list(range(1, 11))
outraFuncao(lista)

def novaFuncao(p1, p2):
  print(p1 + p2)

novaFuncao(9, 7)

def outraFuncao(p1, p2):
  print(p1 * p2)

def outraFuncao():
  print("Olá, mundo!")

def somaLista(lista):
  return sum(lista)

print(somaLista(lista))

def somaInteiros(n1 :int, n2: int):
  if not isinstance(n1, int) or not isinstance(n2, int):
    return "Erro!"
  else:
    return n1 + n2

print(somaInteiros("d", 3))
