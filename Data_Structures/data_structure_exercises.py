"""Simple examples using the various data structures.
"""

# Creates list
squares_first_ten_numbers = [i*i for i in range(1, 11)]
print(squares_first_ten_numbers)

# Creates set
squares_first_ten_numbers_set = {i*i for i in range(1, 11)}
print(squares_first_ten_numbers_set)

# Creates dict
squares_first_ten_numbers_dict = {i: i*i for i in range(1, 11)}
print(squares_first_ten_numbers_dict)
