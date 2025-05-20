# JOGO DA VELHA

import tkinter as tk
from tkinter import messagebox

#Variáveis globais
janela = None
jogador_atual = "X"
botoes = [["","",""], ["","",""], ["","",""]]
casas_ocupadas = 0

def interface():
  global janela
  for linha in range(3):
    for coluna in range(3):
      botao = tk.Button(janela, text="", font=("Arial", 24), width=5, height=2)
      botao.grid(row=linha, column=coluna)
      botoes[linha][coluna] = botao

  botoes[0][0]["command"] = lambda: clique(0, 0)
  botoes[0][1]["command"] = lambda: clique(0, 1)
  botoes[0][2]["command"] = lambda: clique(0, 2)
  botoes[1][0]["command"] = lambda: clique(1, 0)
  botoes[1][1]["command"] = lambda: clique(1, 1)
  botoes[1][2]["command"] = lambda: clique(1, 2)
  botoes[2][0]["command"] = lambda: clique(2, 0)
  botoes[2][1]["command"] = lambda: clique(2, 1)
  botoes[2][2]["command"] = lambda: clique(2, 2)

def clique(linha, coluna):
  global jogador_atual, casas_ocupadas
  if botoes[linha][coluna]['text'] == "":
    botoes[linha][coluna]['text'] = jogador_atual
    casas_ocupadas += 1
    if verificar_vencedor():
      messagebox.showinfo("Fim de Jogo", f"Jogador {jogador_atual} venceu!")
      reiniciar()
    elif casas_ocupadas == 9:
      messagebox.showinfo("Fim de Jogo", "Empate!")
      reiniciar()
    else:
      jogador_atual = "O" if jogador_atual == "X" else "X"

def verificar_vencedor():
  for linha in range(3):
    if all(botoes[linha][coluna]["text"] == jogador_atual for coluna in range(3)) or \
        all(botoes[j][linha]['text'] == jogador_atual for j in range(3)):
      return True
  
  if all(botoes[i][i]['text'] == jogador_atual for i in range(3)) or \
      all(botoes[i][2 - i]['text'] == jogador_atual for i in range(3)):
    return True
  
  return False

def reiniciar():
  global jogador_atual, casas_ocupadas
  for i in range(3):
    for j in range(3):
      botoes[i][j]['text'] = ""
    jogador_atual = "O" if jogador_atual == "X" else "X"
    casas_ocupadas = 0

def main():
  global janela
  janela = tk.Tk()
  janela.title("Jogo da Velha")
  interface()
  janela.mainloop()

main()
