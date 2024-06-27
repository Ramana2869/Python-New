# string data type

str1 = "the sequence of characters"
# index
print(str1.index("q"))
print(str1.index("o"))
# slicing
print(str1[4])
print(str1[4:])
print(str1[4:12])
print(str1[4:12:2])
print(str1[:12])
print(str1[:12:2])
print(str1[4: :2])
print(str1[: :2])
print(str1[: :])
print(str1[-5:])
print(str1[-5:-1])
print(str1[-5:-1:2])
print(str1[-5: :3])
print(str1[:-5])
print(str1[:-1:])
print(str1[:-1:2])
print(str1[::-2])
print(str1,type(str1))
# len
print(len(str1))
# upper
print(str1.upper())
# lower
print(str1.lower())
# replace
print(str1.replace('o','t'))
# strip
str2 = "   i am ramanareddy   "
print(str2.strip())
# split
print(str1.split())
print(str2.split())