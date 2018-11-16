"""Examples using tuple.
"""


def create_beef() -> tuple:
    """Returns a tuple of Beef's info.
    """
    return 'Beef', 1981, 'Pennsylvania'


# Makes a beef tuple, assigns each value to a name, and prints
beef = create_beef()
name, year, state = beef
print(beef)
print(f'{name} was born in {year} and resides in {state}.')

# Demonstrates various operations able to be used with tuples
print(len(beef))
print(beef[0])
print(beef[2])

# Creates another tuple
person = 'Beef', 37, 'USA'
name, age, country = person
print(f'{name} is {age} and lives in {country}.')

# Create tuple with one value
x = (0,)
print(type(x))
