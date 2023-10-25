#encap
class bank():
    
    value=100 #private variable

    def yoki(self):
        print("name yoki")
        print("A/c  435627899")
        print("Amt:30000")
        print("place: salem")
        print("\n")
    def varun(self):
        print("name: varun")
        print("A/c 7830e94")
        print("place: salem")
        print("Amt: 40000")
b=bank()
b.yoki()
b.varun()
print(b.value)


#private class encap
class bank:
    def __init__(self):
        self.__value=20 #private variables
    def __gokul(self):
        print("value:",self.__value)
        print("name gokul")
        print("A/c  435627899")
        print("Amt:30000")
        print("place: salem")
        print("\n")
    def __ram(self):
       # self.__ram()
        print("name: ram")
        print("A/c 7830e94")
        print("place: salem")
        print("Amt: 40000")
b=bank()
b._bank__gokul()
b._bank__ram()
#b._bank__value()
print("value:",b._bank__value)
#b.__value()
#b.gokul()
#b.ram()

