"""
Module for position. Uses Board module to initiate position

@author Sofia Louisy
@company Stickybit AB
"""

from PlantsvsZombies.Board.Board import *

class Position:
    def __init__(self):
        self.x = Board.width+35
        self.y = Board.height//2
    
    def __lt__(self,other):
        return self.x < other.x
    def __le__(self,other):
        return self.x <= other.x
    def __eq__(self,other):
        return self.x == other.x and self.y == self.y
    def __ne__(self,other):
        return self.x != other.x and self.y != self.y
    def __gt__(self,other):
        return self.x > other.x
    def __ge__(self,other):
        return self.x >= other.x
    def setPosition(self,pos):
        """
        Sets the position

        :param position tuple
        """
        self.x = pos[0]
        self.y = pos[1]