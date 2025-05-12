from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

#criar conexão com sqlite3
conexao=sqlite3.connect('cadastro')
cursor=conexao.cursor()

# Criar tabela se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL,
        cidade TEXT NOT NULL
    )
''')
conexao.commit()

def cadastrar():
    Nome = nome.get()
    Email = cpf.get()
    Telefone= telefone.get()
    Cidade = cidade.get()
    
    if Nome == '' or Email == '' or Telefone == '' or Cidade == '':
        messagebox.showwarning("Atenção", "Preencha todos os campos.")
        return
    
    cursor.execute('INSERT INTO usuarios (nome, email,telefone,cidade) VALUES (?, ?,?,?)', (Nome, Email,Telefone,Cidade))
    conexao.commit()
    messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
    nome.delete(0, END)
    cpf.delete(0, END)
    telefone.delete(0,END)
    cidade.delete(0,END)


def buscar():
    cursor.execute("SELECT nome, email,telefone,cidade FROM usuarios")
    usuarios = cursor.fetchall()
    return usuarios

def listar():
    #deletar dados anteriores
    for item in tabela.get_children():
        tabela.delete(item)

    #escrever novos dados
    usuarios = buscar()
    for usuario in usuarios:
        tabela.insert("", "end", values=usuario)

#Personalização de Tela
tela=Tk()
tela.geometry("600x400")
tela.resizable(height=False,width=False)
tela.configure(background="white")

Label(tela,text="Cadastro",font=(("Arial bold"),20),background="white").place(x=240,y=0)

Label(tela,text="Nome: ",font=(("Arial bold"),12),background="white").place(x=10,y=45)
nome = Entry(tela,background="light gray",width=35)
nome.place(x=70,y=49)

Label(tela,text="CPF: ",font=(("Arial bold"),12),background="white").place(x=10,y=80)
cpf = Entry(tela,background="light gray",width=35)
cpf.place(x=70,y=84)

Label(tela,text="Telefone: ",font=(("Arial bold"),12),background="white").place(x=300,y=45)
telefone = Entry(tela,background="light gray",width=20)
telefone.place(x=375,y=49)

Label(tela,text="Cidade: ",font=(("Arial bold"),12),background="white").place(x=300,y=80)
cidade = Entry(tela,background="light gray",width=25)
cidade.place(x=375,y=84)

Button(tela,text="Cadastrar",width=25,command=cadastrar).place(x=90,y=120)
Button(tela,text="Listar",width=25,command=listar).place(x=300,y=120)

colunas=("nome","CPF","Telefone", "Cidade")
tabela=ttk.Treeview(tela,columns=colunas,show="headings")
for x in colunas:
    tabela.heading(x,text=x)
    tabela.column(x,width=145)
tabela.place(x=10,y=160)

tela.mainloop()