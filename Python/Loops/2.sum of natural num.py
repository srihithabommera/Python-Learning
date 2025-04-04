''' Take a positive integer N as input and calculate the sum of the first N natural numbers.'''
a=int(input("Enter a number: "))
# using for loop
sum=0
for i in range(1,a+1):
    sum+=i
print(sum)
print("--------------------------------------------")

# using while loop
b=int(input("Enter a number: "))
sum=0
while b!=0:
    b-=1
    sum+=b+1
print(sum)