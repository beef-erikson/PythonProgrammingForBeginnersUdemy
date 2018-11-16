class LandAnimal:
    def __init__(self):
        """Initialization for LandAnimal.
        """
        super().__init__()
        self.walking_speed = 5

    def increase_walking_speed(self, how_much: int) -> None:
        """Increases walking speed by provided int amount.
        """
        self.walking_speed += how_much


class WaterAnimal:
    def __init__(self):
        """Initialization for WaterAnimal.
        """
        super().__init__()
        self.swimming_speed = 10

    def increase_swimming_speed(self, how_much: int) -> None:
        """Increases swimming speed by provided int amount.
        """
        self.swimming_speed += how_much


class Amphibian(WaterAnimal, LandAnimal):
    """Inherits from both WaterAnimal and LandAnimal"""
    def __init__(self):
        super().__init__()


# Creates a new Amphibian and uses the functionality from its inherited classes
amphibian = Amphibian()
print(amphibian.walking_speed)
print(amphibian.swimming_speed)

amphibian.increase_walking_speed(10)
print(amphibian.walking_speed)

amphibian.increase_swimming_speed(45)
print(amphibian.swimming_speed)
