#set is the unorder method and not allow the duplicate value
a={"ab","cd","ef","gh","ab"}
print(a)

#set update
a={"x","y","z","a"}
li=["yoki"]
a.update(li)
print(a)

#add set
a={"yokesh","jagathish","deepa"}
print(a)
a.add("mohan")
print(a)

# set default
ss={"name":"raja","clg":"sce","location":"tiruchencode"}
print(ss)
s=ss.setdefault("aa","ss")
print(s)

#remove the set
a={"ak","mohan","hari","raja","jaga"}
a.remove("mohan")
print(a)
a.discard(2)

#pop the set
s={"naveen","gugan","dinesh","yoki"}
s1=s.pop()
print(s1)
print(s)
