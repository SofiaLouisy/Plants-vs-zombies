'''
Module to run an adventure game of Plants vs Zombies

@author Sofia Louisy
@company Stickybit AB
'''
from PlantsvsZombies.Board.Board import Board
import PlantsvsZombies.Actor as Actor
from random import randint

class A1:
    def __init__(self):
        
        self.Board = Board()
        self.Board.setLanes(2)
        self.nrOfZombies = 1
        print("GridPos: "+ str(self.Board.getPosition(0,1)))
        print("lanepositions: " + str(self.Board.getLanePositions()))

        self.initiate_zombies()
        self.initiate_plants()


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

    def run(self):
        """
        Function to run one iteration of the game.

        :return string of state of the game, GAMEOVER, WON or RUNNING
        """

        gameWon = True

        #Loop through lanes
        for i in range(self.Board.lanes):
            
            for plant in self.plants[i]:
                #Attack zombie
                pass
            for zombie in self.zombies[i]:
                gameWon = False
                if self.plants[i]:
                    if(zombie.isBlocked(self.plants[i][0])):
                        zombie.attack(self.plants[i][0])
                        if self.plants[i][0].isDead():
                            self.plants[i].remove(self.plants[i][0])
                    else:
                        zombie.move()
                else:
                    zombie.move()
                if zombie.position()[0] <= -zombie.width:
                    return "GAMEOVER"
        if gameWon:
            return "WON"
        else:
            return "RUNNING"

    def initiate_zombies(self):
        
        self.zombies = []
        for i in range(self.Board.lanes):
            self.zombies.append([])

        #Initiate zombies on random lanes
        lanePositions = self.Board.getLanePositions()

        for i in range(self.nrOfZombies):
            lane = randint(0,self.Board.lanes-1)
            self.zombies[lane].append(Actor.Zombie())
            self.zombies[lane][-1].Position.y = lanePositions[lane]

    def initiate_plants(self):

        self.plants = []
        for i in range(self.Board.lanes):
            self.zombies.append([])
            self.plants.append([])

        self.plants[0].append(Actor.Plant())
        self.plants[0].append(Actor.Plant())

        if self.Board.putObject(0,1):
            self.plants[0][0].setPosition(self.Board.getPosition(0,1))
        if self.Board.putObject(0,0):
            self.plants[0][1].setPosition(self.Board.getPosition(0,0))