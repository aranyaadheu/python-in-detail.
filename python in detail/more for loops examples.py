product = 1
for n in range (1,10):
    product = product * n

print(product)

# calling friends using for loop

friends = ['alex', 'khabib', 'marshal']

for friends in friends:
    print("Come here,", friends)

# counting from one to ten. 

for countdown in range (1,10):
    print("Starting", countdown)

# countdown for a rocket launch. 

for number in range (5, 0, -1): # starts from 5, goes down to 1.
    print(number)

print("Rocket lift off!")

# classic example. 

def to_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print(x, to_celsius(x))
    