from PlantsvsZombies.Object.Object import *
from PlantsvsZombies.Properties.Attack.ChargedAttack.ChargedAttack import *

class ObjectAttack(ChargedAttack):
    def __init__(self):
        ChargedAttack.__init__(self)
        self.Object = myObject
        #self.Attack = Attack.ChargedAttack()

    def getAttack(self,position):
        """
        Returns an object if charged.

        :param position The position of the origin
        :return myObject if charged, None otherwise
        """
        if self.attack():
            myObject = self.Object.getInstance()
            myObject.Position.setPosition(position)
            return myObject
        else:
            return None