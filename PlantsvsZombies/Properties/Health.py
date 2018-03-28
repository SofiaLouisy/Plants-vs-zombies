"""
Module for health property

@author Sofia Louisy
@company Stickybit AB
"""

class Health:
    def __init__(self):
        self.hitpoints = 100
    
    def looseHealth(self, damage):
        """
        Decreases the health

        :param damage, the decrease amount
        :return hitpoints, the current health
        """
        self.hitpoints -= damage
        return self.hitpoints

    