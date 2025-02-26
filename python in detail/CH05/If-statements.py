# can apply conditions in a programm. 
#simple example. 

cars = ['audi', 'bmw', 'nissan', 'toyota', 'tesla']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title()) #title case. 

# Conditional Tests.
# Checking for equality. 
car = 'bmw'
car == 'bmw' # (==)equality operator.
print()
# inequality operator (!=) 

requested_cake = 'vanilla'
if requested_cake != 'strawberry':
    print("Hold the strawberries!")
print()
# numerical comparisons. 

answer = 17
if answer != 47:
    print("That is not the correct answer. Please try again!")

age = 19
age < 21