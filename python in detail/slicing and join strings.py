"""
it's about how to extract parts of a string--- slicing,
or create a longer string by joining two or more strings together. 
"""

text = "Hello, World!"

print(text[0:5]) #'Hello' (characters from index 0 to 4)
print(text[:5]) #'Hello' (Omitting start assumes 0)
print(text[7:]) #from index 7 to the end. 
print(text[::2]) #every second character. 
print(text[::-1]) # reversing a string.

print("\n")

#Joining Strings. 
#join() method is used to concatenate multiple strings efficiently. 

words = ["Hello", "World", "Python"]
sentence = " ".join(words) #joins words together.
print(sentence) 

#joining characters. 

chars = ['P', 'y', 't', 'h', 'o', 'n']
print("".join(chars))

print("hello" + " " + "world!")
print("\n")

greetings = ["Hello", "World"]
print(" ".join(greetings))

name = "Alex"
print("Hello, " + name + "!") 

## slicing and joining strings. 

phoneNum = '0177964653'

areaCode = "(" + phoneNum[:3] + ")"

