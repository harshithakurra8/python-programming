tpl=(4,8,18,48)
tpl=list(tpl)
tpl[0]=9
tpl=tuple(tpl)
print(tpl)


tpl=(4,6,35,82)
print(tpl+(3,56))

tpl=(4,8,5,6)
print(tpl.index(5))

#Add the following list

#lst = [ 12, 15, 18]
#to the tpl

#tpl = ( 3, 6, 9)
#and then print the tpl.

tpl = ( 3, 6, 9)
print(tpl+(12, 15, 18))


tpl = ( 3, 6, 9)
lst = [ 12, 15, 18]
tpl = list(tpl)
tpl.extend(lst)
tpl = tuple(tpl)
print(tpl)
