"""Fan class design.
"""


class Fan:
    def __init__(self, make: str, radius: float, color: str):
        """Initialization.
        """
        self.make = make
        self.radius = radius
        self.color = color
        self.speed = 0
        self.is_on = False

    def __repr__(self) -> repr:
        """Representation for output when calling object.
        """
        return repr((self.make, self.radius, self.color, self.speed, self.is_on))

    def switch_on(self) -> None:
        """Sets is_on to true and sets starting speed of fan.
        """
        self.is_on = True
        self.speed = 3

    def switch_off(self) -> None:
        """Sets is_on to False and sets speed to 0.
        """
        self.is_on = False
        self.speed = 0

    def increase_speed(self):
        """Increases speed by 1.
        """
        self.speed += 1

    def decrease_speed(self):
        """Decreases speed by 1.
        """
        self.speed -= 1


# Creates object and uses the various class methods.
fan = Fan('Manufacturer', 12, 'Black')
print(fan)

fan.switch_on()
print(fan)
fan.switch_off()
print(fan)
fan.switch_on()

fan.increase_speed()
print(fan)
fan.decrease_speed()
fan.decrease_speed()
print(fan)
