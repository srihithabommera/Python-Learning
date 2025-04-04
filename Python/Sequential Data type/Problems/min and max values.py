# Find the max and min values in a list of numbers.
a=[15,2,7,25,10]
print("The minimum value is ",min(a))
print("The maximum vaalue is",max(a))
print("----------------------------------------------")
# using for loop
max=a[0]
min=a[0]
for i in a:
    if i>max:
        max=i
    if i<min:
        min=i
print("The maximum value is",max)
print("The minimum value is",min)
print("----------------------------------------------")
b=sorted(a)
print(b[0])
print(b[-1])