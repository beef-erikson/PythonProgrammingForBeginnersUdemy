"""Basics of exception handling.
"""

# Note that value i could be user input instead of example here
# Hard-coding 0 just for example
try:
    # ZeroDivisionError exception
    i = 0
    j = 10 / i

    # TypeError exception
    values = [1, '1']
    sum(values)

except TypeError:
    print('TypeError')
    j = 10

except ZeroDivisionError:
    print('Cannot divide by zero')
    j = 0

# Catch-all
except:
    print('Something went horribly wrong.')
    j = 0

# Executed when no exception
else:
    print('Else')

# Will always execute regardless of exception - handle file/resource closing / etc here
finally:
    print('Finally')


print(j)
print('End')
