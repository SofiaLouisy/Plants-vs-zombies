# To do

* Add an attack projectile class that has movement/position and that will attack the zombie when "is blocked"
* A plant can create an attack projectile object when a zombie is on the lane
* Add a pointer that points on the plant in the front of
the lane (so it is clear who to compare "is blocked" to)
* Customize grid so that it fits the board
* Use insertion sort to sort zombies, to know who to be attacked by plant
* exceptions for all methods
* move all properties so that they are not dependent on actor objects (e.i. attack uses other). Move everything actor related to the actor. attack should just return the damage or 0 if charging (can be interpreted as true of false if needed)