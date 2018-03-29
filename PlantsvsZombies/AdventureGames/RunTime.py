"""
Module that keeps track of the runtime in a game, and when
enterings should be made.
"""

class RunTime():
    startUp = 100
    def __init__(self):
        self.endTime = 3000
        self.enterings = set([])
        self.runTime = 0
        self.initiate_enterings()
        self.addWave(self.endTime//2)

    def initiate_enterings(self):
        self.enterings.add(RunTime.startUp)
        self.enterings.add(RunTime.startUp*10)
        self.enterings.add(RunTime.startUp*50)
        current_time = RunTime.startUp*50

        for i in range (2):
            self.enterings.add(current_time +100*i)
        
        print(self.enterings)
        

    def addWave(self,time):
        for i in range(10):
            self.enterings.add(time+i*100)
    
    def run(self):
        """
        runs the time and determined if a zombie should be
        created or not
        """
        self.enterings.discard(self.runTime)
        self.runTime += 1
        
    def isEntering(self):
        """
        Checks if an entering should be done at this time
        :return True if entering should be done, Salse othrewise
        """
        return self.runTime in self.enterings
    
    def isFinished(self):
        """
        Checks if there are no more to be added
        :return bool True is no more to add, false otherwise
        """
        return bool(not len(self.enterings))