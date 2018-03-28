from PlantsvsZombies.Object.Object import *

class Projectile(Object):
    def __init__(self):
        Object.__init__(self)
        self.Movement = Properties.FastMovement()
    
    def isColliding(self,other):
        """
        Checks if the object collides with an Actor

        :param other the Actor
        :return True if the positions coinside, False otherwise.
        """
        return other.getPosition()[0] >= self.getPosition()[0] and other.getPosition()[1] == self.getPosition()[1]