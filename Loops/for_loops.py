"""Examples using Python's for loop.
"""

# Basic for loop - prints 1-5
for index in range(1, 6):
    print(index)
print()


def is_prime(number: int) -> bool:
    """Checks if the provided integer is a prime number and returns result as a bool.
    """
    # not a prime if less than 2
    if number < 2:
        return False

    # checks if number is divisible by 2 to number -1
    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    # it's prime
    return True


def sum_up_to_number(number: int) -> int:
    """Adds from 1 up to the number provided and returns the sum.
    """
    the_sum = 0
    for i in range(1, number+1):
        the_sum += i
    return the_sum


def sum_of_divisors(number: int) -> int:
    """Returns the sum of divisors from the number provided.
    """
    the_sum = 0

    if number < 2:
        return the_sum

    # increase the sum by divisor when it divides evenly
    for divisor in range(1, number + 1):
        if number % divisor == 0:
            the_sum += divisor

    return the_sum


def print_number_triangle(number: int) -> None:
    """Prints a line of 1 - number, number times in a triangle pattern.
    """
    number_line = ''
    for i in range(1, number + 1):
        number_line += str(i) + ' '
        print(number_line)


print(is_prime(33))
print(sum_up_to_number(10))
print(sum_of_divisors(6))
print(print_number_triangle(5))
