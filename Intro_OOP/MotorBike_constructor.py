"""Defines the class MotorBike and create some objects.
"""


# Creates a class with a speed field
class MotorBike:
    def __init__(self, speed: int):
        self.speed = speed


# Make new objects with speed argument
honda = MotorBike(50)
bmw = MotorBike(80)

# Print object speed
print(honda.speed)
print(bmw.speed)
print()
