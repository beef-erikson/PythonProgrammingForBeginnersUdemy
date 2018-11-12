"""Examples of methods using the string module.
"""

import string

# Prints ascii letters
print()
print(string.ascii_letters)         # a-zA-Z
print(string.ascii_lowercase)       # a-z
print(string.ascii_uppercase)       # A-Z

# Prints digits
print()
print(string.digits)                # 0-9
print(string.hexdigits)             # 0-9a-fA-F
print(string.octdigits)             # 0-7

# Misc
print()
print(string.punctuation)           # bunch of punctuation
print(string.whitespace)            # whitespace.

# Reason for use is checking for things. Example:
print()
if 'b' in string.ascii_letters:
    print('Yes!')                   # this triggers
else:
    print('No!')

# Another way to be a little more specific:
if '3' in '13579':
    print('Yes!')                   # this triggers
if '3' not in '13579':
    print('Yes!')                   # this does not trigger
if '3'.isdigit() and '3' in '13579':
    print('Yes!')                   # this triggers
