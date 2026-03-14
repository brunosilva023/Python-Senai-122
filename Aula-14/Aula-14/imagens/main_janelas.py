import tkinter as Tk



def mostrar():
    m = input_.get()
    text_MOSTAR.config(text = m)
    



janela  =  Tk.Tk()
janela.geometry('400x600')
janela.title('ISSO É UMA JANELA')


text = Tk.Label(janela, text = 'ESCREVA ALGO',font=('Poplar Std', 15), bg = 'blue', fg = 'white' )
text.pack(pady=20)


input_ = Tk.Entry(janela, font=('arial', 15), bg='red')
input_.pack(pady = 20)


btn = Tk.Button(janela, text='CLIQUE AQUI' ,font=('arial', 15), command= mostrar)
btn.pack(pady=20)


text_MOSTAR = Tk.Label(janela, text = '',font=('Poplar Std', 15) )
text_MOSTAR.pack(pady=20)



janela.mainloop()