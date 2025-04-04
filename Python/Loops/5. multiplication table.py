''' Take a positive integer N as input and print the multiplication table of N from 1 to 100.'''
# using for loop
N=int(input("Enter the number: "))
for i in range(1,11):print(N,"x",i,"=",N*i)
print("---------------------------------------------------------------------------")

# using while loop
N=int(input("Enter the number: "))
i=1
while i<=10:
    print(N,"x",i,"=",N*i)
    i+=1
print("---------------------------------------------------------------------------")
