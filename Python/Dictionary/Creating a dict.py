# By using {}
# By using dict()
# By using :
# BY using fromkeys()
# By using zip()

a={}
print(type(a))
print('-----------------------------------------')

a=dict()
print(type(a))
print('-----------------------------------------')

a={1:"srihitha",2:"pavithra"}
print(type(a))
print('-----------------------------------------')

a={"name","age"}
c=12
b=dict.fromkeys(a,c)
print(b)
print('-----------------------------------------')

a={'name','fullname'}
b=['srihitha']
c=dict(zip(a,b))
print(c)