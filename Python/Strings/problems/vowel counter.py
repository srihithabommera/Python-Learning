'''write a program that takes a string input from the user and counts the number of vowels (A,E,I,O,U)
in the string.'''
a="Hello world"
vowels=['A','E','I','O','U','a','e','i','o','u']
count=0
for char in a:
    if char in vowels:
        count+=1
print("Number of Vowels:",count)