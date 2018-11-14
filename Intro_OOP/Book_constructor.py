"""Defines the class Book and create some objects.
"""


# Create a class with a name field
class Book:
    def __init__(self, name: str):
        self.name = name


# Creates new objects and assigns the name field
it = Book('IT')
liseys_story = Book("Lisey's Story")
moby_dick = Book('Moby Dick')

# Prints names
print(it.name)
print(liseys_story.name)
print(moby_dick.name)
