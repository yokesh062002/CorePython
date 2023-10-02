balance=[200000,19000,3400,100000]

def debit(money=0,pos=0):
    if money<=balance[pos]:
        balance[pos]-=money
        print(money,"debited")
        return balance[pos]
    else:print("can't debit")

hai=debit(10000.0)
print(hai)

def simple(single=0):
    return single*single
yet=simple(20)