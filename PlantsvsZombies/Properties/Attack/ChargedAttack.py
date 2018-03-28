'''
Module that handles attack with recharge time. Overrides attack

@author Sofia Louisy
@company Stickybit AB
'''
from PlantsvsZombies.Properties.Attack.Attack import *

class ChargedAttack(Attack):
    def __init__(self):
        Attack.__init__(self)
        self.chargeTime = 4
        self.charging = 0
        self.damage = 10
    
    def attack(self):
        '''
        Returns arrack damage. If charging, returns 0.

        :return True if attack, False if charging
        '''
        if(not self.charging):
            self.charging = self.chargeTime
            return self.damage
        else:
            self.charging -= 1
            return 0