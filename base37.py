class Publicacao():
  def __init__(self, titulo, editora, ano):
    self.titulo = titulo
    self.editora = editora
    self.ano = ano

  def info(self):
    print(f"Título: {self.titulo}, Editora: {self.editora}")

class Livro(Publicacao):
  def __init__(self, titulo, autor, editora, ano):
    super().__init__(titulo, editora, ano)
    self.autor = autor

  def info_livro(self):
    print(f"O autor é: {self.autor}")

edicao = Livro("A Divina Comédia", "Dante", "Cia das Letras", "2020")
edicao.info()
edicao.info_livro()

print(f"Título: {edicao.titulo}, Autor: {edicao.autor}")
