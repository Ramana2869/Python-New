# lambda or anonymous functions

# prog to calculate temperature conversion by normal function
'''
def tempconv(c):
    tf = 1.8*c+32
    return tf
# main prog
print(tempconv,type(tempconv))
c = float(input("enter the temp in celcius: "))
ft = tempconv(c)
print("the temp in fahreheat is {}".format(ft))
'''

# prog to calculate temperature conversion by lambda function
'''
tempconv1 = lambda c : 1.8*c+32

# main prog
print(tempconv1,type(tempconv1))
c = float(input("enter the temp in celcius: "))
ft = tempconv1(c)
print("the temp in fahreheat is {}".format(ft))
'''

# prog to calculate multiplication of two numbers by using lambda function
'''
multiop = lambda a,b : a*b

# main prog
a = float(input("enter a value: "))
b = float(input("enter b value: "))
res = multiop(a,b)
print("multiplication of two no's is: {}".format(res))
'''

# prog to calculate biggest number from two numbers

biggest = lambda a,b : "equal values" if(a==b) else a if(a>b) else b

a = float(input("enter a value: "))
b = float(input("enter b value: "))
res = biggest(a,b)
print("big {},{} = {} ".format(a,b,res))


# prog to find biggest number from three numbers
'''
findbig = lambda a,b,c : "all values equal" if(a==b) and (b==c) else a if(a>b) and (a>c) else b if(b>a) and (b>c) else c

a = float(input("enter a value: "))
b = float(input("enter b value: "))
c = float(input("enter c value: "))
res = findbig(a,b,c)
print("big {},{},{} = {} ".format(a,b,c,res))
'''