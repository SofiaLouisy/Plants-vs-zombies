from PlantsvsZombies.Object.Object import *
import PlantsvsZombies.Properties as Properties

class ObjectAttack:
    def __init__(self):
        self.Object = myObject
        self.Attack = Properties.ChargedAttack()

    def getAttack(self,position):
        if not self.Attack.charging:
            self.charging = self.Attack.chargeTime
            myObject = self.Object.getInstance()
            myObject.Position.setPosition(position)
            return myObject
        else:
            self.charging -= 1
            return None