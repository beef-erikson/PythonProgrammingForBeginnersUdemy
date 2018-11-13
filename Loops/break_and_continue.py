"""Examples of using break and continue in loops.
"""

# Normal loop - prints odd numbers from 1 to 10
for i in range(1, 11, 2):
    print(i, end=' ')
print()


# Examples using break
for i in range(1, 11):
    if i == 5:
        break
    print(i, end=' ')           # prints 1-4 and breaks out of loop
print()

for i in range(1, 11):
    if i % 2 == 0:
        break
    print(i, end=' ')           # prints 1 and breaks out of loop
print()


# Examples using continue
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=' ')           # prints odd numbers from 1 to 10
print()

for i in range(1, 11):
    if i % 2:
        continue
    print(i, end=' ')           # prints even numbers
