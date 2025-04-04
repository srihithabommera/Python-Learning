# METHOD-OVER LOADING:
class OverLoading:
    def add(self,a,b):
        return a+b
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c
obj=OverLoading()
print(obj.add(1,2,6))