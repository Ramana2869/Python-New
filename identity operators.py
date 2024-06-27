# set
set1 = {"python","java","sql",11,12,3.3,True}
set2 = {"python","java","sql",11,12,3.3,True}
print(set1,id(set1))
print(set2,id(set2))
print(set1 is set2)
print(set1 is not set2)
# int
a = 43578
b = 43578
print(a,id(a))
print(b,id(b))
print(a is b)
print(a is not b)
# float
c = 49.33
d = 49.33
print(c,id(c))
print(d,id(d))
print(c is d)
print(c is not d)
# string
e = "django"
f = "django"
print(e,id(e))
print(f,id(f))
print(e is f)
print(e is not f)
# complex
g = 10+2j
h = 10+2j
print(g,id(g))
print(h,id(h))
print(g is h)
print(g is not h)
# range
r1 = range(20,30)
r2 = range(20,30)
print(r1,id(r1))
print(r2,id(r2))
print(r1 is r2)
print(r1 is not r2)
# bool
bo1 = True
bo2 = True
print(bo1,id(bo1))
print(bo2,id(bo2))
print(bo1 is bo2)
print(bo1 is not bo2)