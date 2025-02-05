### Python range() with More Examples
# Concatenation (series of interconnected things.) of two range() functions using itertools chain() method
# The chain() method is used to print all the values in iterable targets one after another mentioned in its arguments.

from itertools import chain

# using chain method
print("Concatenating the result")
res = chain(range(5), range(10, 20, 2))

for i in res:
    print(i, end=' ')

### Accessing range() with an Index Value

ele = range (10) [0]
print("\nFirst element:", ele)

ele = range(10)[-1]
print("\nLast element:", ele)

ele = range(10)[4]
print("\nFifth element:", ele)

## range() function with List in Python. 

fruits = ['apple', 'banana', 'cherry', 'tomato']

for i in range(len(fruits)):
    print(fruits[i])
