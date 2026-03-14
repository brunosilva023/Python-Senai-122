import tkinter as tk


def imc_c ():
    
    peso = float(input_peso.get())
    altura=float(input_altura.get())
    imc_cal  =  round(peso/(altura ** 2), 2)
    imc.config(text =f"IMC  {imc_cal}")
    


    if imc_cal < 18.5 :
        resultado = 'Magreza'
        imc2.config(text = resultado)
    elif imc_cal >= 18.5 and imc_cal <= 24.9:
        resultado = 'Normal'
        imc2.config(text = resultado)            
    elif imc_cal >= 25 and imc_cal <= 29.9:
        resultado = 'Sobrepeso'
        imc2.config(text = resultado) 




root = tk.Tk()
root.title('IMC')
root.geometry('500x500')
root.iconbitmap('m2.png')

tk.Label(root, text = 'digite o peso e a altura para ver o IMC', font = ('arial', 15) ).pack(pady=20)

frm = tk.Frame(root)
frm.pack(pady=20,padx=5)

tk.Label(frm, text = 'Peso', font = ('arial', 15) ).pack()
input_peso = tk.Entry(frm, width=10)
input_peso.pack(pady=10)

tk.Label(frm, text = 'Altura: ', font = ('arial', 15) ).pack()
input_altura = tk.Entry(frm, width=10)
input_altura.pack(pady=10)


btn = tk.Button(root, text='calcule o IMC', command=imc_c)
btn.pack()


tk.Label(root, text = 'IMC', font = ('arial', 15) ).pack(pady=20)


imc = tk.Label(root, text = '')
imc.pack()


imc2 = tk.Label(root, text = 'Resultado ')
imc2.pack()

root.mainloop()
