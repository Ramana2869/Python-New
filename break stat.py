# break statement

'''
a = "python"
for i in a:
    if(i=="h"):
        break
    print("{}".format(i))
'''
'''
lst = [10,60,40,80,20,90,30,70,50]
for val in lst:
    if(val==90):
        break
    print("{}".format(val))
else:
    print("code executed")   # else part not executed in break statement
'''
'''
# prog to find given number is prime or not
n = int(input("enter a number: "))
if (n<=1):
    print("{} number is invalid".format(n))
else:
    result = "PRIME"
    for i in range(2,n):
        if(n%i==0):
            result = "NOT PRIME"
            break
    if(result=="PRIME"):
            print("{} is a prime number".format(n))
    else:
            print("{} is not a prime number".format(n))
'''
# prog to find citizen is eligible to vote whether entered a correct age
while(True):
    age = int(input("enter a corrcet age: "))
    if (age>=18) and (age<=100):
        break
print("The citizen is eligible to vote")