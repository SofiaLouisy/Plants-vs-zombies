from PlantsvsZombies.Properties.Attack.ChargedAttack.ObjectAttack.ObjectAttack import *
from PlantsvsZombies.Object.Projectile.Pea import *

class PeaAttack(ObjectAttack):
    def __init__(self):
        ObjectAttack.__init__(self)
        self.Object = Pea.Pea