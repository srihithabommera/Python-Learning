''' Take a positive integer N as input and print all the odd numbers from 1 to N.'''
# using for loop
N=int(input("Enter the number: "))
for i in range(N+1):
    if not(i%2==0):print(i)
print("---------------------------------------------------------------------------")

# using while loop
a=int(input("Enter the number: "))
i=1
while i<=a:
    if not(i%2==0):print(i)
    i+=1
print("---------------------------------------------------------------------------")
