"""
Module of an actor with properties health, position, graphics and width

@author Sofia Louisy
@company Stickybit AB
"""

import PlantsvsZombies.Properties as Properties

class Actor:
    def __init__(self):
        self.Health = Properties.Health()
        self.Position = Properties.Position()
        self.stillHangingOn = 0
        #grfx
        self.grfx = "PlantsvsZombies/Actor/dead_ozzy.gif"#"rsz_ozzy.jpg"
        self.width = 70
        #with Image.open(self.grfx) as img:
        #    self.width = img.size[0]

    def __lt__(self,other):
        return self.Position < other.Position
    def __le__(self,other):
        return self.Position <= other.Position
    def __eq__(self,other):
        return self.Position == other.Position
    def __ne__(self,other):
        return self.Position != other.Position
    def __gt__(self,other):
        return self.Position > other.Position
    def __ge__(self,other):
        return self.Position >= other.Position

    def getPosition(self):
        """
        Function for retrieving position

        :return (x,y) position as a tuple
        """
        return self.Position.x,self.Position.y
     
    def isBlocked(self,other):
        """
        Function for knowing if an actor is blocked by another actor

        :param other The other actor
        :return True if blocked by other, False otherwise
        """
        if issubclass(other.__class__,Actor):
            return other.getPosition()[0]+other.width//2 >= self.getPosition()[0]-self.width//2
        else:
            raise TypeError
            return -1

    def isDead(self):
        """
        Use if isDying.

        :return True if dead, False otherwise
        """
        self.stillHangingOn -= 1
        return self.stillHangingOn <= 0
    
    def isDying(self):
        return self.Health.hitpoints <= 0