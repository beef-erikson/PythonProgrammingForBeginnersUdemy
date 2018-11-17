"""Example of using collections - deque is faster than a standard list.
"""

from collections import deque

# Makes a deque and pops the rightmost and leftmost values
queue = deque(['Zero', 'One', 'Two'])
queue.pop()
queue.popleft()
print(queue)

# Append to right and left of deque
queue.append('Three')
queue.appendleft('Minus One')
print(queue)
