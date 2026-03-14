import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Formulário de Cadastro")
root.geometry("400x350")

def dados():
   
    nome = entry_nome.get()
    idade = entry_idade.get()
    email = entry_email.get()
    endereco = entry_endereco.get()
    celular = entry_celular.get()
    cep = entry_cep.get()
    cidade = entry_cidade.get()
    cursos = entry_cursos.get()

    resultado = (f'''Nome: {nome}\nIdade: {idade}\nE-mail: {email}\n"Endereço: {endereco}\nCelular: {celular}\n"CEP: {cep}\nCidade: {cidade}\nCursos: {cursos}''')
    
    messagebox.showinfo("Dados Salvos", f"Dados cadastrados com sucesso:\n\n{resultado}")

tk.Label(root, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
entry_nome = tk.Entry(root, width=30)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Idade:").grid(row=1, column=0, padx=10, pady=5)
entry_idade = tk.Entry(root, width=30)
entry_idade.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="E-mail:").grid(row=2, column=0, padx=10, pady=5)
entry_email = tk.Entry(root, width=30)
entry_email.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Endereço:").grid(row=3, column=0, padx=10, pady=5)
entry_endereco = tk.Entry(root, width=30)
entry_endereco.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Celular:").grid(row=4, column=0, padx=10, pady=5)
entry_celular = tk.Entry(root, width=30)
entry_celular.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="CEP:").grid(row=5, column=0, padx=10, pady=5)
entry_cep = tk.Entry(root, width=30)
entry_cep.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Cidade:").grid(row=6, column=0, padx=10, pady=5)
entry_cidade = tk.Entry(root, width=30)
entry_cidade.grid(row=6, column=1, padx=10, pady=5)

tk.Label(root, text="Cursos:").grid(row=7, column=0, padx=10, pady=5, )
entry_cursos = tk.Entry(root, width=30)
entry_cursos.grid(row=7, column=1, padx=10, pady=5)

btn_enviar = tk.Button(root, text="Cadastrar", command=dados)
btn_enviar.grid(row=8, column=0, columnspan=2, pady=15)

root.mainloop()
