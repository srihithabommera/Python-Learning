# Print all multiples of 7 from 1 to 100 using while loop?

# using while loop
a=int(input("Enter a Number: "))
i=1
while i<=10:
    b=a*i
    print(a,'x',i,'=',b)
    i+=1
print('---------------------------------------')


#using for loop
b=int(input("Enter a number: "))
for i in range(1,11):
    c=b*i
    print(b,'x',i,'=',c)
print('---------------------------------------')