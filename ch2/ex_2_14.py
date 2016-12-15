"""
Problem: you wnat to combine small string together into a larger string
"""

parts = ["It's", "beginning", "to", "look", "a", "lot", "like", "Christmas"]
print(' '.join(parts))
print('•'.join(parts))
print('\u2122 '.join(parts))

a = "Go placidly"
b = "amid the noise and haste"
print(a + " " + b)

# IMPORTANT: If joining a lot of strings together, first collect the strings then use join. Successivley adding them together is HORRIBLE on memory


