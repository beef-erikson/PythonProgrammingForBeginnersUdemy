"""Creates an empty class and instances of that object.
   Fields are then created on the fly.
"""


# Declares an empty class
class Country:
    pass


# Creates new objects from the Country class
canada = Country()
usa = Country()
mexico = Country()

# Create and assign fields to each object
canada.name = 'Canada'
canada.continent = 'North America'
usa.name = 'United States of America'
usa.continent = 'North America'
mexico.name = 'Mexico'
mexico.continent = 'North America'


print(f'{usa.name} is in {usa.continent}.')
