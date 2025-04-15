# Faça uma matriz 3x3 e preencha com valores de 1 a 9
matriz = [[1,2,3],[4,5,6],[7,8,9]]

print(matriz)
for linha in matriz:
  print(linha)

for linha in range(3):
  for coluna in range(3):
    print(matriz[linha][coluna])

for linha in matriz:
  for coluna in linha:
    print(coluna)
