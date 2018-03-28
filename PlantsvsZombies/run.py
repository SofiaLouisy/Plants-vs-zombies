#from Actor.Zombie.Zombie import *
#from Actor.Plant.Plant import *
from Board.Board import Board
import Actor
import pygame
import sys
#pygame.examples.aliens

#Initialize all internal modules
pygame.init()

size = width, height = Board.size

#Inititing zombie
zombie = Actor.Zombie()
plant = Actor.Plant()

#Setting background
green = 100,255,100
background_img = pygame.image.load(Board.grfx)

#Create surface object (represents the displayed graphics)
screen = pygame.display.set_mode(size)

#Creates surface with data from image
zombie_img = pygame.image.load(zombie.grfx)
plant_img = pygame.image.load(plant.grfx)

print(plant.position())

#Gives us a rect if we want
#zombie_rect = zombie_img.get_rect(center = zombie.position())#center = )

while True:
    #Check for user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #Erase screen
    screen.blit(background_img,(0,0))

    #Move image and draw on screen


    if(zombie.isBlocked(plant)):
        screen.blit(zombie_img,zombie.position())
        zombie.attack(plant)
    else:


        screen.blit(zombie_img,zombie.move())
    
    

    screen.blit(plant_img,plant.position())

    #makes everything we just drew visible
    #this strategy makes sure we only see completed stuff
    pygame.display.flip()