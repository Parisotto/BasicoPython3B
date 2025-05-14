# Árvore de Decisão

pergutas = [
  "Com base na oferta de alguns produtos em oferta, eu deveria comprar mais?",
  "Tenho dinheiro para algo além do vestido?", # 1
  "Eu gosto do produto recomendado?", # 2
  "O produto recomendado combina com a minha roupa?" # 3
]

resultado = ("Declinar", "Aceitar")

def arvore_de_decisao(pergunta):
  return input(pergunta + " (sim|não): ").lower().strip()

def decisao(d):
  print(f"\n{d} oferta!\n")

def main():
  print(f"\n{pergutas[0]}\n")

  while True:
    resposta = arvore_de_decisao(pergutas[1])
    if resposta == 'sim':
      resposta = arvore_de_decisao(pergutas[2])
      if resposta == 'sim':
        resposta = arvore_de_decisao(pergutas[3])
        if resposta == 'sim':
          sinalizador = 1
          break
        elif resposta == 'não':
          sinalizador = 0
          break
      if resposta == 'não':
        sinalizador = 0
        break
    elif resposta == 'não':
      sinalizador = 0
      break
    
    print("\nResponda somente com 'sim' ou 'não'\n")

  decisao(resultado[sinalizador])

main()