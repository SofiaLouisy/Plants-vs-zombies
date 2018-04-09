"""
Plant module with Actor module as parent. Overrides graphics and adds a function "setPosition"

@author Sofia Louisy
@company Stickybit AB
"""

from PlantsvsZombies.Actor.Actor import Actor
#from PlantsvsZombies.Object.Projectile.Pea.Pea import Pea as Pea
#import PlantsvsZombies.ObjectAttack as ObjectAttack
from PlantsvsZombies.Properties.Attack.ChargedAttack.ObjectAttack.PeaAttack import *
class Plant(Actor):

    def __init__(self):
        Actor.__init__(self)
        self.Position.x = 100
        #grfx
        self.Attack = PeaAttack()
        self.grfx = "PlantsvsZombies/Actor/Plant/rsz_plant.gif"
        self.width = 36
        #self.chargeTime = 100
        #self.charging = self.chargeTime
    
    def setPosition(self,pos):
        """
        Sets the position of the plant

        :param pos the position (x,y) as a tuple
        """
        self.Position.setPosition(pos)
    
    def getAttack(self):
        attack = self.Attack.getAttack(self.getPosition())
        if attack:
            self.grfx = "PlantsvsZombies/Actor/Plant/rsz_plant_rotated.gif"
        elif self.Attack.charging <= self.Attack.chargeTime-10:
            self.grfx = "PlantsvsZombies/Actor/Plant/rsz_plant.gif"
        return attack