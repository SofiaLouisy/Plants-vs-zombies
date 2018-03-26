from Actor.Zombie.Zombie import Zombie
#from Actor.ActorProperties.Position import Position
zombie = Zombie()
print("zombie position: " + str(zombie.position()))
print("zombie moved position: " + str(zombie.move()))
#print(Position())
import Properties
position = Properties.Position()
print(position)
from Actor.Plant.Plant import *
print(Plant())

import Actor
print(Actor.Zombie())

plant = Actor.Plant()
zombie = Actor.Zombie()
while (not plant.isDead()):
    print("Plant: " + str(plant.Health.hitpoints))
    print("Zombie: " + str(zombie.Health.hitpoints))
    zombie.attack(plant)
print("Plant: " + str(plant.Health.hitpoints))
print("Zombie: " + str(zombie.Health.hitpoints))
print("Plant: " + str(plant.isDead()))

from Object.Object import *
print(Object())