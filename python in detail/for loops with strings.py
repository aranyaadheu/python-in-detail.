'''
every for loop can also be written as a while loop. 

'''

greeting = "Hello"
for c in greeting:
    print("The next character is:", c)

print("\n")
'''
notice that the for loop will stop iterating after the "o" is printed.
You can also use for loops with Python's range() function to generate a series of numbers, which you can see in the following example. 

'''

for i in range(0, 6):
    print("The next value is:", i)
print("\n")
"""
can use for loops with strings to perform tasks and functions such as: Reading text from a file, 
searching for a value or specific data in a document or spreadsheet. 
"""

### Looping over a String. 
# for Loop
#The most direct--and common--way to loop over a string is to use the for loop.

greeting = 'Hello'
for char in greeting:
    print(char)

print("\n")
'''
If i want the position of the string then i can use len() function to get that. 
len(greeting) is an integer that tells Python how many characters are in the string. 
But because it's an integer, you need to convert it to an iterable sequence
by using the range() function

'''
for i in range(len(greeting)):
    print(i)

print("\n")

###While loop with indexing. 

greeting = "Hello"
index = 0
while index < len(greeting):
    print(greeting[index])
    index += 1

print("\n")

### While loop with slicing. 

greeting = 'Hello'
index = 0
while index < len(greeting):
    print(greeting[index:index+1])
    index += 1

print("\n")

### List comprehensions. 

numbers = [1, 2, 3, 4, 5, 6]
SQ_NUM = [ x ** 2 for x in numbers]

print(SQ_NUM)

print("\n")

### additional advanced string loop techniques. 
## map() function. 

def square(x):
    return x*x

    