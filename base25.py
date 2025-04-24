import tkinter as tk

janela = None

def interface():
  rotulo = tk.Label(janela, text="Tarefa")
  rotulo.pack(pady=10)

  tarefa = tk.Entry(janela, width=70)
  tarefa.pack(pady=10, padx=20)

  bt_adicionar = tk.Button(janela, text="Adicionar Tarefa")
  bt_adicionar.pack(pady=10)

  lista = tk.Listbox(janela, width=70, height=10)
  lista.pack(padx=20, pady=10)

  bt_concluir = tk.Button(janela, text='Concluir')
  bt_concluir.pack(pady=10)

def main():
  janela = tk.Tk()
  janela.title("Gerenciador de Tarefas")
  interface()
  janela.mainloop()

main()
