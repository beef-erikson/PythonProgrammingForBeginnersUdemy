"""This is an example of using list comprehension to shorten looping logic.
"""

# Creates two lists
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
numbers_length_four = []

# Gets all elements with a length of 4 and prints
for number in numbers:
    if len(number) == 4:
        numbers_length_four.append(number)
print(numbers_length_four)

# Uses list comprehension to set back to numbers and prints
numbers_length_four = [ number for number in numbers ]
print(numbers_length_four)

# Uses list comprehension to print the length of all the elements
numbers_length_four = [ len(number) for number in numbers ]
print(numbers_length_four)

# List comprehension all to upper and prints
numbers_length_four = [ number.upper() for number in numbers ]
print(numbers_length_four)

# Gets all elements with a length of 4 using list comprehension and prints
numbers_length_four = [ number for number in numbers if len(number) == 4 ]
print(numbers_length_four)
