"""
Plant module with Actor module as parent. Overrides graphics and adds a function "setPosition"

@author Sofia Louisy
@company Stickybit AB
"""

from PlantsvsZombies.Actor.Actor import Actor
from PlantsvsZombies.Object.Projectile.Pea.Pea import Pea as Pea

class Plant(Actor):
    __bases__ = (Actor,)

    def __init__(self):
        Actor.__init__(self)
        self.Position.x = 100
        #grfx
        self.grfx = "/home/sofia/python/PlantsvsZombies/PlantsvsZombies/Actor/Plant/rsz_plant.gif"
        self.width = 36
        self.chargeTime = 100
        self.charging = self.chargeTime
    
    def setPosition(self,pos):
        """
        Sets the position of the plant

        :param pos the position (x,y) as a tuple
        """
        self.Position.setPosition(pos)
    
    def getAttack(self):
        if not self.charging:
            self.charging = self.chargeTime
            pea = Pea()
            pea.Position.setPosition(self.getPosition())
            self.grfx = "/home/sofia/python/PlantsvsZombies/PlantsvsZombies/Actor/Plant/rsz_plant_rotated.gif"
            return pea
        else:
            self.charging -= 1
            if self.charging <= self.chargeTime-10:
                self.grfx = "/home/sofia/python/PlantsvsZombies/PlantsvsZombies/Actor/Plant/rsz_plant.gif"
            return None