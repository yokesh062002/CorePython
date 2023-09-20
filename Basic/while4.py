seat=10;
while seat>0:
    amt=int(input("enter the amount"))
    if amt>=120:
        print("you bought",seat,"ticket")
        seat-=1
    else:
        print("insufficent amount to buy ticket")