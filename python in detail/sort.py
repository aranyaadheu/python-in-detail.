# sorting a List Permanently with the sort() Method. 

cars = ['bmw', 'supra', 'audi', 'toyota', 'hyundai']
cars.sort()
print(cars)

# can run it also in reverse by putting reverse= True.

cars.sort(reverse=True)
print(cars)
print("\n")
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# printing a list in reverse order. 
# finding the length of a list. 
cars = ['toyota', 'bmw', 'supra', 'hyundai']
len(cars)

#Avoiding Index Errors when working with Lists.

motorcycles = ['honda', 'yamaha', 'suzuki', 'royal enfield']
print(motorcycles[-1])

#the index -1 always returns the last item in a list. 
#working with Lists. 

'''
Looping through an entire List. 
'''
magicians = ['alice', 'david', 'alex']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your nex trick, {magician.title()}.\n")

#doing something after a for loop. 

print("Thank you, everyone. That was a great magic show!")
print("\n")

animals = ['Lion', 'Tiger', 'Crocodile', 'Dog']
for animal in animals:
    print(animal)
print()

for animal in animals:
    print(f"A {animal.lower()} would make a great pet.")
print("\nAny of these animals would make a great pet")

