#Creado por William Jose Rodriguez Sicoli

import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
            

class ejemplo_gui(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("guippt.ui", self)
        self.setFixedSize(self.size())
        #Conectamos los botones a las funciones 
        self.botonPiedra.clicked.connect(self.fnpiedra)
        self.botonPapel.clicked.connect(self.fnpapel)
        self.botonTijeras.clicked.connect(self.fntijeras)
        
    def fnpiedra(self):
        #Esta funcion sirve para colocar la imagen de "piedra"
        
        opc = 1
        juego(self,opc)
        imagen = QPixmap("piedra.png")
        self.usufoto.setPixmap(imagen)
        
   
    def fnpapel(self):
        #Esta funcion sirve para colocar la imagen de "papel"
        opc = 2
        juego(self,opc)
        imagen = QPixmap("papel.png")
        self.usufoto.setPixmap(imagen)
        

    def fntijeras(self):
        #Esta funcion sirve para colocar la imagen de "tijeras"
        opc = 3
        juego(self,opc)
        imagen = QPixmap("tijera.png")
        self.usufoto.setPixmap(imagen)
      

def juego (self, opc):
        #Hacemos un random para elegir un numero del 1 al 3
        #1=piedra 2=papel 3=tijeras
        #recibimos el parametro opc para comparar
        compu = random.choice ([1,2,3])

        if compu == 1:
        #Colocamos la imagen de "piedra" de la CPU
            imagen = QPixmap("piedra.png")
            self.cpufoto.setPixmap(imagen)

        elif compu ==2:
        #Colocamos la imagen de "papel" de la CPU
            imagen = QPixmap("papel.png")
            self.cpufoto.setPixmap(imagen)

        else:
        #Colocamos la imagen de "tijera" de la CPU
            imagen = QPixmap("tijera.png")
            self.cpufoto.setPixmap(imagen)

        if opc == compu:
        #Comparamos la eleccion del usuario y la del cpu
            imagen = QPixmap("empate.png")
            self.mostrar.setPixmap (imagen)
            #print(opc," ",compu)
            #print para ver los resultado en consolo, ignorar
            
           
        elif opc == 1 and compu == 3 or opc == 2 and compu == 1 or opc == 3 and compu == 2 :
        #Comparamos la eleccion del usuario y la del cpu, aqui gana el usuario
            imagen = QPixmap("ganaste.png")
            self.mostrar.setPixmap (imagen)
            #print(opc," ",compu)
            #print para ver los resultado en consolo, ignorar
            
        else:
        #Comparamos la eleccion del usuario y la del cpu, caso contrario de ganar
                imagen = QPixmap("perdiste.png")
                self.mostrar.setPixmap (imagen)

                #print(opc," ",compu)
                #print para ver los resultado en consolo, ignorar
       

  
if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = ejemplo_gui()
    GUI.show()
    sys.exit(app.exec_())
