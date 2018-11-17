"""Examples using the decimal and math modules.
"""

import math
from decimal import Decimal

# This outputs 1.29999999
value1 = 4.5
value2 = 3.2
print(value1 - value2)

# Proper way to handle decimal operations - outputs 1.3
value1 = Decimal('4.5')
value2 = Decimal('3.2')
print(value1 - value2)

# Example of math module functions. Both print 3
print(math.ceil(2.2))
print(math.floor(3.7))
