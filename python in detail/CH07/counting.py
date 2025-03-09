# Using continue in a Loop
# prints odd numbers in a range. 

current_number = 0
while current_number < 100:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)