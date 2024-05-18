def log(val):
    print("----")
    print("--"+ str(val) +"--")
    print("----")
log(9)


def log(val):
    val=str(val)
    len_val=len(val)
    prefix="--"+"-"*len_val+"--"
    print(prefix)
    print("-" + str(val) + "-")
    print(prefix)
log(120)

def log(val,decor):
    val=str(val)
    len_val=len(val)
    prefix=decor*2+decor*len_val+decor*2
    print(prefix)
    print(decor+" "+str(val)+" "+decor)
    print(prefix)
log(120,"%")


def log(*values,decor="-",end="/n",padding=2):
    for val in values:
        val=str(val)
        len_val=len(val)
        prefix=decor*padding+decor*len_val+decor*padding
        output=decor*(padding-1)+" "+str(val)+" "+decor*(padding-1)
        print(prefix)
        print(output)
        print(prefix,end=end)
log(120,decor="^",padding=4)

def log(*values,decor="-",**kwargs):
    if "padding" not in kwargs:
        kwargs["padding"]=2

        kwargs.setdefault("padding",2)
        kwargs.setdefault("end","/n")
    for val in values:
        val=str(val)
        len_val=len(val)
        prefix=decor*kwargs["padding"]+decor*len_val+decor*kwargs["padding"]
        output=decor*(kwargs["padding"]-1)+" "+str(val)+" "+decor*(kwargs["padding"]-1)
        print(prefix)
        print(output)
        print(prefix,end=kwargs["end"])
log(10, decor="0")


def root(num):
    num_root=pow(num,0.5)
    return num_root
root_25=root(25)
print(root_25)

lroot=lambda num: pow(num,0.5)
print(lroot(25))





