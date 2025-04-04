'''write a program that makes three numbers as input and finds the largesr among them using decision
making statements.'''
a=int(input("Enter the numbers: "))
b=int(input("Enter the numbers: "))
c=int(input("Enter the numbers: "))
if a>b and a>c:print(a,"is largest number.")
elif b>a and b>c:print(b,"is largets number.")
else:print(c,"is largest")