# if statement
'''
ticket = input("do you have a ticket(yes/no):")
if (ticket=="yes"):
    print("enter into theatre")
    print("watch the movie")
    print("eat snacks")
print("go home")
'''
'''
n = float(input("enter a value:"))
if n==0 :
    print("{} is zero".format(n))
if n>0 :
    print("{} is positive".format(n))
if n<0 :
    print("{} is negative".format(n))
'''
'''
a = int(input("enter a value:"))
b = int(input("enter b value:"))
if a==b :
    print("both values are equal")
if a>b :
    print("big of({},{})={}".format(a,b,a))
if b>a :
    print("big of ({},{})={}".format(a,b,b))
'''
'''
a = int(input("enter first value:"))
b = int(input("enter second value:"))
c = int(input("enter third value:"))
if a>b and a>c :
    print("big({},{},{})={}".format(a,b,c,a))
if b>a and b>c :
    print("big({},{},{})={}".format(a,b,c,b))
if c>a and c>b :
    print("big({},{},{})={}".format(a,b,c,c))
if a==b and b==c :
    print("all values are equal")
'''

n = int(input("enter a number:"))
if n%2==0 :
    print("{} is a even number".format(n))
if n%2==1:
    print("{} is a odd number".format(n))