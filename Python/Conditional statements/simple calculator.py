a=int(input("Enter The First Number: "))
b=int(input("Enter The First Number: "))
c=input("Enter operation: ")
if c=="+":
    print("The addition of two numbers is",a+b)
elif c=="-":
    print("The subtraction of two numbers is",a-b)
elif c=="*":
    print("The multiplication of two numbers is",a*b)
elif c=="/":
    print("The division of two numbers is",a/b)
else:
    print("Enter valid operator")