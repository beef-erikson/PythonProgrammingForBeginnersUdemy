"""Dictionary example of counting the number of characters in a string.
"""

# String to parse
string = 'This is a line of stuff. I like coffee, long walks, and campfires.'

# Makes an empty dict
character_occurrences = {}

# Goes through string and and assigns each character as key, value as number of occurrences
for char in string:
    character_occurrences[char] = character_occurrences.get(char, 0) + 1

print(character_occurrences)
