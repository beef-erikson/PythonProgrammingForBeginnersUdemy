"""Example of using the statistics module.
"""

import statistics

marks = [1, 6, 9, 23, 2]

# Print mean
print(statistics.mean(marks))

# Print median values
print(statistics.median(marks))
print(statistics.median_high(marks))
print(statistics.median_low(marks))
