from abc import ABC, abstractmethod

"""Example of creating and using an abstract class.
"""


class AbstractAnimal(ABC):
    """Abstract class method bark.
    """
    @abstractmethod
    def bark(self): pass


class Dog(AbstractAnimal):
    """Defines the bark method from AbstractAnimal.
    """
    def bark(self) -> None:
        print('woof')


dog = Dog()
dog.bark()
