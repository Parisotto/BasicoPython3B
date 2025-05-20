class Pessoa():
  def __init__(self, nome, idade, genero):
    self.nome = nome
    self.idade = idade
    self.genero = genero

  def saudacao(self):
    print(f"Meu nome é {self.nome} e tenho {self.idade} anos.")

class Professor(Pessoa):
  def __init__(self, nome, idade, genero, titulo):
    super().__init__(nome, idade, genero)
    self.titulo = titulo

  def info(self):
    print(f"O título é {self.titulo}")


pessoa1 = Pessoa("Edson", "62", "M")
pessoa2 = Pessoa("Sandra", "58", "F")

pessoa1.saudacao()
pessoa2.saudacao()

print(pessoa1.nome)

print()
prof1 = Professor("Parisotto", "63", "Maculino", "Mestre")
print(prof1.nome)
prof1.info()
prof1.saudacao()
