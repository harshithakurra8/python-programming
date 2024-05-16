if 0>1:
    print("0 is bigger than 1")
else:
    print("0 is ofcourse smaller than 1")

contacts={
    "Jack":86587326873,
    "wilbur":29864878,
    "harry":89688287,
    "joe":868653876,
    "lucky":8258267
}
client=input("Search🔍:")
if client in contacts:
    print(client,contacts[client])
else:
    print(client,"Not found!")