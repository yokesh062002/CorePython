#single inher
class bike:
    def gear(self):
        print("5 speed gear box")
class car(bike):
    def benz(self):
        print(" is the classis car")
c=car()
c.benz()
c.gear()

#multilevel inher
class bank:
    def name(self):
        print("canara bank")
class bank1(bank):
    def name1(self):
        print("hdfc bank")
class bank2(bank1):
    def name2(self):
        print("kyc bank")
b=bank2()
b.name()
b.name1()
b.name2()

#multiple inher
class travels:
    def name(self):
        print("kpn travels")
class travels1:
    def name1(self):
        print("kavery travels")
class main(travels1,travels):
    def luxary(self):
        print("enjoy your journey of he happiness")
m=main()
m.name()
m.name1()
m.luxary()

#higher inher
class college:
    def name(self):
        print("college is good")
class clgname(college):
    def name1(self):
        print("sce college")
class clglocation(college):
    def name2(self):
        print("tiruchencode")
class placement(clgname,clglocation,college):
    def name3(self):
        print("bad")
p=placement()
p.name()
p.name1()
p.name2()
p.name3()