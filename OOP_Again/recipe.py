from abc import ABC, abstractmethod

"""Template method pattern example.
"""


class AbstractRecipe(ABC):
    """Abstract class for recipes.
    """
    def execute(self):
        self.prepare()
        self.recipe()
        self.cleanup()

    @abstractmethod
    def prepare(self): pass

    @abstractmethod
    def recipe(self): pass

    @abstractmethod
    def cleanup(self): pass


class StoveRecipe(AbstractRecipe):
    """Defines the necessary methods from the abstract class.
    """
    def prepare(self):
        print('do the dishes')
        print('get raw materials')

    def recipe(self):
        print('execute the steps')

    def cleanup(self): pass


class MicrowaveRecipe(AbstractRecipe):
    """Defines the necessary methods from the abstract class.
    """
    def prepare(self):
        print('do the dishes')
        print('get raw materials')
        print('switch on microwave')

    def recipe(self):
        print('execute the steps')

    def cleanup(self):
        print('switch off microwave')


# Creates and executes each type of class
recipe = StoveRecipe()
recipe.execute()

microwave = MicrowaveRecipe()
microwave.execute()
