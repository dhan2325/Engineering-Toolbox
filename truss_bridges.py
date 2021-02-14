import pygame
from sys import exit

def create_pop():
    pygame.init()

    screen = pygame.display.set_mode((1600, 800)) #create the screen
    running = True

    #Title, Icon
    pygame.display.set_caption("Truss Types")

    #truss image
    trussimg = pygame.image.load('types.png')
    img_x = 200
    img_y = 350

    def truss():
        screen.blit(trussimg, (img_x,img_y))


    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill((30,200,200))
        truss()
        pygame.display.update()