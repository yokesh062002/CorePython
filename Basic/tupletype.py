#tuple method
a=(1,2,3,4,5,6,7,5,8,5,0,2,5,)
r=a.count(5)
print(r)

#tuple index
b=(1,2,3,4,5,6,7,8,9,0)
c=b.index(6)
print(c)

#append method
g=("yoki","mohan","jagathish","deepa")
h=list(g)
h.append("kanmani")
g=tuple(h)
print(g)

#tuple to tuple
x=("apple","cat","egg")
y=("ball",)
x += y
print(x)

#tuple convat in list
a=("yoki","mohan","jaga","deepa")
b=list(a)
b[1]="star"
a=tuple(b)
print(a)

#tuple loop
a=("dog","cat","rat")
for i in a:
    print(i)

# loop range
b=("bag","pen","pencil","shoe")
for i in range(len(b)):
    print(b[i])

# while loop in tuple
c=("ravi","ram","son","hari")
i=0
while i<len(c):    
    print(c[i])
    i=i+1

#tuple remove
a=("ak","bk","ck","dk")
b=list(a)
b.remove("ck")
a=tuple(b)
print(a)

# join tuple in using + operater
a=("ravi","dog","tom",)
b=("monkey",)
c=a+b
print(c)

#*operater
a=("ak","bk","ck","dk")
b=a*3
print(b)

#tuple count
a=(1,2,3,4,5,6,7,8,1,9,0,1)
b=a.count(1)
print(b)

#index tuple
a=(1,2,3,4,5,6,7)
d=a.index(5)
print(d)