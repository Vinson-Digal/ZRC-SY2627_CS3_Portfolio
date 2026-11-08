# 1a. What is duck typing, as explained in the video?
# Another way to achieve polymorphism besides inheritance.Object must have the minimum methods/attributes needed."If it walks like a duck and quacks like a duck, it's a duck."
# As long as the object has the minimum necessary methods and
# attributes, Python will accept it.

# 1b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from Animal?

# The Car class only needed the minimum methods and attributes such as speak(), and the alive attribute, so that it could work inside the same loop as Dog and Cat, even if it does not inherit from Animal.

# 3. How does the code in 2.2 demonstrate polymorphism?

# Car, Boat, and Drone are unrelated classes (none inherit from each other), but each has a move() method. The single function start_trip(vehicle) calls vehicle.move() without checking the type of the object. The same call, vehicle.move(), produces a different result depending on the object passed in: the car drives, the boat sails, and the drone flies. Same method name, many forms. That is polymorphism, achieved through duck typing instead of inheritance.

class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()

car = Car()
boat = Boat()
drone = Drone()

start_trip(car)
start_trip(boat)
start_trip(drone)
