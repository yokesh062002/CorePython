a={"name":"yoki","age":21,"native":"salem"}
print(a)
print(type(a))

#dic item
a={"name":"yoki","age":21,"native":"salem"}
a.items()
print(a)

#copy dic
a={"name":"pp","age":25,"hobby":"chat","frnds":["kumar","raja","sam"]}
print(a)

#key name:
for i in a:
    print(i)
#values:
for i in a:
    print(a[i])

#using valuese:
for i in a.values():
    print(i)
for i in a.keys():
    print(i)
for i,j in a.items():
    print(i,j)

#print set of keys
a={"name":"yoki","age":21,"native":"salem"}
print(a)
print(a["name"])

a={"name":"yoki","age":21,"native":"salem","frnd":["yoki","mohan","jaga"]}
print(a)
print(a["frnd"])
b=a["native"]
print(b)
#get
b=a.get("name")
print(b)
#key
b=a.keys()
print(b)
a["bike"]="ns200"
print(a)
b=a.values()
print(b)
a["car"]="tata"
print(b)
b=a.keys()
print(b)

#change the value 
a={"name":"yoki","age":21,"native":"salem","frnd":["sam","yoki","mohan"]}
print(a)
a["age"]=22
print(a)
#update dic
a.update({"name":"yokesh"})
print(a)

#basic dic
a={"name":"yoki","age":21,"native":"salem"}
print(a)
print(len(a))
print(type(a))

#pop dict
a={"name":"yoki","age":21,"native":"salem"}
a.popitem()
print(a)
# set default
b=a.setdefault("frnds","yoki")
print(b)
#update
a.update({"bike":"ns200"})
print(a)
#value
b=a.values()
print(b)
b=a.values()
a["car"]="tata"
print(a)

#loop dic
a={"name":"yoki","age":21,"native":"salem"}
print(a)
for i in a:
    print(i)

for i in a:
    print(a[i])

for i in a.values():
    print(i)

for i in a.keys():
    print(i)

for i,j in a.items():
    print(i,j)  