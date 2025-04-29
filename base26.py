import tkinter as tk

janela = None
def interface():
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


def main():
  janela = tk.Tk()
  janela.title("Agenda de Contatos")
  interface()
  janela.mainloop()

main()