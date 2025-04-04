class Parents:
    def Method1(self):
        print("I am Parent class")
class Child1(Parents):
    def Method2(self):
        print("I am Srihitha")
class Child2(Parents):
    def Method3(self):
        print("I am Pavithra")
obj1=Child1()
obj1.Method2()
obj1.Method1()
obj2=Child2()
obj2.Method3()
obj2.Method1()
print(Child1.__mro__)