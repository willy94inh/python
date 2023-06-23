#/****@author William Sicoli****/

#Modules/modulos
import pygame 
import pygame.locals 


pygame.init()

#Screen/Pantalla
screen_width =300
screen_height =300
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('TicTacToe')

#variables
grosor_lineas=5
posiciones =[]
click=False
pos=[]
jugador = 1
gana=0
acabado=False

#Colores/Colors 
verde=(0,255,0)
rojo=(255,0,0)
azul=(0,0,255)
white=(255,255,255)
fuente = pygame.font.SysFont(None,48)

#Boton/button
nuevo_boton = pygame.draw.rect(screen, white, (screen_width // 2 - 130, screen_height // 2, 260,50))


def game_grid ():
    fondo = (185,255,202)
    color = (50,50,50)
    screen.fill(fondo)
    for x in range (1,3):
            #Lineas de la cuadricula/grid lines Horizontal
            pygame.draw.line(screen,color,(0,x*100),(screen_width,x*100),grosor_lineas)
            #vertical
            pygame.draw.line(screen,color,(x*100,0),(x*100,screen_width),grosor_lineas)

for x in range(3):
     row = [0] * 3
     posiciones.append(row)

def dibujado():
     
     x_pos = 0
     for x in posiciones:
         y_pos = 0
         for y in x:
              if y == 1:
                   #Dibujado X/X draw
                   pygame.draw.line(screen,verde,(x_pos*100+15, y_pos*100+15),(x_pos*100+85, y_pos*100+85),grosor_lineas)
                   pygame.draw.line(screen,verde,(x_pos*100+15, y_pos*100+85),(x_pos*100+85, y_pos*100+15),grosor_lineas)
              if y == -1:
                   pygame.draw.circle(screen,rojo,(x_pos*100+50, y_pos*100+50),35,grosor_lineas)
              y_pos+=1
         x_pos+=1


def ganador ():
     global gana
     global acabado
    #Validaciones del ganador / winner validations 
     y_pos =0
     for x in posiciones:
          if sum(x) == 3:
               gana=1
               acabado=True
          if sum(x)==-3:
               gana=2
               acabado=True
          if posiciones[0][y_pos]+posiciones[1][y_pos]+posiciones[2][y_pos]==3:
               gana=1
               acabado=True
          if posiciones[0][y_pos]+posiciones[1][y_pos]+posiciones[2][y_pos]==-3:
               gana=2
               acabado=True
          y_pos+=1
        

     if posiciones[0][0]+posiciones[1][1]+posiciones[2][2] ==3 or posiciones[2][0]+posiciones[1][1]+posiciones[0][2] ==3:
        gana=1
        acabado=True
     if posiciones[0][0]+posiciones[1][1]+posiciones[2][2] ==-3 or posiciones[2][0]+posiciones[1][1]+posiciones[0][2] ==-3:
        gana=2
        acabado=True
    #Validacion empate / Tie Validation
     if acabado==False:
        empate =True
        for row in posiciones: 
                for i in row:
                    if i ==0:
                     empate=False
        if empate==True:
                acabado=True
                gana=0


def mensaje(gana):
    #Mostrar en pantalla ganador / Show winner on screen
    if gana !=0:
        text='Jugador '+str(gana) +" gana!"

    elif gana == 0:
        text="Es un empate"

    imagen = fuente.render(text,True,azul)
    pygame.draw.rect(screen, verde, (screen_width // 2 - 130, screen_height // 2 - 60, 260, 50))
    screen.blit(imagen,(screen_width // 2 - 130,screen_height // 2 - 50))

    nuevo = "Jugar de nuevo?"
    nuevo_img= fuente.render(nuevo,True,azul)
    pygame.draw.rect(screen, white, nuevo_boton)
    screen.blit(nuevo_img,(screen_width // 2 - 130,screen_height // 2 + 10))


    

estado=True 
while estado:
    game_grid()
    dibujado()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            estado=False
        
        if acabado ==0:
            if event.type==pygame.MOUSEBUTTONDOWN and click==False:
                click=True
            if event.type==pygame.MOUSEBUTTONUP and click == True:
                click =False
                pos=pygame.mouse.get_pos()
                pos_x = pos[0]
                pos_y = pos[1]
                if posiciones[pos_x //100][pos_y//100] == 0:
                    posiciones[pos_x //100][pos_y//100] = jugador
                    jugador*=-1
                    ganador()


    if acabado==True:
         mensaje(gana)
         if event.type==pygame.MOUSEBUTTONDOWN and click==False:
            click=True
         if event.type==pygame.MOUSEBUTTONUP and click == True:
            click=False
            pos=pygame.mouse.get_pos()
            #Reiniciar a 0 variables / Restore variables to 0 
            if nuevo_boton.collidepoint(pos):
                posiciones =[]
                pos=[]
                jugador = 1
                gana=0
                acabado=False
                for x in range(3):
                    row = [0] * 3
                    posiciones.append(row)
                
    pygame.display.update()


pygame.quit()
