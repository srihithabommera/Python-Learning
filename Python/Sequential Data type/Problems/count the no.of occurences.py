# count the no.of occurences of a specific element in a list.
a=[1,2,3,2,1,4,2,5]
count=0
b=[]
c=[]
for i in a:
    if i not in b:b.append(i)
        #print(b)
    else:
        c.append(i)
        count+=1
print(count)
print("-------------------------------")

d=a.count(2)
print(d)
print("-------------------------------") 