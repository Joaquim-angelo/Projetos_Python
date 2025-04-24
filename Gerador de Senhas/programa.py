from customtkinter import *
from random import randint, shuffle

tela=CTk()
tela.title("Gerador de Senhas")
tela.geometry("420x340")
tela.resizable(height=False,width=False)
tela.configure(fg_color="dark gray")
set_default_color_theme("green")

numeros=BooleanVar()
letras=BooleanVar()
simbolos=BooleanVar()

def numbers():
    #0-9 em caracteres unicode
    return chr(randint(48,57))

def a_z():
    #a-z em caracteres unicode
    return chr(randint(97,122))
def A_Z():
    #A-Z em caracteres unicode
    return chr(randint(65,90))
def especiais():
    #Caracteres especiais em caracteres unicode
    return chr(randint(33,47))

def mostrar():
    lenght=8
    senha=[]

    for i in range(lenght):
        if numeros.get():
            senha.append(numbers())
        if letras.get():
            senha.append(a_z())
            senha.append(A_Z())
        if simbolos.get():
            senha.append(especiais())
    senha=senha[:lenght]
    #Shuflle: função random pra embaralhar elementos de uma lista
    shuffle(senha)
    Texto.configure(text=senha)

CTkLabel(tela,text="Gerador de Senhas",font=(("arial bold",20)),text_color="white").pack(pady=15)
CTkCheckBox(tela,text="Números",font=(("arial bold",17)),variable=numeros,text_color="white").pack(pady=5)
CTkCheckBox(tela,text="Letras",font=(("arial bold",17)),variable=letras,text_color="white").pack(pady=5)
CTkCheckBox(tela,text="Símbolos",font=(("arial bold",17)),variable=simbolos,text_color="white").pack(pady=5)
CTkButton(tela,text="Mostrar",font=(("arial bold",17)),command=mostrar,fg_color="dark blue",hover_color="green").pack(pady=15)

Texto = CTkLabel(tela, text="", font=CTkFont(size=14),width=140,bg_color="white",text_color="black")
Texto.pack(pady=5)

tela.mainloop()