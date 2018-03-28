from PlantsvsZombies.Object.Projectile.Projectile import *

class Pea(Projectile):
    def __init__(self):
        Projectile.__init__(self)
        self.grfx = "Object/Projectile/Pea/rsz_ozzy.gif"