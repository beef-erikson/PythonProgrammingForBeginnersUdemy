# List of stuff I didn't already know
> Hey, not all of us can be geniuses!

## Easy String Formatting
```python
name = "Beef"
print(f"This is {name}")

# --outputs:
# > This is Beef
```     

## Getting Index Element in Loops
```python
number_list = [1,3,6,5]
for index,number in enumerate(number_list):
    print(f'{index} - {number}')

# -- outputs:
# > 0 - 1
# > 1 - 3
# > 2 - 6
# > 3 - 5
```

## Shorthand If Statement
```python
number = 5
is_even = True if number % 2 == 0 else False
print(is_even)

# Output is False

number = 6
is_even = 'Yes' if number % 2 == 0 else 'No'
print(is_even)

# Output is Yes
```

## Calling Tuple Values By Name
```python
beef = 'Beef', 37, 'Pennsylvania'
name, age, state = beef
print(f'{name} is {age} and resides in {state}.')

# -- outputs:
# > Beef is 37 and resides in Pennsylvania.
```

## Using a Template Method Pattern
[See here](https://github.com/beef-erikson/PythonProgrammingForBeginnersUdemy/blob/master/OOP_Again/recipe.py)

## List and Dictionary Unpacking as Method Arguments
```python
number_list = [1, 2, 3, 4, 5, 6]
example_method(*number_list)
some_dict = {'a': '1', 'b': '2', 'c': '3'}
example_method(*number_list, **some_dict)
```
[See more here](https://github.com/beef-erikson/PythonProgrammingForBeginnersUdemy/blob/master/Final_Tips/methods_and_arguments.py)
