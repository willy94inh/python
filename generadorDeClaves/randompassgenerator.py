import tkinter
import random

ventana = tkinter.Tk()
ventana.title('Generador de claves')

#Variables
i = 8

#Caracteres

carac = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!$%&/()=?¿'


#Funciones
def clave_final():
    #Eliminando de pantalla la clave anterior
    pass_text.delete(0, tkinter.END)

    #Ciclo for para generar contrasena
    for claves in range(i):
        clave = ''
        clave += random.choice(carac)
        pass_text.insert(i,clave)
        
#Pantalla 
pass_text = tkinter.Entry(ventana, font='Calibri 20')
pass_text.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

#Buttons
boton_gene = tkinter.Button(ventana, text='Generar clave' , command = lambda: clave_final() )
boton_gene.grid(row=1, column=3, columnspan=2)

ventana.mainloop()
