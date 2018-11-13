"""Examples of using common string methods.
"""

lowercase = 'hello world'
uppercase = 'HELLO WORLD'
titlecase = 'Hello World'
number = '123'

print(lowercase)                    # hello world
print(lowercase.upper())            # HELLO WORLD
print(lowercase.capitalize())       # Hello world
print(lowercase.title())            # Hello World
print(uppercase)                    # HELLO WORLD
print(uppercase.lower())            # hello world
print()

print(lowercase.islower())          # True
print(lowercase.istitle())          # False
print(lowercase.isupper())          # False
print(titlecase.isupper())          # False
print(uppercase.isupper())          # True
print()

print(number.isdigit())             # True
print('123A'.isdigit())             # False
print(number.isalpha())             # False
print()

print(lowercase.endswith('world'))  # True
print(lowercase.endswith('ld'))     # True
print(lowercase.endswith('wo'))     # False
print(lowercase.startswith('hel'))  # True
print(lowercase.startswith('el'))   # False
print()

print(lowercase.find('hello'))      # 0
print(lowercase.find('ello'))       # 1
print(lowercase.find('wor'))        # 6
print(lowercase.find('Ello'))       # -1
