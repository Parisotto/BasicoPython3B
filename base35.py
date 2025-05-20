# Classes e objetos - POO Programação Orientada a Objetos

class Livro():
  def __init__(self, titulo, autor):
    self.titulo = titulo
    self.autor = autor

  def info(self):
    print(f"Títuo: {self.titulo}, autor: {self.autor}")

livro1 = Livro("Fundação", "Isaac Asimov")

print(livro1.titulo)
print(livro1.autor)

livro1.info()
print()
livro2 = Livro("Os Miseráveis", "Vitor Hugo")
print(livro2.titulo)
print(livro2.autor)

livro2.info()
