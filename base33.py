# Jogo Pedra, Papel Tesoura (Jokenpô)

import customtkinter as tk # pip install customtkinter
import random
from PIL import Image # pip install pillow

total_pontos_voce = 0
total_pontos_empate = 0
total_pontos_app = 0

def pedra():
  jokenpo('Pedra')

def papel():
  jokenpo('Papel')

def tesoura():
  jokenpo('Tesoura')

def jokenpo(escolha_usuario):
  global total_pontos_app, total_pontos_empate, total_pontos_voce

  escolha_app = random.choice(['Pedra', 'Papel', 'Tesoura'])
  if escolha_usuario == escolha_app:
    ganhador = 'EMPATE!'
    cor = 'blue'
    total_pontos_empate += 1
    pontos_empate.configure(text=f"Você: {total_pontos_empate}")
  elif (
    (escolha_usuario == 'Pedra' and escolha_app =='Tesoura') or
    (escolha_usuario == 'Papel' and escolha_app == 'Pedra') or
    (escolha_usuario == 'Tesoura' and escolha_app == 'Papel')
  ):
    ganhador = 'VOCÊ venceu!'
    cor = 'green'
    total_pontos_voce += 1
    pontos_voce.configure(text=f"Você: {total_pontos_voce}")
  else:
    ganhador = 'App venceu!'
    cor = 'red'
    total_pontos_app += 1
    pontos_app.configure(text=f"Você: {total_pontos_app}")
  
  mensagem = f"Você: {escolha_usuario.upper()}\nApp: {escolha_app.upper()}\n\n{ganhador}"
  resultado.configure(text=mensagem, text_color=cor)

def interface():
  global resultado, pontos_voce, pontos_empate, pontos_app

  icon_pedra = tk.CTkImage(light_image=Image.open("icons/pedra.png"), size=(20, 20))
  icon_papel = tk.CTkImage(light_image=Image.open("icons/papel.png"), size=(20, 20))
  icon_tesoura = tk.CTkImage(light_image=Image.open("icons/tesoura.png"), size=(20, 20))

  quadro = tk.CTkFrame(janela, border_color="black", border_width=0.5)
  quadro.pack(padx=20, pady=20, fill="both", expand=True)

  tk.CTkLabel(quadro, text="Pedra, Papel ou Tesoura?", font=("Verdana", 18)).pack(pady=20)

  frame_botoes = tk.CTkFrame(quadro)
  frame_botoes.pack(pady=20, padx=20)

  bt_pedra = tk.CTkButton(frame_botoes, image=icon_pedra, text="Pedra", command=pedra)
  bt_pedra.grid(row=1, column=1, padx=(20, 0), pady=(20, 0))

  bt_papel = tk.CTkButton(frame_botoes, image=icon_papel, text="Papel", command=papel)
  bt_papel.grid(row=1, column=2, padx=20, pady=(20, 0))

  bt_tesoura = tk.CTkButton(frame_botoes, image=icon_tesoura, text="Tesoura", command=tesoura)
  bt_tesoura.grid(row=1, column=3, padx=(0, 20), pady=(20, 0))

  resultado = tk.CTkLabel(frame_botoes, text="JOKENPÔ?", font=("Verdana", 18))
  resultado.grid(row=2, columnspan=4, pady=(20, 0), padx=20)

  pontos_voce = tk.CTkLabel(frame_botoes, text="Você: 0", font=("Arial", 16), text_color='green')
  pontos_voce.grid(row=3, column=1, pady=10, padx=10)
  
  pontos_empate = tk.CTkLabel(frame_botoes, text="Empate: 0", font=("Arial", 16), text_color='blue')
  pontos_empate.grid(row=3, column=2, pady=10, padx=10)
  
  pontos_app = tk.CTkLabel(frame_botoes, text="App: 0", font=("Arial", 16), text_color='red')
  pontos_app.grid(row=3, column=3, pady=10, padx=10)
  


def main():
  global janela
  janela = tk.CTk()
  janela.title("JOKENPÔ - Pedra, Papel ou Tesoura")
  interface()
  janela.mainloop()

main()