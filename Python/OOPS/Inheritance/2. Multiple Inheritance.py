class Father:
    def Method1(self):
        print("I am father class")
class Mother:
    def Method2(self):
        print("I am mother class")
class Child(Father,Mother):
    def Method3(self):
        print("I am child class")
obj=Child()
obj.Method3()
obj.Method1()
obj.Method2()
print(Child.__mro__)