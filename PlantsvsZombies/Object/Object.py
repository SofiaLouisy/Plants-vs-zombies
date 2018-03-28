"""
Module for an object with properties position, movement, graphocs and width.

@author Sofia Louisy
@company Stickybit AB
"""
import PlantsvsZombies.Properties as Properties

class Object:
    def __init__(self):
        self.Position = Properties.Position()
        self.Movement = Properties.FastMovement()
        self.grfx = "Actor/Zombie/ozzy.jpg"#"rsz_ozzy.jpg"
        self.width = 36
    
    def getPosition(self):
        """
        Returns the position of the object

        :return (x,y) the position as a tuple
        """

        return self.Position.x,self.Position.y
    
    def isHit(self,other):
        """
        Checks if the object collides with an Actor

        :param other the Actor
        :return True if the positions coinside, False otherwise.
        """

        return other.getPosition()[0] >= self.getPosition()[0] and other.getPosition()[1] == self.getPosition()[1]