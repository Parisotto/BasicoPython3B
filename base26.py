import tkinter as tk
from tkinter import messagebox as msg

janela = None
agenda = []

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
  

def incluir():
  contato = {}
  nome = entry_nome.get()
  celular = entry_celular.get()
  email = entry_email.get()

  if nome and celular and email:
    contato = {"nome":nome, "celular":celular, "email":email}
    agenda.append(contato)

    entry_email.delete(0, tk.END)
    entry_nome.delete(0, tk.END)
    entry_celular.delete(0, tk.END)
    entry_nome.focus_set()

    lista.delete(0, tk.END)
    for item in agenda:
      lista.insert(tk.END, f"{item['nome']} - {item['celular']} - {item['email']}")
  else:
    msg.showwarning("Aviso", "Digite o nome, celular e email para incluir.")

def interface():
  global entry_nome, entry_celular, entry_email, lista

  quadro = tk.Frame(janela)
  quadro.pack(padx=20, pady=20, fill="both", expand=True)

  label_nome = tk.Label(quadro, text="Nome:")
  label_nome.pack(padx=20, pady=(10, 0), anchor='w')
  entry_nome = tk.Entry(quadro, width=50)
  entry_nome.pack(padx=20)

  label_celular = tk.Label(quadro, text="Celular:")
  label_celular.pack(padx=20, pady=(10, 0), anchor='w')
  entry_celular = tk.Entry(quadro, width=50)
  entry_celular.pack(padx=20)

  label_email = tk.Label(quadro, text="E-mail:")
  label_email.pack(padx=20, pady=(10, 0), anchor='w')
  entry_email = tk.Entry(quadro, width=50)
  entry_email.pack(padx=20)

  frame_botoes = tk.Frame(quadro)
  frame_botoes.pack()

  botao_incluir = tk.Button(frame_botoes, text="Incluir", command=incluir)
  botao_buscar = tk.Button(frame_botoes, text="Buscar", command=buscar)

  botao_incluir.grid(row=0, column=0, padx=10, pady=10)
  botao_buscar.grid(row=0, column=1, padx=10, pady=10)

  lista = tk.Listbox(quadro, width=50)
  lista.pack(pady=(20, 0))


def main():
  janela = tk.Tk()
  janela.title("Agenda de Contatos")
  interface()
  janela.mainloop()

main()