from customtkinter import *

app=CTk()
app.title("Conversor de Bases")
app.geometry('450x350')
app.resizable(height=False,width=False)
app._set_appearance_mode("dark")

cima=CTkFrame(app,width=500,height=70,fg_color="black",corner_radius=0).place(x=0,y=0)
baixo=CTkFrame(app,width=500,height=320).place(x=0,y=80)

titulo=CTkLabel(app,text="conversor de bases numéricas",font=("Arial bold",23),fg_color="black",text_color="white")
titulo.place(x=70,y=15)

combo=CTkComboBox(app,width=140,justify=CENTER,font=("Arial",15),values=['Binario','Octal','Decimal','Hexadecimal'],corner_radius=0)
combo.place(x=35,y=100)
valor=CTkEntry(app,width=140,justify=CENTER,font=("Arial",12),corner_radius=0)
valor.place(x=180,y=100)

#Função de conversão
def conversor():
    def conversor_decimal(numero,base):
        decimal=int(numero,base)
        binario=bin(decimal)
        octal=oct(decimal)
        hexadecimal=hex(decimal)

        print(str(decimal))
        print(str(binario))
        print(str(octal))
        print(str(hexadecimal))
        resp_binario.configure(text=str(binario))
        resp_octal.configure(text=str(octal))
        resp_decimal.configure(text=str(decimal))
        resp_hexadecimal.configure(text=str(hexadecimal))
    
    numero=valor.get()
    base=combo.get()

    if base=="Binario":
        base=2
    elif base=='Octal':
        base=8
    elif base=='Decimal':
        base=10
    elif base=='Hexadecimal':
        base=16

    conversor_decimal(numero,base)

btn=CTkButton(app,text="CONVERTER",width=100,command=conversor,font=("Arial bold",12),corner_radius=0,fg_color="blue",hover_color="green")
btn.place(x=330,y=100)

label_binario=CTkLabel(app,text="BINÁRIO",font=("Arial bold",19),width=140,text_color="white",fg_color="Black")
label_binario.place(x=35,y=160)
resp_binario=CTkLabel(app,text="",font=("Arial bolf",17),width=140,fg_color="white",text_color="black")
resp_binario.place(x=180,y=160)

label_octal=CTkLabel(app,text="OCTAL",font=("Arial bold",19),width=140,text_color="white",fg_color="Black")
label_octal.place(x=35,y=200)
resp_octal=CTkLabel(app,text="",font=("Arial",17),width=140,fg_color="white",bg_color="white")
resp_octal.place(x=180,y=200)

label_decimal=CTkLabel(app,text="DECIMAL",font=("Arial bold",19),width=140,text_color="white",fg_color="Black")
label_decimal.place(x=35,y=240)
resp_decimal=CTkLabel(app,text="",font=("Arial",17),width=140,fg_color="white",bg_color="white")
resp_decimal.place(x=180,y=240)

label_hexadecimal=CTkLabel(app,text="HEXA",font=("Arial bold",19),width=140,text_color="white",fg_color="Black")
label_hexadecimal.place(x=35,y=280)
resp_hexadecimal=CTkLabel(app,text="",font=("Arial",15),width=140,fg_color="white",bg_color="white")
resp_hexadecimal.place(x=180,y=280)

app.mainloop()