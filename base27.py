arquivo = open("cores.txt", "w")
arquivo.write('Com estão?')
arquivo.close()

with open("cores.txt", "w") as cores:
  cores.write("azul")

lista_cores = ["azul", "verde", "amarelo", "vermelho"]

with open("cores.txt", "w") as cores:
  for c in lista_cores:
    cores.write(c + "\n")

with open("cores.txt", 'r') as cores:
  print(cores.read())

with open("cores.txt", "a") as cores:
  cores.write("branco\n")

with open("cores.txt", "a") as cores:
  lista_novas_cores = ["rosa", "preto", "lilás", "azul"]
  for cor in lista_novas_cores:
    cores.write(cor + "\n")

