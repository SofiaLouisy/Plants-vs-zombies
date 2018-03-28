from PlantsvsZombies.Board.Board import Board
from PlantsvsZombies.AdventureGames.A1 import *
import PlantsvsZombies.Actor as Actor
import pygame
import sys

#Initialize all internal modules
pygame.init()

size = width, height = Board.size

#Inititing zombie
game = A1()

#Setting background
green = 100,255,100
background_img = pygame.image.load(Board.grfx)

#Create surface object (represents the displayed graphics)
screen = pygame.display.set_mode(size)

#Gives us a rect if we want
#zombie_rect = zombie_img.get_rect(center = zombie.position())#center = )

while True:
    #Check for user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #Erase screen
    screen.blit(background_img,(0,0))

    #Move image and draw on screen
    
    gameState = game.run()

    if(gameState == "GAMEOVER"):
        # Fill background
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((0, 0, 0))

        # Display some text
        font = pygame.font.Font(None, 200)
        text = font.render("Game Over!", 1, (100,0,0))
        textpos = text.get_rect()
        textpos.center = background.get_rect().center
        background.blit(text, textpos)

        # Blit everything to the screen
        screen.blit(background, (0, 0))
        pygame.display.flip()
        pygame.time.wait(3000)
        sys.exit()
    
    elif(gameState == "WON"):
            # Fill background
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((100,255,100))

        # Display some text
        font = pygame.font.Font(None, 200)
        text = font.render("VICTORY!", 1, (0, 100, 0))
        textpos = text.get_rect()
        textpos.center = background.get_rect().center
        background.blit(text, textpos)

        # Blit everything to the screen
        screen.blit(background, (0, 0))
        pygame.display.flip()
        pygame.time.wait(3000)
        sys.exit()    
    
    
    actorsGenerator = game.getActors()

    for actor in actorsGenerator:
        screen.blit(pygame.image.load(actor.grfx),actor.getPosition())

    #makes everything we just drew visible
    #this strategy makes sure we only see completed stuff
    pygame.display.flip()