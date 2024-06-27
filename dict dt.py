# dict data type

d1 ={2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81,10:100}
print(d1,type(d1))
# add
d1[11]=121
print(d1)
# modify
d1[10]=99
print(d1)
# pop
d1.pop(6)
print(d1)
# popitem
d1.popitem()
print(d1)
# keys
print(d1.keys())
# values
print(d1.values())
# get
print(d1.get(3))
print(d1.get(12))

for k,v in  d1.items():
    print(k," ",v)

# items
print(d1.items())
# copy
d2=d1.copy()
print(d2)
# update
d3 ={12:144,13:169,20:400}
d2.update(d3)
print(d2)
# special case
d4 ={1:[2,3,4,5],6:[7,8,9,10],11:[12,13,14,15]}
print(d4)
for a,b in d4.items():
    print(a,">>>>",b)