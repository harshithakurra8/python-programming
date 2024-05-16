name="Jake"
print(name[0])

name="Jake"
print(name[-1])


email="""How are you?
I'm fine!"""
print(email)



name="John Smith"
print(name[0:10])

name="John Smith"
print(name[5:])

first_name="John"
Last_name="Smith"
print(first_name+" "+Last_name)

print("ha"*8)

first_name="John"
print(len(first_name))

name=input("Name:")
if len(name)>5:
    print("Your name should be less than 5 letters")
else:
    print("Nice name")

name="John"
print(name.upper())

contacts={
    "Jack":86587326873,
    "Wilbur":29864878,
    "Harry":89688287,
    "Joe":868653876,
    "Lucky":8258267
}
client=input("Search🔍:")
client_key=client.capitalize
if client_key in contacts:
    print(client,contacts[client_key])
else:
    print(client,"Not found!")


msg=input(">><<")
if "." in msg:
    print("$%^%#")
else:
    print("not found!")






