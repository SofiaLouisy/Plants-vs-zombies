"""
Zombie module with Actor module as parent. Overrides graphics and adds Attack property. Added functions move and attack

@author Sofia Louisy
@company Stickybit AB
"""

from PlantsvsZombies.Actor.Actor import *
import PlantsvsZombies.Properties

class Zombie(Actor):
    def __init__(self):
        Actor.__init__(self)
        self.Movement = Properties.Movement()
        self.Attack = Properties.ChargedAttack()
        self.grfx = "/home/sofia/python/PlantsvsZombies/PlantsvsZombies/Actor/Zombie/rsz_ozzy.gif"
    
    def move(self):
        """
        Moves the zombie horizontally from right to left

        :return (x,y) new position as a tuple
        """
        self.grfx = "/home/sofia/python/PlantsvsZombies/PlantsvsZombies/Actor/Zombie/rsz_ozzy.gif"
        self.Position.x -= self.Movement.move()
        return self.Position.x,self.Position.y
    
    def attack(self,other):
        """
        Tries to attack target. Changes graphics accordingly
        """
        if(self.Attack.attack(other)):
            self.grfx = "/home/sofia/python/PlantsvsZombies/PlantsvsZombies/Actor/Zombie/rsz_ozzy_tilt.gif"
        else:
            self.grfx = "/home/sofia/python/PlantsvsZombies/PlantsvsZombies/Actor/Zombie/rsz_ozzy_halvtilt.gif"