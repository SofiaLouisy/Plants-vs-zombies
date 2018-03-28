from PlantsvsZombies.Object.Object import *

class Projectile(myObject):
    def __init__(self):
        myObject.__init__(self)
        self.Movement = Properties.FastMovement()
        self.Attack = Properties.Attack()
    
    def move(self):
        """
        Moves the projectile horizontally from left to right

        :return (x,y) new position as a tuple
        """
        self.Position.x += self.Movement.move()
        return self.Position.x,self.Position.y

    def isColliding(self,other):
        """
        Checks if the object collides with an Actor

        :param other the Actor
        :return True if the positions coinside, False otherwise.
        """
        return other.getPosition()[0] <= self.getPosition()[0] and other.getPosition()[1] == self.getPosition()[1]

    def attack(self,other):
        """
        Attacks target.
        """
        damage = self.Attack.attack()
        other.Health.looseHealth(damage)