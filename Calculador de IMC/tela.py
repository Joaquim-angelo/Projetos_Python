from customtkinter import *

app=CTk()
app.geometry("400x350")
app.resizable(height=False,width=False)

Titulo=CTkLabel(app,text="IMC",font=("Times new roman",40)).pack(pady=10,padx=10)
#Peso
Txt1=CTkLabel(app,text="PESO (KG)",font=("Times new roman",20))
Txt1.place(x=60,y=80)
Peso=CTkEntry(app,width=100)
Peso.place(x=200,y=80)

#Altura
Txt2=CTkLabel(app,text="ALTURA (M)",font=("Times new roman",20))
Txt2.place(x=60,y=120)
Altura=CTkEntry(app,width=100)
Altura.place(x=200,y=120)

#função para calcular imc
def calculadora():
    peso=float(Peso.get())
    altura=float(Altura.get())
    imc=peso/(altura*altura)
    print(imc)
    if(imc<18.5):
        resultado.configure(text=f"imc: {imc:.2f}\n Peso abaixo do normal",text_color="red")
        resultado.place(x=110,y=220)
    elif(18.5<imc<24.9):
        resultado.configure(text=f"imc: {imc:.2f}\n Peso normal",text_color="green")
        resultado.place(x=150,y=220)
    elif(imc>24.9):
        resultado.configure(text=f"imc: {imc:.2f}\n Acima do peso",text_color="red")
        resultado.place(x=140,y=220)
        
#Botão confirmar
Btn=CTkButton(master=app,text="Confirmar",fg_color="dark blue",hover_color="green",width=100,corner_radius=30,command=calculadora)
Btn.place(x=160,y=180)

#Resultado a ser exibido na tela
resultado=CTkLabel(app,text='',font=("Times new roman",20),text_color="dark blue")

app.mainloop()