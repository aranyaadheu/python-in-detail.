# Making Numerical Lists. 
'''
Lists are ideal for storing sets of numbers.
'''
#using the range() function. 

for value in range(1,5):
    print(value) # to get the number 5, use (1,6)
print()
# using range() to make a list of numbers

numbers = list(range(1,6))
print(numbers)
print()
# skip numbers in a given range. Pass a 3rd value in the python range()

even_nums = list(range(2,11,2))
print(even_nums)
print()

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)
print()

# simple statistics with a List of Numbers.

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits), max(digits), sum(digits))
print()

#List Comprehensions
# a list comprehension combines the for loop and the creation of new elements into one line
# and automatically appends each new element. 

squares = [value**2 for value in range(1, 11)]
print(squares)

#4-3. Counting to twenty.

for num in range(0,21):
    print(num)
print()

odd_num = list(range(0, 21, 3))
print(odd_num)

#4-4. One million. 

num = list(range(1, 1000000))
#print(num) # summing a million. 
print(min(num), max(num), sum(num))
print()

#4-7. Three.  
value = list(range(3, 30))
print(value)
print()

#4-8. Cubes:

cubes = [value**3 for value in range(0,11)]
print(cubes)

'''
working with a part of a List. 
'''
#slicing a list. 

players = ['charles', 'martina', 'micheal', 'florence', 'alex']
print(players[0:3])
print(players[1:4])
print(players[:4])
print()

#looping through a slice. 

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())






















