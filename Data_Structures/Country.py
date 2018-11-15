"""Example of using lists and classes.
"""


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
