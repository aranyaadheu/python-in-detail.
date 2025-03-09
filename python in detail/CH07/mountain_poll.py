# Filling a Dictionary with user input.

responses = {}

polling_active = True

while polling_active:
    # Prompt for the person's name and response. 
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

# Store the response in the Dictionary. 
responses[name] = response

# Find out if anyone else is going to take the poll.
repeat = input("Would you like to let another person respond? (yes/ no) ")
if repeat == 'no':
    polling_active = False

# Polling is Complete. Show the results. 
print("\n--- Poll results ---")
for name, response in responses.items():
    print(f"{name} would you like to climb {response}.")
