# approaches to develop a function for problem solving
'''
# approach.1
# input = takes inputs from function call(outside)
# process = process the input inside of function body(inside)
# output = function gives result to the function call(outside)

def sumop(a,b):   # here a,b are formal parameters
    c = a+b       # here c is local variable and process inside
    return c
# main prog
x = float(input("enter first value: "))
y = float(input("enter second value: "))  # input outside
res = sumop(x,y)   # function call
print("sum of {},{} is {}".format(x,y,res))    # output outside
'''
'''
# approach.2
# input = takes inputs in function call(inside)
# process = process the input inside of function body(inside)
# output = function gives result within function body(inside)

def sumop():
    a = float(input("enter a value: "))
    b = float(input("enter b value: "))   # input inside
    c = a+b    # process inside
    print("sum of {},{} is {}".format(a,b,c))   # output inside
# main prog
sumop()  # function call
'''
'''
# approach.3
# input = takes inputs in function body(inside)
# process = process the input inside of function body(inside)
# output = function gives result to the function call(outside)

def sumop():
    a = float(input("enter a value: "))
    b = float(input("enter b value: "))   # input inside
    c = a+b    # process inside
    return ("sum of {},{} is {}".format(a,b,c)) 
# main prog
result = sumop()
print(result)   # output outside
'''
'''
# approach.4
# input = takes inputs from function call(outside)
# process = process the input inside of function body(inside)
# output = function gives result within function body(inside)
def sumop(a,b):
    c = a+b     # process inside
    print("sum of {},{} is {}".format(a,b,c))   # output inside
# main prog
a = float(input("enter a value: "))
b = float(input("enter b value: "))    # input outside
sumop(a,b)
'''
'''
# prog to find square root of a given number
# approach.1
def sqroot(n):
    res = n**0.5
    return res

n = float(input("enter a number: "))
result = sqroot(n)
print(result)
'''
'''
# approach.2
def sqroot():
    n = float(input("enter a number: "))
    res = n**0.5
    print("sqrt of {} is {}".format(n,res))

sqroot()
'''
'''
# approach.3
def sqroot():
    n = float(input("enter a number: "))
    res = n**0.5
    return ("sqrt of {} is {}".format(n,res))

result = sqroot()
print(result)
'''
'''
# approach.4
def sqroot(n):
    res = n**0.5
    print("sqrt of {} is {}".format(n,res))

n = float(input("enter a number: "))
sqroot(n)
'''
'''
# prog to find multiplication table by using functions
def num(n):
    if n<=0:
        print("{} is invalid input".format(n))
    else:
        print("multi of {}".format(n))
        for i in range(1,11):
            print("{} * {} = {}".format(n,i,n*i))
# main prog
x = int(input("enter a number: "))
num(x)
'''
'''
# prog to find sum and avg of list dynamically entered values by using functions
def numbers():
    lst = []
    n = int(input("enter how many no's you want: "))
    for i in range(1,n+1):
        val = float(input("enter {} number: ".format(i)))
        lst.append(val)
    return lst
def sumavg(lst):
    s = 0
    for val in lst:
        print("{}".format(val))
        s = s+val
    else:
        print("sum of list is {}".format(s))
        print("avg of list is {}".format(s/len(lst)))
# main prog
lst = numbers()
sumavg(lst)
'''
# prog to find simple interest and total amount to pay
def intr(P,RI,T):
    SI = P*T*RI/100
    TA = P+SI
    print("Simple intrest for principle is {}".format(SI))
    print("The total amount to pay is {}".format(TA))
# main prog
intr(50000,20,3)