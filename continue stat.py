# continue statement

'''
a = "python"
for val in a:
    if(val=="h"):
        continue
    print("{}".format(val))
'''
'''
var = "python programming"
for val in var:
    if(val=="o") or (val=="r"):
        continue
    print("{}".format(val))
else:
    print("else part is excuted")   # else part is executed in continue statement
'''
'''
s1 = (10,20,90,60,40,80,30,50,70)
for val in s1:
    if(val==20) or (val==80) or (val==50):
        continue
    print("{}".format(val))
'''
# prog to accept list of values and only retrieve +ve values
n = int(input("enter how many no's you want: "))
if (n<=0):
    print("{} is invalid".format(n))
else:
    l = list()
    for i in range(1,n+1):
        val = float(input("enter {} value: ".format(i)))
        l.append(val)
    else:
        print("content of list {}".format(l))
        plst = []
        for value in l:
            if(value<=0):
                continue
            plst.append(value)
        else:
            print("plst is {}".format(plst))
        nlst = []
        for value in l:
            if(value>=0):
                continue
            nlst.append(value)
        else:
            print("nlst is {}".format(nlst))
