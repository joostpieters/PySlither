import pygame

pygame.init()

white = (220,220,220) #Seteando colores RGB customizados
black = (0,0,0)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("La serpienteh")


#pygame.display.update()

gameExit = False

#--------------------------------------------------

lead_x = 300 #Primer bloque de la serpiente
lead_y = 300
lead_x_change = 0

clock = pygame.time.Clock()


while gameExit == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -11
            if event.key == pygame.K_RIGHT:
                lead_x_change = 11
            if event.key == pygame.K_UP:
                lead_y = lead_y - 7
            if event.key == pygame.K_DOWN:
                lead_y = lead_y + 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                lead_x_change = 0

    lead_x = (lead_x)+(lead_x_change)

    gameDisplay.fill(white) #Seteando el FONDO como blanco
    
    pygame.draw.rect(gameDisplay, red,[lead_x,lead_y,30,30]) #Serpiente
#Dibuja rectangulo. En gameDisplay. Rojo. Posicionado en 400x300. 30x30 de alto y ancho.
#Mas info: https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect
    gameDisplay.fill(black, rect=[200,200,100,100]) #Otra forma de crear formas
    pygame.display.update() #Updatear asi se ve el fondo blanco

    clock.tick(40)


pygame.quit()
quit()
