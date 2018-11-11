"""Creates a definition for a multiplication table
"""


def print_multiplication_table(number_to_multiply: int, start: int, end: int) -> None:
    """Creates a multiplication table based on number and a start/end point
    """
    for index in range(start, end + 1):
        print(f"{number_to_multiply} * {index} = {number_to_multiply * index}")


print_multiplication_table(6, 34, 39)
