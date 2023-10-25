#error handling try:1
try:
    a=20
    b=0
    c=a/b
    print(c)
except Exception as e:
    print(e)
    print("hello")

#name error
try:
    name=123
    print(name)
except NameError as e:
    print("name error",e)
#value error
try:
    num=int(input("enter the values"))
    print(num)
except ValueError as d:
    print("Value error",d)
    print("yokesh")
#index error
try:
    li=[21,34,56,78,90,23]
    print(li[10])
except IndexError as h:
    print("index error",h)
#Key error
try:
    dd={"name":"yoki","name1":"varun"}
    print(dd["age"])
except KeyError as f:
    print("Key error",f)
#attbution error
try:
    class a:
        pass
    A=()
    a.hello()
except AttributeError as d:
    print("attribute error",d)
#raise error
try:
    a=int(input("enter the values"))
except ValueError as e:
    print("valueerror",e)
    raise KeyError("vallue not found")
else:
    print("value",e)
finally:
    print("thank you")

