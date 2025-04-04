class GrandParents:
    def Method1(self):
        print("I am Grandparents class")
class Parent1(GrandParents):
    def Method2(self):
        print("I am Parent1 class")
class Parent2:
    def Method3(self):
        print("I am Parent2 class")
class Child(Parent2,Parent1):
    def Method4(self):
        print("I am child class")
obj=Child()
obj.Method4()
obj.Method3()
obj.Method2()
obj.Method1()
print(Child.__mro__)