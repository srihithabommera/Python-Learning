# single Inheritence
class Parent:
    def method1(self):
        print("I'm a Parent")
class Child(Parent):
    def method2(self):
        print("I'm Child")
obj1=Child()
obj1.method1()
obj1.method2()