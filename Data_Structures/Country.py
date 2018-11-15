"""Example of using lists and classes.
"""
from operator import attrgetter


class Country:
    def __init__(self, name: str, population: int, area: int):
        """Initializations.
        """
        self.name = name
        self.population = population
        self.area = area

    def __repr__(self):
        """Produces custom output when calling self.
        """
        return repr((self.name, self.population, self.area))


# Creates list of countries
countries = [Country('India', 1200, 100),
             Country('China', 1400, 200),
             Country('USA', 120, 300)]

# Prints and slicing
print(countries)
print(countries[0:2])
print(countries[::-1])

# Add country and print
countries.append(Country('Russia', 80, 900))
print(countries)

# Sort countries by name and print
countries.sort(key=attrgetter('name'))
print(countries)

# Find max population
print(max(countries, key=attrgetter('population')))

# Find minimum area
print(min(countries, key=attrgetter('area')))
