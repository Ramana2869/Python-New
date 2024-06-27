# list data type

l1 =[32,88.89,"file",True,889,"edit",False,7637,7781,"view"]
print(l1,type(l1))
# append
l1.append("print")
print(l1)
# index
print(l1.index(889))
# insert
l1.insert(6,932)
print(l1)
# reverse
l1.reverse()
print(l1)
# sort
l2 =[12,6,988,24,766,19,757,30,587,30]
l2.sort()
print(l2)
# remove
l2.remove(757)
print(l2)
# pop
l2.pop()
print(l2)
# count
print(l2.count(30))
# clear
l2.clear()
print(l2)
# copy
l3 =l1.copy()
print(l3)
# extend
l4 =[30,848,674,2,84]
l3.extend(l4)
print(l3)
# nested list
l5 =["right","left",873,98,235,True,[72,365,327,872,15,267,76,876],776]
print(l5[6][3])
