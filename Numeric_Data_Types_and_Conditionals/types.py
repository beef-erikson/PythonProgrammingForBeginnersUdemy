"""Demo of how Python handles types.
"""

number = 5
value = 2.5
is_triggered = True

print(type(number))         # int
print(type(value))          # float
print(type(is_triggered))   # bool
print(type("wheee"))        # str
print(type(6/2))            # float
print(number//value)        # 2.0
print(int(value))           # 2
print(float(number))        # 5.0
