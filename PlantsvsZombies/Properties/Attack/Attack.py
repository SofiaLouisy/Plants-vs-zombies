'''
Module that handles attack

@author Sofia Louisy
@company Stickybit AB
'''

class Attack:
    def __init__(self):
        self.damage = 15
    
    def attack(self):
        '''
        Target looses health

        :return damage the attack damage
        '''
        return self.damage