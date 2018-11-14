"""Defines the class Book and create some objects.
"""


# Makes empty class book
class Book:
    pass


# Creates new objects
it = Book()
liseys_story = Book()
moby_dick = Book()

# Assigns name field to each
it.name = 'IT'
liseys_story.name = "Lisey's Story"
moby_dick.name = 'Moby Dick'

# Prints names
print(it.name)
print(liseys_story.name)
print(moby_dick.name)
