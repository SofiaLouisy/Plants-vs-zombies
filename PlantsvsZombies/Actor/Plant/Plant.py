"""
Plant module with Actor module as parent. Overrides graphics and adds a function "setPosition"

@author Sofia Louisy
@company Stickybit AB
"""

from PlantsvsZombies.Actor.Actor import Actor

class Plant(Actor):
    def __init__(self):
        Actor.__init__(self)

        self.Position.x = 100
        #grfx
        self.grfx = "/home/sofia/python/PlantsvsZombies/PlantsvsZombies/Actor/Plant/rsz_plant.gif"
        self.width = 36
    
    def setPosition(self,pos):
        """
        Sets the position of the plant

        :param pos the position (x,y) as a tuple
        """
        self.Position.setPosition(pos)