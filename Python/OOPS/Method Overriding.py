# METHOD OVER-RIDING:
class Grandparents:
    def method(self):
        print("This is grandparents class")
class Parent(Grandparents):
    def method(self):
        print("This is parent class")
class Child(Parent):
    def method(self):
        print("This is child class")
obj=Child()
obj.method()
obj=Parent()
obj.method()
print('--------------------------------------')

# another code
class Parent1:
    def method(self):
        print("This is parent1 class")
class Parent2:
    def method(self):
        print("This is parent2 class")
class Child(Parent1,Parent2):
    #def method(self):
        #print("This is parent1 class")
    pass
obj=Child()
obj.method()
# here parent1 class is printed because it follows the MRO method(Method resolution order.)

print('-------------------------------------------------')
# it also over rides the methods by using __init__ method.
class Parent:
    def __init__(self):
        print("This is parent class")
class Child(Parent):
    def __init__(self):
        print("This is Child class")
Child()