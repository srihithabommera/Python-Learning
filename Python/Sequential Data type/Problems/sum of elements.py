# Find the sum of all elements in a given list of numbers.
a=[10,20,30,40,50]
print("----------------------------------------------")
# Printing output directly by using sum keyword.
print("sum of elements =",sum(a))
print("----------------------------------------------")
# printing using for loop.
sum=0
for i in a:
    sum+=i
print(sum)
print("----------------------------------------------")
# printing using while loop.
a=[10,20,30,40,50]
i=0
sum=0
length=len(a)
while i<length:
    #print(length)
    sum+=a[i]
    i+=1
print(sum)
print("----------------------------------------------")
