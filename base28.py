from tkinter import messagebox as msg
import customtkinter as tk
from tkinter import Listbox

#tk.set_appearance_mode('dark')
tk.set_appearance_mode('light')

janela = None
agenda = []
indice_selecionado = None

def carga():
  global agenda
  agenda = arquivo('r')
  dados_lista_box()

def arquivo(op = 'r', contato = ''):
  arquivo = 'contatos.txt'
  try:
    with open(arquivo, op) as arq:
      if op == 'r':
        return arq.readlines()
      elif op == 'a':
        arq.write(contato)
      elif op == 'w':
        arq.writelines(contato)
  except:
    return []

def buscar():
  nome = entry_nome.get().lower().strip()
  celular = entry_celular.get().strip()
  email = entry_email.get().lower().strip()

  lista.selection_clear(0, tk.END)

  if nome or celular or email:
    for i in range(0, lista.size()):
      if nome and nome in lista.get(i).lower():
        indice = i
        break
      elif celular and celular in lista.get(i):
        indice = i
        break
      elif email and email in lista.get(i).lower():
        indice = i
        break
      else:
        indice = None

    print(indice)
    if lista.size() > 0 and indice != None:
      lista.selection_set(indice)
      lista.activate(indice)
      lista.see(indice)
    else:
      msg.showinfo("Informação", "Nenhum contato encontrado")
  else:
    msg.showerror("ERRO", "Digite nome ou celular ou email para ser buscado")
  
def excluir():
  global indice_selecionado
  if indice_selecionado is not None:
    del agenda[indice_selecionado]
    arquivo('w', agenda)
    dados_lista_box()
    entry_nome.delete(0, tk.END)
    entry_celular.delete(0, tk.END)
    entry_email.delete(0, tk.END)
  else:
    msg.showwarning("Aviso", "Selecione um contato para excluir")

def editar():
  global indice_selecionado
  if indice_selecionado is not None:
    nome = entry_nome.get()
    celular = entry_celular.get()
    email = entry_email.get()

    if nome and celular and email:
      agenda[indice_selecionado] = f"{nome} - {celular} - {email}\n"
      arquivo('w', agenda)
      dados_lista_box() 

      entry_nome.delete(0, tk.END)
      entry_celular.delete(0, tk.END)
      entry_email.delete(0, tk.END)
    else:
      msg.showwarning("Aviso", "Preencha todos os campos para editar o contato")
  else:
    msg.showwarning("Aviso", "Selecione um contato para editar.")

      

def incluir():
  #contato = {}
  nome = entry_nome.get()
  celular = entry_celular.get()
  email = entry_email.get()

  if nome and celular and email:
    #contato = {"nome":nome, "celular":celular, "email":email}
    contato = f"{nome} - {celular} - {email}\n"
    agenda.append(contato)
    arquivo('a', contato)

    entry_email.delete(0, tk.END)
    entry_nome.delete(0, tk.END)
    entry_celular.delete(0, tk.END)
    entry_nome.focus_set()

    dados_lista_box()
  else:
    msg.showwarning("Aviso", "Digite o nome, celular e email para incluir.")

def dados_lista_box():
  lista.delete(0, tk.END)
  for item in agenda:
    lista.insert(tk.END, str(item))

def selecionar_contato(event):
  global indice_selecionado
  try:
    indice_selecionado = lista.curselection()[0]
  except:
    print("Nada selecionado")

  if indice_selecionado is not None:
    contato = agenda[indice_selecionado].split(" - ")
    entry_nome.delete(0, tk.END)
    entry_nome.insert(0, contato[0])
    entry_celular.delete(0, tk.END)
    entry_celular.insert(0, contato[1])
    entry_email.delete(0, tk.END)
    entry_email.insert(0, contato[2])

def interface():
  global entry_nome, entry_celular, entry_email, lista

  quadro = tk.CTkFrame(janela)
  quadro.pack(padx=20, pady=20, fill="both", expand=True)

  label_nome = tk.CTkLabel(quadro, text="Nome:")
  label_nome.pack(padx=20, pady=(10, 0), anchor='w')
  entry_nome = tk.CTkEntry(quadro, width=350)
  entry_nome.pack(padx=20)

  label_celular = tk.CTkLabel(quadro, text="Celular:")
  label_celular.pack(padx=20, pady=(10, 0), anchor='w')
  entry_celular = tk.CTkEntry(quadro, width=350)
  entry_celular.pack(padx=20)

  label_email = tk.CTkLabel(quadro, text="E-mail:")
  label_email.pack(padx=20, pady=(10, 0), anchor='w')
  entry_email = tk.CTkEntry(quadro, width=350)
  entry_email.pack(padx=20)

  frame_botoes = tk.CTkFrame(quadro)
  frame_botoes.pack()

  botao_incluir = tk.CTkButton(frame_botoes, text="Incluir", command=incluir)
  botao_buscar = tk.CTkButton(frame_botoes, text="Buscar", command=buscar)
  botao_editar = tk.CTkButton(frame_botoes, text='Editar', command=editar)
  botao_excluir = tk.CTkButton(frame_botoes, text='Excluir', command=excluir)

  botao_incluir.grid(row=0, column=0, padx=10, pady=10)
  botao_buscar.grid(row=0, column=1, padx=10, pady=10)
  botao_editar.grid(row=1, column=0, padx=10, pady=10)
  botao_excluir.grid(row=1, column=1, padx=10, pady=10)

  lista = Listbox(quadro, width=38,
                  font=("Verdana", 12),
                  bg=quadro.cget("fg_color")[0],
                  bd=0)
  lista.pack(pady=10, padx=10)
  lista.bind('<<ListboxSelect>>', selecionar_contato)


def main():
  janela = tk.CTk()
  janela.title("Agenda de Contatos")
  interface()
  carga()
  janela.mainloop()

main()