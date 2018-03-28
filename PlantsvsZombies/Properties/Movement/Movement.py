"""
Module for movement.

@author Sofia Louisy
@company Stickybit AB
"""

class Movement:
    def __init__(self):
        self.speed = 5
    
    def move(self):
        """
        Returns the nr of pixles to be moved

        :return speed The speed
        """
        return self.speed