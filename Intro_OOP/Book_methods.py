"""Defines the class Book and create some objects.
"""


# Create a class with a name field
class Book:
    def __init__(self, name: str, copies: int=0):
        self.name = name
        self.copies = copies

    def increase_copies(self, number_of_copies: int):
        """Increases the number of copies.
        """
        self.copies += number_of_copies

    def decrease_copies(self, number_of_copies: int):
        """Decreases the number of copies.
        """
        self.copies -= number_of_copies


# Creates new objects and assigns the name field
it = Book('IT', 1)
liseys_story = Book("Lisey's Story", 1)
moby_dick = Book('Moby Dick', 1)

# Prints names
print(it.name)
print(liseys_story.name)
print(moby_dick.name)
print()

# Increases and decreases copies
print(f"There are {liseys_story.copies} copies of {liseys_story.name}")
liseys_story.increase_copies(10)
print(f"There are {liseys_story.copies} copies of {liseys_story.name}")
liseys_story.decrease_copies(6)
print(f"There are {liseys_story.copies} copies of {liseys_story.name}")
