import pygame
import button
from datetime import datetime
from tkinter import *
from tkinter import messagebox

# Inicializando fonte
pygame.font.init()

#configurando a tela
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1200

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Gerador de Cracha')


#carregando imagens
cracha_img = pygame.image.load('Gerar_Cracha.png').convert_alpha()

#carregando crachas gerados
def crachas_manha_draw(x, y):
    crachas_manha = fonte.render("Voluntarios manhã: " + str(numero_crachas_manha), True, (000, 000, 000))
    screen.blit(crachas_manha, (x, y))

def crachas_tarde_draw(x, y):
    crachas_tarde = fonte.render("Voluntarios tarde: " + str(numero_crachas_tarde), True, (000, 000, 000))
    screen.blit(crachas_tarde, (x, y))
    


#numero de crachas gerados
numero_crachas_manha = 0
numero_crachas_tarde = 0
fonte = pygame.font.Font('FreeSansBold.ttf', 32)

#carregando botão
cracha_button = button.Button(1000, 100, cracha_img, 0.8)



#game loop
run = True
while run:

    #carregando a hora
    now = datetime.now().hour
    
    #carregando as imagens
    screen.fill((255, 255, 255))
    crachas_manha_draw(110, 110)
    crachas_tarde_draw(110, 210)

    cracha_button.draw(screen)

    #click event
    if cracha_button.click() == True:
        if now >= 6 and now <= 11:
            numero_crachas_manha += 1
        elif now >= 12 and now <= 18:
            numero_crachas_tarde += 1

    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:

            Tk().wm_withdraw() #to hide the main window
            if messagebox.askquestion('','Quer fechar o programa?') == 'yes':
                run = False
            
    pygame.display.update()


pygame.quit()