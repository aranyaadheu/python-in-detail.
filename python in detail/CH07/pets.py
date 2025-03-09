# Removing all instances of specific values from a List. 

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
print()

# remove() removes repetitive values from a List. 

foods = ['burger', 'cheese', 'dragonfruit', 'cheese', 'pizza', 'burger']

print(foods)

while 'burger' in foods:
    foods.remove('burger')

print(foods)