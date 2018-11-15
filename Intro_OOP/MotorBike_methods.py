"""Defines the class MotorBike and create some objects.
"""


# Creates a class with a speed field
class MotorBike:
    def __init__(self, speed: int):
        """Initializations
        """
        self.speed = speed

    def increase_speed(self, how_much: int):
        """Increases the speed of the object
        """
        self.speed += how_much

    def decrease_speed(self, how_much: int):
        """Decreases the speed of the object
        """
        self.speed -= how_much


# Make new objects with speed argument
honda = MotorBike(50)
bmw = MotorBike(80)

# Print object speed
print(honda.speed)
print(bmw.speed)
print()

# Increase speed
bmw.increase_speed(20)
print(bmw.speed)

# Decrease speed
bmw.decrease_speed(50)
print(bmw.speed)
