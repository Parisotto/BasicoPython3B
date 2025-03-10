# 1.Adicione o número 50 ao final da lista.
lista_numeros = [10, 20, 30, 40]
lista_numeros.append(50)
print(lista_numeros)

# 2. Adicione “laranja” ao índice 1 da lista.
lista_frutas = ["maçã", "banana", "uva"]
lista_frutas.insert(1,"laranja")
print(lista_frutas)

# 3. Remova “cachorro” da lista.
lista_animais = ["cachorro", "gato", "pássaro", "cachorro"]
while "cachorro" in lista_animais:
  lista_animais.remove("cachorro")
print(lista_animais)

# 4. Remova o elemento de índice 2 da lista e mostre o elemento removido.
lista_nomes = ['Alice', 'Bob', 'Charlie', 'David']
print(lista_nomes.pop(2))
print(lista_nomes)

# 5. Encontre o índice da primeira ocorrência de ‘azul’ na lista.
lista_cores = ['vermelho', 'azul', 'verde', 'amarelo', 'azul']
print(lista_cores.index('azul'))

# 6. Conte quantas vezes o número 2 aparece na lista.
lista_numeros_repetidos = [1, 2, 3, 2, 4, 2, 5, 2]
quantidade = lista_numeros_repetidos.count(2)
print("O número 2 aparece ", quantidade, " vezes na lista.")

# 7. Ordene a lista em ordem crescente.
lista_desordenada = [50, 20, 80, 10, 40]
lista_desordenada.sort()
print(lista_desordenada)

# 8. Inverta a ordem dos elementos da lista.
lista_invertida = ['maçã', 'banana', 'laranja', 'uva']
lista_invertida.reverse()
print("Lista invertida: ", lista_invertida)

# 9. Crie uma cópia profunda da lista.
original = [1, 2, 3, 4, 5]
copia_profunda = original[:]
print(copia_profunda)
print(original)


# 10. Dada a lista:
lista_numerica = [15, 8, 22, 3, 10]

# a) Mostre o tamanho da lista.
tamanho = len(lista_numerica)
print("Tamanho da lista: ", tamanho)

# b) Mostre o maior valor da lista.
print("Maior valor da lista: ", max(lista_numerica))

# c) Mostre o menor valor da lista.
print("Menor valor da lista: ", min(lista_numerica))

# d) Mostre a soma de todos os elementos da lista
print("Soma de todos os valores da lista: ", sum(lista_numerica))
