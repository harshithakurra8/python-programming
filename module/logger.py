def log(*values,decor="-",**kwargs):
    if "padding" not in kwargs:
        kwargs["padding"]=2

        kwargs.setdefault("padding",2)
        kwargs.setdefault("end")
    for val in values:
        val=str(val)
        len_val=len(val)
        prefix=decor*kwargs["padding"]+decor*len_val+decor*kwargs["padding"]
        output=decor*(kwargs["padding"]-1)+" "+str(val)+" "+decor*(kwargs["padding"]-1)
        print(prefix)
        print(output)
        print(prefix,end=kwargs["end"])
log(10, decor="0")