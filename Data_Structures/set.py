"""Examples of using the set type.
"""

# Creates a list
numbers = [1, 2, 3, 2, 1]
print(numbers)

# Creates a set from numbers list
numbers_set = set(numbers)
print(numbers_set)

# Adding to a set - note 3 does not show twice
numbers_set.add(3)
print(numbers_set)
numbers_set.add(4)
print(numbers_set)

# Removing element from set
numbers_set.add(0)
print(numbers_set)
numbers_set.remove(0)
print(numbers_set)

# Checks if value is present
print(1 in numbers_set)
print(5 in numbers_set)

# Performs similar methods you would use in list
print(min(numbers_set))
print(max(numbers_set))
print(sum(numbers_set))
print(len(numbers_set))

# Makes two sets using range
numbers_1_to_5_set = set(range(1, 6))
numbers_4_to_10_set = set(range(4, 11))
print(numbers_1_to_5_set)
print(numbers_4_to_10_set)

# Uses union to combine the two sets
print(numbers_1_to_5_set | numbers_4_to_10_set)

# Uses intersect to find common values
print(numbers_1_to_5_set & numbers_4_to_10_set)

# Checks first set elements against second and returns unique elements from first
print(numbers_1_to_5_set - numbers_4_to_10_set)
