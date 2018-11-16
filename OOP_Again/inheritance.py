"""Example using class inheritance.
"""


class Animal:
    def bark(self) -> None:
        print('Bark')


class Pet(Animal):
    def groom(self) -> None:
        print('Groom')


# Creates a Pet which inherits properties from Animal
pet = Pet()
pet.bark()
pet.groom()
