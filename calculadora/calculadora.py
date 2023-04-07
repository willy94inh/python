#/****@author William Sicoli****/
 

import customtkinter
from tkinter import *
from tkinter import messagebox

#Titulo, tamano y fondo
app= customtkinter.CTk()
app.title("Mi calculadora")
app.geometry("250x270")
app.resizable(False, False)
app.config(bg="#000000")

#Fuentes
fuente1=('Arial',20,'bold')

#funciones
a=0
ecuacion=""

def show(valor):
    global a
    global ecuacion
    ecuacion+=valor
    resultado.insert(a,valor)
    a=a+1
    

def limpiar():
    global ecuacion
    resultado.delete(0,END)
    ecuacion=""

def calcular ():
    try:
        global ecuacion
        resultado_funcion=""
        resultado_funcion=eval(ecuacion)
        limpiar()
        resultado.insert(0,resultado_funcion)
        ecuacion=""
    except:
        messagebox.showerror(title="Error",message="Ingrese un valor")



#Aqui se muestra el resultado
resultado=customtkinter.CTkEntry(app,textvariable="",font=fuente1,width=350,fg_color="#000000",border_color="#000000")
resultado.place(x=0,y=10)

#Botones
boton_limpiar=customtkinter.CTkButton(app,command=limpiar,text="C",font=fuente1,width=230,height=2,fg_color="#2e2a27",hover_color="#b5520b")
boton_limpiar.place(x=10,y=60)

boton7=customtkinter.CTkButton(app,command=lambda:show("7"),text="7",font=fuente1,width=50,height=2,fg_color="#2e2a27",hover_color="#b5520b")
boton7.place(x=10,y=100)

boton4=customtkinter.CTkButton(app,command=lambda:show("4"),text="4",font=fuente1,width=50,height=2,fg_color="#2e2a27",hover_color="#b5520b")
boton4.place(x=10,y=135)

boton1=customtkinter.CTkButton(app,command=lambda:show("1"),text="1",font=fuente1,width=50,height=2,fg_color="#2e2a27",hover_color="#b5520b")
boton1.place(x=10,y=170)

boton8=customtkinter.CTkButton(app,command=lambda:show("8"),text="8",font=fuente1,width=50,height=2,fg_color="#2e2a27",hover_color="#b5520b")
boton8.place(x=70,y=100)

boton5=customtkinter.CTkButton(app,command=lambda:show("5"),text="5",font=fuente1,width=50,height=2,fg_color="#2e2a27",hover_color="#b5520b")
boton5.place(x=70,y=135)

boton2=customtkinter.CTkButton(app,command=lambda:show("2"),text="2",font=fuente1,width=50,height=2,fg_color="#2e2a27",hover_color="#b5520b")
boton2.place(x=70,y=170)

boton9=customtkinter.CTkButton(app,command=lambda:show("9"),text="9",font=fuente1,width=50,height=2,fg_color="#2e2a27",hover_color="#b5520b")
boton9.place(x=130,y=100)

boton_menos=customtkinter.CTkButton(app,command=lambda:show("-"),text="-",font=fuente1,width=50,height=2,fg_color="#2e2a27",hover_color="#b5520b")
boton_menos.place(x=190,y=100)

boton6=customtkinter.CTkButton(app,command=lambda:show("6"),text="6",font=fuente1,width=50,height=2,fg_color="#2e2a27",hover_color="#b5520b")
boton6.place(x=130,y=135)

boton_mas=customtkinter.CTkButton(app,command=lambda:show("+"),text="+",font=fuente1,width=50,height=2,fg_color="#2e2a27",hover_color="#b5520b")
boton_mas.place(x=190,y=135)

boton3=customtkinter.CTkButton(app,command=lambda:show("3"),text="3",font=fuente1,width=50,height=2,fg_color="#2e2a27",hover_color="#b5520b")
boton3.place(x=130,y=170)

boton_multiplicacion=customtkinter.CTkButton(app,command=lambda:show("*"),text="x",font=fuente1,width=50,height=2,fg_color="#2e2a27",hover_color="#b5520b")
boton_multiplicacion.place(x=190,y=170)

boton_coma=customtkinter.CTkButton(app,command=lambda:show("."),text=".",font=fuente1,width=50,height=2,fg_color="#2e2a27",hover_color="#b5520b")
boton_coma.place(x=10,y=205)

boton0=customtkinter.CTkButton(app,command=lambda:show("0"),text="0",font=fuente1,width=50,height=2,fg_color="#2e2a27",hover_color="#b5520b")
boton0.place(x=70,y=205)

boton_calcular=customtkinter.CTkButton(app,command=calcular,text="=",font=fuente1,width=50,height=2,fg_color="#2e2a27",hover_color="#b5520b")
boton_calcular.place(x=130,y=205)

boton_division=customtkinter.CTkButton(app,command=lambda:show("/"),text="/",font=fuente1,width=50,height=2,fg_color="#2e2a27",hover_color="#b5520b")
boton_division.place(x=190,y=205)

app.mainloop()
