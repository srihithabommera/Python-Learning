'''Take a positive integer N as input and print all the even numbers from 1 to N.'''
# using for loop.
N=int(input("Enter the number: "))
for i in range(1,N+1):
    if i%2==0:print(i)
print("---------------------------------------------------------------------------")

# using while loop.
a=int(input("Enter the number: "))
i=1
while i<=a:
    if i%2==0:
        print(i)
    i+=1
print("---------------------------------------------------------------------------")
