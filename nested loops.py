# nested loop
'''
for i in range(1,6):
    print("*"*30)
    print("value of i (outer loop) {}".format(i))
    print("*"*30)
    for j in range(1,4):
        print("value of j (inner loop) {}".format(j))
    else:
        print("i am out of inner loop")
        print("*"*30)
else:
    print("i am out of outer loop")
'''
'''
i = 1
while(i<6):
    print("*"*30)
    print("val of (outer loop) {}".format(i))
    print("*"*30)
    j = 1
    while(j<6):
        print("val of (inner loop) {}".format(j))
        j = j+1
    else:
        print("i am out inner loop")
        i = i+1
else:
    print("i am out of outer loop")
'''
'''
for i in range(6,0,-1):
    print("i val of (outer loop) {}".format(i))
    print("*"*30)
    j = 1
    while(j<4):
        print("val of j (inner loop) {}".format(j))
        j = j+1
    else:
        print("out of inner loop")
        print("*"*30)
else:
    print("out of outer loop")
'''
'''
j = 1
while(j<4):
    print("val of j (outer loop) {}".format(j))
    print("*"*30)
    for i in range(1,6):
        print("i val of (inner loop) {}".format(i))
    else:
        print("out of inner loop")
        j = j+1
        print("*"*30)
else:
    print("out of outer loop")
'''
'''
lst = [2,8,6,9,28,69]
for n in lst:
    if (n<=0):
        print("{} is invalid input".format(n))
    else:
        print("multi-table of number {}".format(n))
        print("*"*30)
        for i in range(1,11):
            print("{} * {} = {}".format(n,i,n*i))
        else:
            print("out of inner loop")
            print("*"*30)
else:
    print("out of outer loop")
'''
n = int(input("enter how many no's you want: "))
if (n<=0):
    print("{} is invalid input".format(n))
else:
    lst = list()
    for i in range(1,n+1):
        val = input("enter value: {}".format(i))
        lst.append(val)
    else:
        print("list of values {}".format(lst))