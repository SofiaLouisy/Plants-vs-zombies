"""
Module for a board of fixed size and graphics.

@author Sofia Louisy
@company Stickybit AB
"""

class Board:
    grfx = "/home/sofia/python/PlantsvsZombies/PlantsvsZombies/Board/grass.bmp"
    size = width,height = (1027,770) #image size

    def __init__(self):
        self.lanes = 1
        self.grid = []
        self.sections = 3
        self.constructGrid()
    
    def setLanes(self,nr):
        """
        Sets the number of lanes and constructs a grid accordingly

        :param nr The number of lanes
        """
        self.lanes = nr
        self.constructGrid()
    
    def getLanePositions(self):
        """
        Function for getting vertical position of lanes

        :return a tuple of the vertical lane positions
        """        
        lanePositions = [None]*(self.lanes)
        for i in range (self.lanes):
            lanePositions[i] = (Board.height*(i+1)//(self.lanes*2))
        return tuple(lanePositions)

    def constructGrid(self):
        self.grid = []
        for i in range(self.lanes):
            self.grid.append([True for i in range(self.sections)])
    
    def getPosition(self,row,col):
        """
        Calculates the horizontal and vertical position of a grid position

        :param row the row
        :param col the column
        :return x,y a tuple of the position
        """
        x = Board.width*(col+1)//(self.sections*2)
        #x = Board.width*(1)//(self.sections*2)
        y = Board.height*(row+1)//(self.lanes*2)
        return x,y
    
    def putObject(self,row,col):
        """
        Marks the position of the grid as filled

        :param row the row
        :param col the column
        :return True if position was free, False if position was taken
        """
        if self.grid[row][col]:
            self.grid[row][col] = False
            return True
        else:
            return False

    def removeObject(self,row,col):
        """
        Marks the position of the grid as free

        param row the row
        param col the column
        return True if position has been freed, False if position was already free
        """
        if not self.grid[row][col]:
            self.grid[row][col] = True
            return True
        else:
            return False