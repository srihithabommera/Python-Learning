# Print Fibonacci Sequence till 50?
# A Fibonacci Sequence is a series of numbers where each number is the sum 
# of the two numbers that precede it. 0, 1, 1, 2, 3, 5, 8,........

# using while loop.
a=int(input("Enter the Sequence: "))
b,c=0,1
count=0
while count<a:
    d=b+c
    b=c
    c=d
    print(b)
    count+=1
print('---------------------------------------')

# using for loop
e=int(input("Enter the Sequence: "))
f,g=0,1
for i in range(0,e):
    h=f+g
    f=g
    g=h
    print(f)
print('---------------------------------------')