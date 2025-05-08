import customtkinter as ctk 
# Para instalar o CustomTkinter, no Terminal digite:
# pip install customtkinter
# De ENTER e espere a instalação

# ctk.set_appearance_mode('dark')

def validar_login():
  usuario = entry_nome.get().lower()
  senha = entry_senha.get().lower()

  if usuario and senha:
    if usuario == "Edson".lower() and senha == '123'.lower():
      resultado.configure(text="Login efetuado com sucesso!", text_color="green")
    else:
      resultado.configure(text="Nome ou senha incorretos!", text_color="red")
  else:
    resultado.configure(text="Digite um nome e senha!")

def interface():
  global entry_nome, entry_senha, resultado

  # ctk.CTkLabel(app, text='Node de login:').pack(pady=(10,0))
  label_nome = ctk.CTkLabel(app, text='Node de login: *')
  label_nome.pack(pady=(20, 0))

  entry_nome = ctk.CTkEntry(app, placeholder_text='Digite seu nome de usuário', width=200)
  entry_nome.pack()

  label_senha = ctk.CTkLabel(app, text="Senha: *")
  label_senha.pack(pady=(10, 0))

  entry_senha = ctk.CTkEntry(app, width=200, show="*")
  entry_senha.pack()

  ctk.CTkButton(app, width=200, text='Login', command=validar_login).pack(pady=20)

  resultado = ctk.CTkLabel(app, text='')
  resultado.pack(pady=10)

def main():
  global app

  app = ctk.CTk()
  app.title("Sistema de Login")
  app.geometry('500x300')
  interface()
  app.mainloop()

main()
