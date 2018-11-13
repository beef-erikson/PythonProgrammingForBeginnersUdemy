"""A simple menu design.
   User enters 2 numbers then is asked what operation to perform on them.
   Answer is then calculated and output, asking for / performing another option until user quits.
"""

# Header
print()
print('----------')
print('Gathers two numbers and performs a mathematical operation on them.')
print('----------')
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
print('5 - Exit')
print()

# Gets user input and processes option
is_running = True
while is_running:
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
    elif user_selection == '4':
        # multiply
        print(f"Result is: {first_number * second_number}")
    elif user_selection == '5':
        # exits
        print('Enjoy your day.')
        is_running = False
    else:
        print("Not a valid response. Run again.")
