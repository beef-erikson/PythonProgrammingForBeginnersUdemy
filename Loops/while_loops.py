"""Examples using while loop.
"""

# Simple example that prints 0-4 on one line
i = 0
while i < 5:
    print(i, end=" ")
    i += 1
print()


def print_squares_up_to_limit(limit: int) -> None:
    """Takes the provided number and prints out all the squares that lead up to that number.
    """
    number = 1
    while number * number < limit:
        print(number * number, end=" ")
        number += 1


def print_cubes_up_to_limit(limit: int) -> None:
    """Takes the provided number and prints out all the cubes that lead up to that number.
    """
    number = 1
    while number * number * number < limit:
        print(number * number * number, end=" ")
        number += 1


print_squares_up_to_limit(35)
print()
print_cubes_up_to_limit(35)
