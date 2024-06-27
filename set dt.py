# set data type

s ={10,20,30,30,40,40,50,60,70}
print(s,type(s))

s1 ={33,"gmail",736.877,True,28,"scroll"}
print(s1,type(s1))
# add()
s1.add("shift")      
print(s1)
# len()
print(len(s1)) 
# remove()    
s1.remove(True)    
print(s1)
# discard()
s1.discard("scroll")   
print(s1)
# pop()
s1.pop()        
print(s1) 
# isdisjoint()
s2 ={10,20,30,40}
s3 ={12,24,36,20}
s4 ={14,28,42,60}
print(s2.isdisjoint(s3))
print(s3.isdisjoint(s4))
print(s3.isdisjoint(set()))
print(set().isdisjoint(set()))
# issuperset()
s5 ={10,20}
print(s2.issuperset(s2))
print(s2.issuperset(s5))
print(s2.issuperset(s3))
print(s2.issuperset(s4))
print(s2.issuperset(set()))
print(set().issuperset(s4))
print(set().issuperset(set()))
# issubset()
print(s5.issubset(s2))
print(s5.issubset(s3))
print(set().issubset(s5))
print(set().issubset(set()))
# union()
print(s2.union(s3))
# intersection()
print(s2.intersection(s3))
# difference
print(s2.difference(s3))
print(s3.difference(s2))
# symmetric-difference
print(s2.symmetric_difference(s3))
# update
s2.update(s4)
print(s2)
# empty set
s =set()
print(s,type(s))
print(len(s))