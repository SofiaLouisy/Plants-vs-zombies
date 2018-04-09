"""
Module for an object with properties position, movement, graphocs and width.

@author Sofia Louisy
@company Stickybit AB
"""
import PlantsvsZombies.Properties as Properties

class myObject:
    def __init__(self):
        self.Position = Properties.Position()
        self.grfx = "PlantsvsZombies/Actor/Zombie/rsz_ozzy.gif"#"rsz_ozzy.jpg"
        self.width = 36
        self.dying = False
        self.stillHangingOn = 15

    @staticmethod
    def getInstance():
        return __class__()
    
    def getPosition(self):
        """
        Returns the position of the object

        :return (x,y) the position as a tuple
        """

        return self.Position.x,self.Position.y

    def isDead(self):
        self.stillHangingOn -= 1
        return self.stillHangingOn <= 0
        

    
    def isDying(self):
        return self.dying