# if else statement
'''
n = int(input("enter a no:"))
if n%2==0:
    print("{} is even number".format(n))
else:
    print("{} is odd number".format(n))
'''
# nested if else
'''
e_no = int(input("enter emp no:"))
e_name = input("enter emp name:")
basic_sal = float(input("enter emp basic salary:"))
if (basic_sal<=0):
    print("invalid salary")
else:
    if (basic_sal>=10000):
        da = basic_sal*0.2
        ta = basic_sal*0.15
        hra = basic_sal*0.15
        ma = basic_sal*0.1
        gpf = basic_sal*0.02
        lic = basic_sal*0.02
    else:
        da = basic_sal*0.3
        ta = basic_sal*0.25
        hra = basic_sal*0.2
        ma = basic_sal*0.1
        gpf = basic_sal*0.01
        lic = basic_sal*0.01
    net_sal = basic_sal+(da+ta+hra+ma)-(gpf+lic)
    print("*"*50)
    print("emp_no is : {}".format(e_no))
    print("emp_name is : {}".format(e_name))
    print("emp basic salary : {}".format(basic_sal))
    print("emp da : {}".format(da))
    print("emp ta : {}".format(ta))
    print("emp hra : {}".format(hra))
    print("emp ma : {}".format(ma))
    print("emp gpf : {}".format(gpf))
    print("emp lic : {}".format(lic))
    print("*"*50)
    print("emp net salary is : {}".format(net_sal))
    print("*"*50)
'''
# elif statement

d = int(input("enter a digit: "))
if (d==0):
    print("the digit is {} (zero)".format(d))
elif(d==1):
    print("the digit is {} (one)".format(d))
elif(d==2):
    print("the digit is {} (two)".format(d))
elif(d==3):
    print("the digit is {} (three)".format(d))
elif(d==4):
    print("the digit is {} (four)".format(d))
elif(d==5):
    print("the digit is {} (five)".format(d))
elif(d==6):
    print("the digit is {} (six)".format(d))
elif(d==7):
    print("the digit is {} (seven)".format(d))
elif(d==8):
    print("the digit is {} (eight)".format(d))
elif(d==9):
    print("the digit is {} (nine)".format(d))
else:
    print("it is a number")