"""Defines the class MotorBike and create some objects.
"""


# Creates an empty class
class MotorBike:
    pass


# Make new objects
honda = MotorBike()
bmw = MotorBike()

# Set speed field to each object
honda.speed = 50
bmw.speed = 80

# Print object
print(honda)
print(bmw)
print()

# Print object speed
print(honda.speed)
print(bmw.speed)
print()

# Note honda changes but not bmw
honda.speed = 55
print(honda.speed)
print(bmw.speed)
