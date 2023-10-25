class con1:
    def __init__(self):
        print("happiness")
    def hello(self):
        print("sadness")
c1=con1()
c1.hello()

class tamil:
    def __init__(self):
        print("tamil is a playboy")
    def vino(self):
        print("vino is the good boy")
t=tamil()
t.vino()

#constuct
class con:
    def __init__(self,name,age,place):
        print("name",name)
        print("age",age)
        print("place",place)
c=con("yoki",22,"salem")

class D:
    def __init__(self,cname,cage):
        print("name",cname)
        print("age",cage)
d=D("yoki",22)

class ad:
    def __init__(self,place,mail,company):
        self.p=place
        self.m=mail
        self.c=company
        print("place",place)
        print("mail",mail)
        print("company",company)
    def fun(self):
        print("place",self.p)
        print("mail",self.m)
        print("company",self.c)
a=ad("salem","yokesh@gmail.com","hcl")
a.fun()