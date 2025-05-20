class ContaBancaria():
  def __init__(self, saldo):
    self.saldo = saldo
    print(f"Conta aberta. Saldo R${self.saldo},00")

  def deposito(self, valor):
    self.saldo += valor
    print(f"Depósito de R${valor},00 efetuado. Saldo: R${self.saldo},00")

  def saque(self, valor):
    if(self.saldo< valor):
      print(f"Saldo insuficiente para o valor sacado")
    else:
      self.saldo -= valor
      print(f"Saque de R${valor},00 efetuado. Saldo: R${self.saldo},00")

  def versaldo(self):
    print(f"Seu saldo e de R${self.saldo},00")

conta1 = ContaBancaria(int(input("Digite o valor do depósito inicial: R$")))
conta1.deposito(int(input("Digite o valor do depósito: R$")))
conta1.saque(int(input("Digite o valor do saque: R$")))
conta1.versaldo()
