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
<<<<<<< HEAD
        self.grfx = "PlantsvsZombies/Actor/Zombie/rsz_ozzy.gif"
=======
        self.grfx = "/home/sofia/python/PlantsvsZombies/PlantsvsZombies/Actor/Zombie/rsz_ozzy.gif"
>>>>>>> c00767c5558b09582b51b721624a025824fd94fc
        self.stillHangingOn = 200

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
        damage = self.Attack.attack()
        if(damage): 
            self.grfx = "/home/sofia/python/PlantsvsZombies/PlantsvsZombies/Actor/Zombie/rsz_ozzy_tilt.gif"
            other.Health.looseHealth(damage)
        elif self.Attack.charging <= self.Attack.chargeTime-10:
            self.grfx = "/home/sofia/python/PlantsvsZombies/PlantsvsZombies/Actor/Zombie/rsz_ozzy.gif"
            #self.grfx = "/home/sofia/python/PlantsvsZombies/PlantsvsZombies/Actor/Zombie/rsz_ozzy_halvtilt.gif"
    
    def isDead(self):
        self.grfx =  "/home/sofia/python/PlantsvsZombies/PlantsvsZombies/Actor/Zombie/rsz_dead_ozzy.gif"
        return Actor.isDead(self)