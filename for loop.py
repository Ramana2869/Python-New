# for loop

'''
for i in range(28,69,3):
    print(i)
'''
'''
# prog to find multiplication table for a given number
import time
n = int(input("enter a number: "))
if (n<=0):
    print("{} is invalid".format(n))
else:
    for i in range(1,11):
        print("{} * {} = {}".format(n,i,n*i))
        time.sleep(1)
'''
'''
# prog to find sum of digits of a given number
n = input("enter a number: ")
s = 0
for i in n:
    x = int(i)
    s = s+x
else:
    print("sum of {} is {}".format(n,s))
'''
'''
# prog to accept list of values and find sum and avg of list
n = int(input("enter how many no's you want: "))
if (n<=0):
    print("{} is invalid".format(n))
else:
    l = list()
    for i in range(1,n+1):
        val = int(input("enter {} value: ".format(i)))
        l.append(val)
    else:
        s = 0
        print("content of list {}".format(l))
        for val in l:
            s = s+val
        else:
            print("sum of list is {}".format(s))
            print("avg of list is {}".format(s/n))
'''
'''
# prog to accept list of values and sort the list
n = int(input("enter how many no's you want: "))
if (n<=0):
    print("{} is invalid".format(n))
else:
    l = list()
    for i in range(1,n+1):
        val = int(input("enter {} value: ".format(i)))
        l.append(val)
    else:
        print("content of list {}".format(l))
        l.sort()
        print("ascending order of list {}".format(l))
        l.sort(reverse=True)
        print("descending order of list {}".format(l))
'''
# prog to accept list of values and search is successfull or search is unsuccessfull
n = int(input("enter how many no's you want: "))
if (n<=0):
    print("{} is invalid".format(n))
else:
    l = list()
    for i in range(1,n+1):
        val = input("enter {} value: ".format(i))
        l.append(val)
    else:
        print("content of list {}".format(l))
        element = input("enter which element you want: ")
        res = l.count(element)
        if (res>0):
            print("search is successfull")
        else:
            print("search is unsuccessfull")