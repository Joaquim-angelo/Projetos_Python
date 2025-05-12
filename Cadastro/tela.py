from customtkinter import *
from tkinter import ttk
import sqlite3

#01- Personalizando tela
tela=CTk()
tela.title("Cadastro")
tela.geometry("480x400")
tela.resizable(width=False,height=False)
tela.configure(fg_color="white")

titulo=CTkLabel(tela,text="CADASTRO",font=(("Arial bold"),21))
titulo.place(y=20,x=185)

CTkLabel(tela,text="nome",font=(("Arial",18))).place(y=60,x=20)
nome=CTkEntry(tela,width=275).place(y=60,x=80)

CTkLabel(tela,text="CPF",font=(("Arial",18))).place(y=90,x=20)
nome=CTkEntry(tela,width=140).place(y=90,x=80)

CTkButton(tela,text="Adicionar",fg_color="green",hover_color="gray").place(y=130,x=20)
CTkButton(tela,text="Remover",fg_color="green",hover_color="gray").place(y=130,x=170)
CTkButton(tela,text="Atualizar",fg_color="green",hover_color="gray").place(y=130,x=320)

#02-Configurando banco de dados

#quando ocorrer a primeira conexão será criado o banco cadastro
conexao = sqlite3.connect("cadastro")
cursor = conexao.cursor()
#comando para criar tabela das pessoas no banco cadastro
cursor.execute("""
    CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf INTENGER NOT NULL,
        idade INTEGER NOT NULL
    )"""
)
conexao.commit()

tela.mainloop()