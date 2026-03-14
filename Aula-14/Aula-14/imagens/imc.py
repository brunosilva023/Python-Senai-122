import tkinter as tk

def imc_c():
    peso = float(input_peso.get())
    altura = float(input_altura.get())
    imc_cal =round(peso/(altura **2),2)
    

root = tk.Tk()
root.title('IMC')
root.geometry('500x500')
root.iconbitmap('C:/Users/Aluno/Downloads/Aula-14/imagens/ob1.png')

tk.Label(root, text = 'Digite o peso e altura para ver o IMC',font=('arial',10)).pack(pady=20)


frm = tk.Frame(root)
frm.pack(pady=20,padx=5)

input_peso = tk.Entry(frm)
tk.Label(frm, text = 'Digite o peso',font=('arial',10)).pack(pady=20)
input_peso.pack(pady=10)

input_altura = tk.Entry(frm)
tk.Label(frm, text = 'Digite a altura',font=('arial',10)).pack(pady=20)
input_altura.pack(pady=10)



btn = tk.Button(root,text = 'Digite o peso e altura para ver o IMC',font=('arial',10))
btn.pack()

tk.Label(root, text = 'IMC',font=('arial',10)).pack(pady=20)
root.mainloop()