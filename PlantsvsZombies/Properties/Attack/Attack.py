'''
Module that handles attack

@author Sofia Louisy
@company Stickybit AB
'''

class Attack:
    def __init__(self):
        self.damage = 10
    
    def attack(self, other):
        '''
        Target looses health

        :param other the target as an Actor object
        :return True if attack, False if charging
        '''
        other.Health.looseHealth(self.damage)