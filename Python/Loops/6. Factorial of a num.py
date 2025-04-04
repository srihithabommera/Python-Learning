'''Take a positive integer N as input and Calculate its factorial(N!).'''
# using for loop
n=int(input("Enter the number: "))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)
print("--------------------------------------")

# using while loop
n=int(input("Enter the number: "))
fact=1
while n!=0:
    fact*=n
    n-=1
print(fact)
print("--------------------------------------")

# by importing math module.
import math
a=int(input("Enter the number: "))
print(f"The factorial of {a} is",math.factorial(5))
print("--------------------------------------")

# using while loop
d=int(input("Enter a number: "))
fact=1
i=0
while i<d:
    i+=1
    fact*=i
print(fact)
print("--------------------------------------")

