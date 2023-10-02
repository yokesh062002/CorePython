def hello():
    print("hello i am yokesh")
hello()
def mani(name,age):
    print(name,age)
mani("yokesh",21)
def sam():
    tamil=int(input("enter the tamil value"))
    hari=int(input("enter the hari value"))
    if tamil==hari:
        print("hari and tamil is equal")
    elif tamil<=hari:
        print(" hari is gotted big value")
    elif tamil>=hari:
        print("tamil is gotted big value")
    else:
        print(" non of there")
sam()

def son():
    for i in range(0,10):
        print(i)
    for x in range(0,100,2):
        print(x)
son()

def yokesh():
    global x,y
    x=20
    y=40
yokesh()
print(x,y)