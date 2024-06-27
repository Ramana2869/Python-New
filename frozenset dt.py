# frozenset data type

s1 ={2,74,43.7,"python"}
print(s1,type(s1))
fs =frozenset(s1)
print(fs,type(fs))
# converting from list to frozenset
s2 =[2,74,43.7,"python"]
fs =frozenset(s2)
print(fs,type(fs))
# converting from tuple to frozenset
s3 =(2,74,43.7,"python",2)
fs =frozenset(s3)
print(fs,type(fs))