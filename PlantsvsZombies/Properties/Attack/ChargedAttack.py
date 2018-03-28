'''
Module that handles attack with recharge time. Overrides attack

@author Sofia Louisy
@company Stickybit AB
'''
from PlantsvsZombies.Properties.Attack.Attack import *

class ChargedAttack(Attack):
    def __init__(self):
        self.chargeTime = 4
        self.charging = 0
    
    def attack(self, other):
        '''
        If attack is charged, target looses health

        :param other the target as an Actor object
        :return True if attack, False if charging
        '''
        if(not self.charging):
            other.Health.looseHealth(self.damage)
            self.charging = self.chargeTime
            return True
        else:
            self.charging -= 1
            return False