"""A simple menu design.
   User enters 2 numbers then is asked what operation to perform on them.
   Answer is then calculated and output.
"""

# Header
print()
print('----------')
print('Gathers two numbers and performs a mathematical operation on them.')
print("----------")
print()

# Gets user input
first_number = int(input('Enter first number: '))
print()
second_number = int(input('Enter second number: '))
print()

# Prints menu and gets user selection
print('1 - Add')
print('2 - Subtract')
print('3 - Divide')
print('4 - Multiply')
print()
user_selection = input('Choose an operation: ')
print()

# Performs calculation and returns answer
if user_selection == '1':
    # add
    print(f"Result is: {first_number + second_number}")
elif user_selection == '2':
    # subtract
    print(f"Result is: {first_number - second_number}")
elif user_selection == '3':
    # divide
    print(f"Result is: {first_number / second_number}")
    # multiply
elif user_selection == '4':
    print(f"Result is: {first_number * second_number}")
else:
    print("Not a valid response. Run again.")
