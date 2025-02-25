'''
A tuple in Python is like a list, 
but it cannot be changed (immutable).
Tuple = Fixed List (Once created, you can’t change it.)
List = Flexible (You can add, remove, or modify items.)
'''

#defining a Tuple. 
#Use parentheses () instead of square brackets [].

DIMENSIONS = (200, 50)

for DIMENSION in DIMENSIONS:
    print(DIMENSION)

print()

print(DIMENSIONS[0])
print(DIMENSIONS[1])

#writing over a Tuple. 

print("Original dimensions:")
for DIMENSION in DIMENSIONS:
    print(DIMENSION)

DIMENSIONS = (400, 100) # reassigning a variable is valid. 
print("\nModified dimensions:")
for DIMENSION in DIMENSIONS:
    print(DIMENSION)

'''
When compared with lists, tuples are simple data structures. 
'''

#problem(4-13) Buffet. 

items = ('cakes', 'steak', 'soup', 'pastries', 'ice cream')
print("The restaurent offers mostly this items in buffet:")
for item in items:
    print(item.title())

items = ('rice', 'lentils', 'steak', 'ribeye steak')
print("\nThe updated items are:")
for item in items:
    print(item.title())


