# what is for loop?

for x in range (5):
    print(x) 

# basic for loop exmpale. 

friends = ['Suvorno', 'Issac', 'Bara']

for friends in friends:
    print("Hi " + friends)

# certain value in output. 

values = [ 21, 26, 56, 89, 22]

sum = 0
length = 0
for value in values:
    sum += value
    length += 1
print("Total sum: " + str(sum)+ " - Average: " + str(sum/length))