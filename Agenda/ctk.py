import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3

# ---------- BANCO DE DADOS ----------
def criar_tabela():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def cadastrar_usuario(nome, email, senha):
    try:
        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False

# ---------- INTERFACE GRÁFICA ----------
def ao_cadastrar():
    nome = entry_nome.get()
    email = entry_email.get()
    senha = entry_senha.get()

    if nome and email and senha:
        sucesso = cadastrar_usuario(nome, email, senha)
        if sucesso:
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            entry_nome.delete(0, tk.END)
            entry_email.delete(0, tk.END)
            entry_senha.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "E-mail já cadastrado.")
    else:
        messagebox.showwarning("Atenção", "Preencha todos os campos.")

# Criar banco e tabela
criar_tabela()

# Criar janela principal
janela = tk.Tk()
janela.title("Cadastro de Usuário")
janela.geometry("300x250")

# Widgets
tk.Label(janela, text="Nome:").pack(pady=5)
entry_nome = tk.Entry(janela)
entry_nome.pack(pady=5)

tk.Label(janela, text="E-mail:").pack(pady=5)
entry_email = tk.Entry(janela)
entry_email.pack(pady=5)

tk.Label(janela, text="Senha:").pack(pady=5)
entry_senha = tk.Entry(janela, show="*")
entry_senha.pack(pady=5)

tk.Button(janela, text="Cadastrar", command=ao_cadastrar).pack(pady=15)

janela.mainloop()