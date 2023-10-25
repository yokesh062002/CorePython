class Birds:
    def sound(self):
        print("couckkoo")
    def fly(self):
        print("its can be flying the birds")
class Bird1(Birds):
    def peacock(self):
        print("beautifull")
class Bird2(Birds):
    def crow(self):
        print("it is black colour")
obj1=Birds()
obj2=Bird1()
obj3=Bird2()
obj1.sound()
obj1.fly()
obj2.peacock()
obj3.crow()