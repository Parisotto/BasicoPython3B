# Calculadora

import customtkinter as ctk
from tkinter import messagebox
import math

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Calculadora(ctk.CTk):
  def __init__(self):
    super().__init__()

    self.title("Calculadora")
    self.geometry("420x530")
    self.resizable(False, False)
    self.resultado = ctk.StringVar(value=".")
    self.interface()

    self.cursor_visivel = False
    self.cursor_ativo = True
    self.piscar_cursor()

  def piscar_cursor(self):
    if self.cursor_ativo:
      if self.cursor_visivel:
        self.resultado.set(".")
      else:
        self.resultado.set("")
      self.cursor_visivel = not self.cursor_visivel
      self.after(500, self.piscar_cursor)


  def interface(self):
    self.display = ctk.CTkEntry(self, textvariable=self.resultado, font=("Arial", 100), text_color="green",
                                fg_color="#90ee90", justify="right")
    self.display.grid(row=0, column=0, columnspan=4, padx=5, sticky="ew")
    self.display.bind("<Button-1>", lambda e: "break")

    botoes = [
      ['+','-','X','/'],
      ['7', '8', '9', '<'],
      ['4', '5', '6', 'C'],
      ['1', '2', '3'],
      ['0', '.', '=']
    ]

    for linha, caracteres in enumerate(botoes):
      for coluna, c in enumerate(caracteres):
        botao = ctk.CTkButton(self, text=c, font=("Arial", 20))
        cs = rs = 1
        if c == "C":
          botao.configure(fg_color="red", hover_color="#cc0000")
          rs = 2
        elif c == "=":
          botao.configure(fg_color="green", hover_color="#006400")
          cs = 2
        botao.grid(row=linha + 1, column=coluna, padx=5, 
                   pady=5, sticky="nsew", rowspan=rs, columnspan=cs)

    # Ajuste das dimensões
    for i in range(6):
      self.grid_rowconfigure(i, weight=1)
    for i in range(4):
      self.grid_columnconfigure(i, weight=1)


app = Calculadora()
app.mainloop()
