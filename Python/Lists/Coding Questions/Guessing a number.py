''' Create a list in range 1 to 10 first the computer picks one number and you 
guess that number then if your guess is correct, you win else you lose?'''

import random
a=[1,2,3,4,5,6,7,8,9,10]
b=random.choice(a)
c=int(input("Guess a Number: "))
print("Let's computer Guess a number: ",b)
if b==c:print("Hurray!!,you Won")
else:print("You lose")
print('---------------------------------------------------------')


'''Create a list of random five numbers then check whether there is duplicated 
number or not if it is there delete it, if sum of all numbers is 
even print maximum of the list else print minimum of the list.'''
a=[1,2,4,5,5]
del a[4]
print(a)
b=sum(a)
print(b)
if b%2==0:print("The maximum number is: ",max(a))
else:print("The minimum number is: ",min(a))
print('---------------------------------------------------------')
