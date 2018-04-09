from PlantsvsZombies.Actor.Zombie.Zombie import Zombie
#from Actor.ActorProperties.Position import Position
zombie = Zombie()
print("zombie position: " + str(zombie.getPosition()))
print("zombie moved position: " + str(zombie.move()))
#print(Position())
import PlantsvsZombies.Properties as Properties
position = Properties.Position()
print(position)
from PlantsvsZombies.Actor.Plant.Plant import *
print(Plant())

import PlantsvsZombies.Actor as Actor
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

from PlantsvsZombies.Object.Projectile.Pea.Pea import Pea as Pea
pea = Pea()
pea.Position.setPosition((0,0))
print(plant.getPosition())
attackPea = plant.getAttack()
#print(attackPea.getPosition())


from PlantsvsZombies.AdventureGames.RunTime import *
runTime = RunTime()
print(runTime)