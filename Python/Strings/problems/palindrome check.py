''' write a program that takes a string input from the user and checks if it is a palindrome or not.
A palindrome is a word, phrase, number, or sequence of characters that reads the same backward as 
forward.'''
a=input("Enter the input: ")
b=(a[::-1])
if a==b:print("It is palindrome.")
else:print("It not a palindrome.")