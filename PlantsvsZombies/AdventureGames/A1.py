'''
Module to run an adventure game of Plants vs Zombies

@author Sofia Louisy
@company Stickybit AB
'''
from PlantsvsZombies.Board.Board import *
import PlantsvsZombies.Actor as Actor
from random import randint
from PlantsvsZombies.Object.Projectile.Pea.Pea import Pea as Pea

class A1:
    def __init__(self):
        
        self.Board = Board()
        self.Board.setLanes(2)
        self.nrOfZombies = 3
        self.runTime = 0
        self.gameTime = 2000
        print("GridPos: "+ str(self.Board.getPosition(0,1)))
        print("lanepositions: " + str(self.Board.getLanePositions()))

        self.initiate_zombies()
        self.initiate_plants()
        self.initiate_objects()
        self.initiate_dyingObjects()
        
        
    def getActors(self):
        """
        Function to get all game objects.
        :yield one object at a time
        """
        for zombies in self.zombies:
            for zombie in zombies:
                yield zombie
        
        for plants in self.plants:
            for plant in plants:
                yield plant

        for objects in self.objects:
            for myObject in objects:
                yield myObject
        
        for deads in self.dyingObjects:
            for dead in deads:
                yield dead

    def run(self):
        """
        Function to run one iteration of the game.

        :return string of state of the game, GAMEOVER, WON or RUNNING
        """

        gameWon = False
        if self.runTime >= 2900:
            gameWon = True

        if self.runTime == 10:
            self.addZombie()
        
        if self.runTime == 20:
            self.addZombie()
        
        if self.runTime == 30:
            self.addZombie()

        #Loop through lanes
        for i in range(self.Board.lanes):
            for myObject in self.objects[i]:
                #check if it left the screen
                object_position = myObject.getPosition()
                if object_position[0] > Board.width:
                    self.objects[i].remove(myObject)
                if myObject.isDying():
                    self.objects[i].remove(myObject)
                    self.dyingObjects[i].append(myObject)
                else:
                    if(self.zombies[i]):
                        if(myObject.isColliding(self.zombies[i][0])):
                            myObject.attack(self.zombies[i][0])
                        else:
                            myObject.move()
                    else:
                        myObject.move()

            for plant in self.plants[i]:
                #Attack zombie
                if not plant.isDying():
                    if(self.zombies[i]):
                        attackObject = plant.getAttack()
                        if attackObject:
                            self.objects[i].append(attackObject)
                else:
                    self.plants[i].remove(plant)
                    self.dyingObjects[i].append(plant)                
            self.plants[i].sort()

            for zombie in self.zombies[i]:
                gameWon = False
                
                if not zombie.isDying():
                    if self.plants[i]:
                        if(zombie.isBlocked(self.plants[i][0])):
                            zombie.attack(self.plants[i][0])
                        else:
                            zombie.move()
                    else:
                        zombie.move()
                    if zombie.getPosition()[0] <= -zombie.width:
                        return "GAMEOVER"
                else:
                    self.zombies[i].remove(zombie)
                    self.dyingObjects[i].append(zombie)
            self.zombies[i].sort()
            
            #Remove dead objects
            for dying in self.dyingObjects[i]:
                if dying.isDead():
                    self.dyingObjects[i].remove(dying)


        if gameWon:
            return "WON"
        else:
            self.runTime +=1
            return "RUNNING"

    def initiate_zombies(self):
        
        self.zombies = []
        for i in range(self.Board.lanes):
            self.zombies.append([])

    def initiate_plants(self):

        self.plants = []
        for i in range(self.Board.lanes):
            self.plants.append([])

        #dummy
        self.plants[0].append(Actor.Plant())
        self.plants[1].append(Actor.Plant())

        if self.Board.putObject(0,1):
            self.plants[0][0].setPosition(self.Board.getPosition(0,1))
        if self.Board.putObject(1,0):
            self.plants[1][0].setPosition(self.Board.getPosition(1,0))


    def initiate_objects(self):
        
        self.objects = []
        for i in range(self.Board.lanes):
            self.objects.append([])
    
    def initiate_dyingObjects(self):
        
        self.dyingObjects = []
        for i in range(self.Board.lanes):
            self.dyingObjects.append([])
    
    def addZombie(self):
        lanePositions = self.Board.getLanePositions()
        lane = randint(0,self.Board.lanes-1)
        self.zombies[lane].append(Actor.Zombie())
        self.zombies[lane][-1].Position.y = lanePositions[lane]
        
