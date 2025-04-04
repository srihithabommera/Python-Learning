# create dictionaries, access values, update values, adn iterate through key-value pairs.
my_dict={'name':'srihitha','age':21,'Native':'Kamareddy'}
#print(my_dict)
a=input("Give name: ")
age=input("Enter age: ")
Native=input("Enter Native: ")
my_dict['a','age','Native']=a,age,Native
print(my_dict)
print("-------------------------------")
for i,j in my_dict.items():
    print(i,j)
print("-------------------------------")
