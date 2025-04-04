# 1.By using {},  2.By using set(range(start,stop,step)),  3.set() method
print("Method-I")
a={2,3,4,8,3}
print(a)
print(type(a))

# creating an empty set refers to dict.
b={}
print(type(b))
print("-------------------------------")

print("Method-II")
a=set(range(0,10,1))
b={i for i in a}
print(b)
print("-------------------------------")

# using set()
print("Method-III")
a=[1,2,3,7,7,7]
b=set(a)
print(b)
print("-------------------------------")
