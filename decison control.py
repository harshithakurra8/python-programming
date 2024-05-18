mood="😁"

if mood=="😁":
    print("I'm Happyyy")
elif mood=="🥲":
    print("I'm Sad")
else:
    print("I'm fine")


mood="🥲"

if mood!="😁":
    print("I'm not Happyyy")

num=1
if num>0:
    print("number is bigger than zero")

total=input("Total:")
print(type(total))

total=int(input("Total:"))
dicount=0
if total>100:
    discount=10
elif total>50:
    discount=5
    print("Amount:",total-discount)

total=int(input("Total:"))
dicount=0
if total<100 and total>=50:
    discount=5
elif total>100:
    discount=10
    print("Amount:",total-discount)

mood="😁"
if mood=="😁"or mood=="😂":
    print("I'm Happyyy")


lst=["milk","honey"]
if "banana" not in lst:
    print("Need banana")
    lst.append("banana")


num=0
if not num>0:
    print("greater than 0")


num=10.1878
num=int(num) if num.is_integer()else num
print(num)
