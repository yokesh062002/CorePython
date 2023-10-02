num=int(input("enter the value:"))
a=""
if num==1:
    print(num,"is not prime number")
elif num>1:
    for y in range(2,num):
        if(num%y)==0:
            a=""
        break
    if a:
        print(num,"is not prime")
    else:
        print(num,"is prime")