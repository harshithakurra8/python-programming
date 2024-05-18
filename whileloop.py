counter=0
while counter!=3:
    print("start the loop")
    counter=counter+1
    print(counter)
    print("end the loop")


def fire():
   print("....Loading Ammoo....")
rounds=3
while rounds:
   print("🔥")
   rounds=rounds-1
fire()  

def fire(rounds):
    print("....Loading Ammoo....")
    print("....firing....")
    while rounds:
        print("🔥")
rounds-=1
fire(6)



def fire(rounds):
    print("....Loading Ammoo....")
    print("....firing....")
    while rounds:
        if rounds:
            print("🔥")
            rounds-=1
        else:
            print("RELOAD!!!!!")
            break

fire(2)


counter=0
while counter!=4:
    counter+=1

    if (counter%2)!=0:
        continue
    print(counter)
    print("end")





