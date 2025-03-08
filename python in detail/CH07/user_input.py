'''
The input() function pauses your program and waits for the user to enter
some text. Once Python receives the user’s input, it assigns that input to a
variable to make it convenient for you to work with.
'''
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# Writing clear prompts

name = input("Please enter your name: ")
print(f"\nHello, {name}!")