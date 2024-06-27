# while loop
'''
# program to generate 1 to n numbers
n = int(input("Enter how many numbers you want: "))
if (n<=0):
    print("entered number {} is invalid".format(n))
else:
    i = 1           # initialization part
    while(i<=n):    # condition part
        print(i)
        i = i+1     # updation part
'''
'''
# program to generate n to 1 numbers
n = int(input("enter how many numbers you want: "))
if (n<=0):
    print("enteres number {} is invalid".format(n))
else:
    i = n
    while(i>=1):
        print(i)
        i = i-1
'''
'''
# program to generate all the even no's b\w 1 to n numbers
n = int(input("Enter how many numbers you want: "))
if (n<=0):
    print("entered number {} is invalid".format(n))
else:
    i = 2
    while(i<=n):
        print(i)
        i = i+2 
'''  
'''      
# program to generate all the odd no's b\w 1 to n numbers
n = int(input("Enter how many numbers you want: "))
if (n<=0):
    print("entered number {} is invalid".format(n))
else:
    i = 1
    while(i<=n):
        print(i)
        i = i+2
'''
'''
# program to generate multiplication table for a +ve number
n = int(input("Enter number you want: "))
if (n<=0):
    print("entered number {} is invalid".format(n))
else:
    i = 1
    while(i<=10):
        print("{} * {} = {}".format(n,i,n*i))
        i = i+1
'''
'''
# program to find sum of first n natural numbers
n = int(input("enter a natural number: "))
if (n<=0):
    print("entered number {} is invalid".format(n))
else:
    i = 1
    s = 0
    while(i<=n):
        print("{}".format(i))
        s = s+i
        i = i+1
    else:
        print("sum of numbers is {}".format(s))
'''
'''
# program to find sum of squares of first n natural numbers
n = int(input("enter a natural number: "))
if (n<=0):
    print("entered number {} is invalid".format(n))
else:
    i = 1
    ss = 0
    while(i<=n):
        print("{}".format(i))
        ss = ss+i**2
        i = i+1
    else:
        print("sum of squares of numbers is {}".format(ss))
'''
'''
# prog to find sum of cubes of first n natural numbers
n = int(input("enter a natural number: "))
if (n<=0):
    print("entered number {} is invalid".format(n))
else:
    i = 1
    cs = 0
    while(i<=n):
        print("{}".format(i))
        cs = cs+i**3
        i = i+1
    else:
        print("sum of cubes of numbers is {}".format(cs))
'''
'''
# prog to find factors of given number
n = int(input("enter a number: "))
if (n<=0):
    print("entered number {} is invalid".format(n))
else:
    i = 1
    while(i<=n//2):
        if(n%i==0):
            print(i)
        i = i+1
'''
# prog to find sum of digits of a given number
n = int(input("enter a number: "))
if (n<=0):
    print("entered number {} is invalid".format(n))
else:
    s = 0
    while(n>0):
        d = n%10
        s = s+d
        n = n//10
    else:
        print("sum of digits is {}".format(s))