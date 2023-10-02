def register(name,location,prefix="mr/miss/mrs"):
    if location=="salem":
        print(prefix,name,"has approved in",location)
    elif location=="chennai":
        print(prefix,name," has gone under waiting state since its",location)
    else: print("business not approved")

register("zealous tech crop","salem")
register("annamalai automobile","chennai")
register(" has been completed","sss")