#overloading example
class yoki:
    def ab(self,a):
        print(a)
    def ab(self,a,b):
        print(a+b)
    def ab(self,a,b,c):
        print(a+b+c)
y=yoki()
y.ab(10,20,30)

#single args
class over:
    def load(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        elif a!=None and b!=None:
            return a+b
        else:
            return a
o=over()
print("sam",o.load(10))
print("sam",o.load(10,20))
print("sam",o.load(10,20,30))

#multiple args passing
class multi:
    def ad(self,*args):
        sum=40
        for i in args:
            sum+=i
        print("add values",sum)
m=multi()
m.ad(40.50)
m.ad(40,50,60)
m.ad(30,40,50,60)
m.ad(10,50,40,30,50,70)
m.ad(49,50,76,50,34,56,67)