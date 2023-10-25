from abc import ABC
class bus(ABC):
    def volvo(self):
        print("hello")
        pass
class kpn(bus):
    def volvo(self):
        print("happy travel")
class str(bus):
    def volvo(self):
        print(" AC bus")
class sat(bus):
    def volvo(self):
        print("good vehicle")
e=bus()
e.volvo()
s=str()
s.volvo()
s1=sat()
s1.volvo()
b=bus()
b.volvo()
