from PlantsvsZombies.Object.Projectile.Projectile import *

class Pea(Projectile):
    
    @staticmethod
    def getInstance():
        return __class__()
        
    def __init__(self):
        Projectile.__init__(self)
        self.grfx = "/home/sofia/python/PlantsvsZombies/PlantsvsZombies/Object/Projectile/Pea/rsz_dove.gif"

    def attack(self,other):
        Projectile.attack(self,other)
        self.dying = True
    
    def isDead(self):
        self.grfx = "/home/sofia/python/PlantsvsZombies/PlantsvsZombies/Object/Projectile/Pea/rsz_blood.gif"
        return myObject.isDead(self)