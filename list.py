lst=["milk","bread","egg"]
print(lst[0])

lst=["milk","bread","egg"]
print(lst[1:])

lst=["milk","bread","egg"]
print(lst[-1])

lst=["milk","bread","egg"]
lst[2]="Banana"
print(lst)

lst=["milk","bread","egg"]
lst.remove("bread")
print(lst)

lst=["milk","bread","egg"]
lst.pop(2)
print(lst)

lst=["milk","bread","egg"]
del(lst[1])
print(lst)

lst=["milk","bread","egg"]
lst.append("banana")
print(lst)

lst=["milk","bread","egg"]
lst=lst+["honey"]
print(lst)

lst=["milk","bread","egg"]
lst.extend(["banana","honey","peach"])
print(lst)

lst=[1,6,8,3,5,9]
print(len(lst))

lst=[1,6,8,3,5,9]
print(sum(lst))

lst=[1,6,8,3,5,9]
print(max(lst))

lst=[1,6,8,3,5,9]
print(min(lst))

lst=[1,6,8,3,5,9]
lst.sort()
print(lst)

lst=[1,6,8,3,5,9]
lst.sort(reverse=True)
print(lst)



#Perform the following functions on the given lst list :

#lst = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#Remove the following elements from the list :

#cherry
#melon
#kiwi
#Add guava to the list

#Add peach to the list

#Reverse the list

#Print the list

#Print the length of the list

#lst = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

lst = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
lst.remove("cherry")
lst.pop(4)
lst.remove("kiwi")
lst.append("guava")
lst.append("peach")
lst.sort(reverse=True)
print(lst)