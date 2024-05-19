class Resume:
    pass
jake=Resume()
print(jake)

class Resume: 
 def __init__(self):
    print("init called!")
jake=Resume()

class Resume:
    def __init__(self):
        print("self:",self)
jake=Resume()
print("jake:",jake)


class Resume:
    def __init__(self,name,age):
        self.name=name
        self.age=age
jake=Resume(jake,21)
print(jake.age)


jake.is_programmer=True
print(jake.is_programmer)

#Modify the attribute(update)
class Resume:
    def __init__(self,name,age):
        self.name=name
        self.age=age
jake=Resume(jake,21)
jake.age=31
print(jake.age)

#delete the attribute
class Resume:
    def __init__(self,name,age):
        self.name=name
        self.age=age
jake=Resume(jake,21)
del(jake.age)
print(jake.name)

#methods
class Resume:
 def __init__(self,name,age):
    self.name=name
    self.age=age

 def show(my):
    len_name=len(my.name)
    print(" -"+" -"*len_name+" -")
    print(" -"+ my.name +" -")
    print(" -"+" -"*len_name+" -")
jake=Resume("jake",21)
jake.show()



