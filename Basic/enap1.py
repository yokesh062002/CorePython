class Deal:
    __seller=""
    __buyer=""
    __value=""
    def __init__(self,s="",b="",v=0):
        print("Deal called")
        self.__seller=s
        self.__buyer=b
        self.__value=v
    def __str__(self):
        return self.__seller+" "+self.__buyer+" "+str(self.__value)+"\n"
    def setseller(self,sel):
        self.__seller=sel
    def getseller(self):
        return self.__seller
    def setbuyer(self,buy):
        self.__buyer=buy
    def getbuyer(self):
        return self.__buyer
    def setvalue(self,val):
        self.__value=val
    def getvalue(self):
        return self.__value
d1=Deal()
d1.setseller("varun")
d1.setbuyer("gokul")
d1.setvalue(2345671)
print(d1.getseller(),d1.getbuyer(),d1.getvalue())
d2=Deal("yoki","varun",40000)
print(d2)
d3=Deal(s="jaga",b="mohan")
d3.setvalue(200000)
print(d3)