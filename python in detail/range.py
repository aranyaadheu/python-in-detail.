for n in range (0,11,2):
    print(n)

# python range() function

for i in range(5):
    print(i, end= " ")
    print()

#Syntax of Python range() function
# Syntax: range(start, stop, step)
###Parameter :


### start: [ optional ] start value of the sequence
### stop: next value after the end value of the sequence
### step: [ optional ] integer value, denoting the difference between any two numbers in the sequence
### Return : Returns an object that represents a sequence of numbers//

for i in range (6):
    print(i, end= ' ')
print()

##Python range (start, stop)
## When the user call range() with two arguments, 
# the user gets to decide not only where the series of numbers stops but also where it starts, 
# so the user doesn’t have to start at 0 all the time. 
# Users can use range() to generate a series of numbers from X to Y using range(X, Y).

## Example of Python range (start, stop)

for i in range (5,20):
    print(i, end=' ')
    print()

## Python range (start, stop, step)

# in this example printing the number from 0 to 9 with the jump of 2. 
# printing even numbers. 

for i in range (0, 10, 2):
    print(i, end=' ')
    print()


# Incrementing the Range using a Positive Step.

for i in range (0, 30, 4):
    print(i, end=' ')
    print()

# Python range() using Negative Step
# for decrement

for i in range (25, 2, -2):
    print(i, end=' ')
    print()

# python range() with float values. 
# using a float number. Anything with a point value. 

for i in range (3.3):
    print(i)

### Python range() function doesn’t support float numbers.
#  i.e. user cannot use floating-point or non-integer numbers in any of its arguments. 
# Users can use only integer numbers.

### Python range() with More Examples
# Concatenation of two range() functions using itertools chain() method
# The chain() method is used to print all the values in iterable targets one after another mentioned in its arguments.

from itertools import chain

# using chain method
print("Concatenating the result")
res = chain(range(5), range(10, 20, 2))

for i in res:
    print(i, end=' ')
    