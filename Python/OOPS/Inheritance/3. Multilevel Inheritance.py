class GrandParents:
    def Method1(self):
        print("I am GrandParent class")
class Parents(GrandParents):
    def Method1(self):
        print("I am Parents class")
class Child(Parents):
    def Method3(self):
        print("I am child class")
obj=Child()
obj.Method3()
obj.Method1()
print(Child.__mro__)