import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
#enviar para beatriz.cristina@sp.senai.br
# Inicialização do Banco de Dados
def init_db():
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT NOT NULL,
            Email TEXT NOT NULL,
            Telefone TEXT NOT NULL,
            Endereço TEXT NOT NULL,
            Serviço TEXT NOT NULL,     
            Total TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

class ClienteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ODG-MOTOS")
        self.root.geometry("800x600") 
        
        self.nome_var = tk.StringVar()
        self.tel_var = tk.StringVar()
        self.end_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.servico_var = tk.StringVar()
        self.total_var = tk.StringVar()
        self.selected_id = None

        # --- Imagens (Logo e Ícone) ---
        try:
            img_icon = tk.PhotoImage(file='odg-removebg-preview.png')
            root.tk.call('wm', 'iconphoto', root._w, img_icon)

            img_open = Image.open("odg-removebg-preview.png")
            img_resized = img_open.resize((100, 100))
            self.logo_img = ImageTk.PhotoImage(img_resized)
            tk.Label(root, image=self.logo_img).pack(pady=5)
        except:
            tk.Label(root, text="ODG MOTOS", font=("Arial", 20, "bold")).pack()

        # Interface - Campos
        frame_campos = tk.LabelFrame(root, text="Dados do Cliente", padx=10, pady=10)
        frame_campos.pack(fill="x", padx=10, pady=5)

        tk.Label(frame_campos, text="Nome:").grid(row=0, column=0, sticky="w")
        tk.Entry(frame_campos, textvariable=self.nome_var, width=25).grid(row=0, column=1, padx=5, pady=2)

        tk.Label(frame_campos, text="Email:").grid(row=1, column=0, sticky="w")
        tk.Entry(frame_campos, textvariable=self.email_var, width=25).grid(row=1, column=1, padx=5, pady=2)

        tk.Label(frame_campos, text="Telefone:").grid(row=0, column=2, sticky="w", padx=10)
        tk.Entry(frame_campos, textvariable=self.tel_var, width=20).grid(row=0, column=3, pady=2)

        tk.Label(frame_campos, text="Endereço:").grid(row=1, column=2, sticky="w", padx=10)
        tk.Entry(frame_campos, textvariable=self.end_var, width=20).grid(row=1, column=3, pady=2)

        tk.Label(frame_campos, text="Serviço:").grid(row=0, column=4, sticky="w", padx=10)
        tk.Entry(frame_campos, textvariable=self.servico_var, width=20).grid(row=0, column=5, pady=2)

        tk.Label(frame_campos, text="Total:").grid(row=1, column=4, sticky="w", padx=10)
        tk.Entry(frame_campos, textvariable=self.total_var, width=20).grid(row=1, column=5, pady=2)

        # Botões
        frame_botoes = tk.Frame(root)
        frame_botoes.pack(pady=10)
        tk.Button(frame_botoes, text="Cadastrar", bg="green", fg="white", width=12, command=self.add_cliente).pack(side="left", padx=5)
        tk.Button(frame_botoes, text="Atualizar", bg="blue", fg="white", width=12, command=self.update_cliente).pack(side="left", padx=5)
        tk.Button(frame_botoes, text="Excluir", bg="red", fg="white", width=12, command=self.delete_cliente).pack(side="left", padx=5)
        tk.Button(frame_botoes, text="Limpar", width=12, command=self.clear_fields).pack(side="left", padx=5)

        # Tabela
        cols = ("ID", "Nome", "Email", "Telefone", "Endereço", "Serviço", "Total")
        self.tree = ttk.Treeview(root, columns=cols, show='headings')
        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.column("ID", width=40)
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)
        self.tree.bind('<<TreeviewSelect>>', self.select_item)

        self.load_data()

    def load_data(self):
        for item in self.tree.get_children(): self.tree.delete(item)
        conn = sqlite3.connect('clientes.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        for row in cursor.fetchall():
            self.tree.insert("", "end", values=row)
        conn.close()

    def add_cliente(self):
        if not self.nome_var.get() or not self.total_var.get():
            messagebox.showwarning("Erro", "Nome e Total são obrigatórios!")
            return
        conn = sqlite3.connect('clientes.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (Nome, Email, Telefone, Endereço, Serviço, Total) VALUES (?,?,?,?,?,?)",
                       (self.nome_var.get(), self.email_var.get(), self.tel_var.get(), self.end_var.get(), self.servico_var.get(), self.total_var.get()))
        conn.commit()
        conn.close()
        self.load_data()
        self.clear_fields()

    def select_item(self, event):
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected)['values']
            if values:
                self.selected_id = values[0]
                self.nome_var.set(values[1])
                self.email_var.set(values[2])
                self.tel_var.set(values[3])
                self.end_var.set(values[4])
                self.servico_var.set(values[5])
                self.total_var.set(values[6])

    def update_cliente(self):
        if not self.selected_id: 
            messagebox.showwarning("Erro", "Selecione um cliente na tabela!")
            return
        conn = sqlite3.connect('clientes.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE clientes SET Nome=?, Email=?, Telefone=?, Endereço=?, Servico=?, Total=? WHERE id=?",
                       (self.nome_var.get(), self.email_var.get(), self.tel_var.get(), self.end_var.get(), self.servico_var.get(), self.total_var.get(), self.selected_id))
        
        conn.commit()
        conn.close()
        self.load_data()
        messagebox.showinfo("Sucesso", "Dados atualizados!")

    def delete_cliente(self):
        if not self.selected_id: return
        if messagebox.askyesno("Confirmar", "Deseja excluir este cliente?"):
            conn = sqlite3.connect('clientes.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM clientes WHERE id=?", (self.selected_id,))
            conn.commit()
            conn.close()
            self.load_data()
            self.clear_fields()

    def clear_fields(self):
        self.nome_var.set(""); self.email_var.set(""); self.tel_var.set("")
        self.end_var.set(""); self.servico_var.set(""); self.total_var.set("")
        self.selected_id = None

if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    app = ClienteApp(root)
    root.mainloop()
