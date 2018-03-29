"""
Module FastMovement with module Movement as parent. Overrides the speed.

@author Sofia Louisy
@company Stickybit AB
"""

from PlantsvsZombies.Properties.Movement.Movement import *

class FastMovement(Movement):
    
    def __init__(self):
        Movement.__init__(self)
        self.speed = 5