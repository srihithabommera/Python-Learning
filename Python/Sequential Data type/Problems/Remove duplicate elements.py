# Remove duplicate elements from a list to create a new list with unique element.
a=[10,20,30,20,40,10,50]
print(set(a))
print("-------------------------------")
# using for loop
b=[]
for i in a:
      if i not in b:b.append(i)
print(set(b))
print("-------------------------------")