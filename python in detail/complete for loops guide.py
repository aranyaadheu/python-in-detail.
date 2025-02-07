#for loops, range() func, nested for loops with if statements. 
#fixed cmn errs in for loops. 
"""
for loops vs. while loops
both can be nested. Imp difference between this two types of loops:
- while loops are used when a segment of a code needs to execute repeteatedly while a condition is true. 
- for loops iterate over a sequence of elements, executing the body of the loop for each element in the sequence. 

"""

'''for variable in sequence:
    body of loop '''

### common for loop structures. 
'''
A for loop is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code multiple times.

'''

#using for loop with Lists. 

numbers = [1, 2, 3, 4, 5, 6, 7]
for num in numbers:
    print(num)

print("\n")

#using for Loop with Strings. 

text = "Python"
for char in text:
    print(char)

print("\n")

#using for Loop with Tuples. 

colors = ("red", "green", "blue")
for color in colors:
    print(color)

print("\n")

#using for loop with dictionaries. 

student_scores = {"Alex":90, "Hormozie":85, "Charlie":78}
for key in student_scores:
    print(key, student_scores[key])
# or using .items()
print("\n")
for name, score in student_scores.items():
    print(name, score)
print("\n")

#using range() in for Loops
#simple range(n)

for i in range(5):
    print(i)
#specifying Start and Stop
for i in range(1,6):
    print("\n", i)
#using step in range()

for i in range(1,10,2):
    print(i)

#Nested for Loops.

for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
print("\n")

#using for Loops with else. 

for num in range(3):
    print(num)
else:
    print("Loop Completed!")
print("\n")

#break and continue in for Loops
#using break to exit a Loop early---

for num in range(10):
    if num == 5: # Loop stops when num == 5
        break
    print(num)
print('\n')

#using continue to skip an iteration

for num in range(5):
    if num == 2: # skips when num == 2
        continue
    print(num)
print('\n')

#List Comprehension: A shorter for Loop

SQ = [x ** 2 for x in range(1,6)]
print(SQ)

#practical example: finding even numbers. 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)


