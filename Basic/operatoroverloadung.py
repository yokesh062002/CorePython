class operator:
    def __init__(self,a):
        self.a=a
        print(self.a+self.a)
obj=operator(10)
obj1=operator(20)
print("sum",obj.a+obj1.a)


class oper:
    def __init__(self,a):
        self.a=a
    def __add__(self,b):
        return self.a+b.a
o=oper(50)
o1=oper(100)
print("value",o+o1)