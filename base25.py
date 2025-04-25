import tkinter as tk
from datetime import datetime as dt
from tkinter import messagebox as msg

janela = tarefa = lista = None
tarefas = []

def adicionar():
  adicionar = tarefa.get()
  if adicionar:
    tarefas.append({'data':dt.now(), 'tarefa':adicionar})
    print(tarefas)
    lista.insert(tk.END, f"{dt.now().strftime('%d/%m/%Y')} - {adicionar}")
    tarefa.delete(0, tk.END)
  else:
    msg.showwarning("Aviso!", "Digite uma tarefa.")

def concluir():
  item = lista.curselection()
  if item:
    concluida = tarefas.pop(item[0])
    lista.delete(item)
    msg.showinfo("Concluida", f"Tarefa \"{concluida['tarefa']}\" concluida.")
  else:
    msg.showerror("Erro!", "Selecione uma tarefa para concluir.")


def interface():
  global tarefa, lista

  rotulo = tk.Label(janela, text="Tarefa")
  rotulo.pack(pady=10)

  tarefa = tk.Entry(janela, width=70)
  tarefa.pack(pady=10, padx=20)

  bt_adicionar = tk.Button(janela, text="Adicionar Tarefa", command=adicionar)
  bt_adicionar.pack(pady=10)

  lista = tk.Listbox(janela, width=70, height=10)
  lista.pack(padx=20, pady=10)

  bt_concluir = tk.Button(janela, text='Concluir', command=concluir)
  bt_concluir.pack(pady=10)

def main():
  janela = tk.Tk()
  janela.title("Gerenciador de Tarefas")
  interface()
  janela.mainloop()

main()
