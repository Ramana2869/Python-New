# positional parameters or arguments
'''
def stdet(stno,stname,stmarks):
    print("\t{} \t{} \t{}".format(stno,stname,stmarks))
# main prog
print("\tstudent information")
stdet(11,"arun",78)
stdet(12,"vamshi",83)
stdet(13,"nithish",72)
'''
# default parameters or arguments
'''
def stdet(stno,stname,stmarks,course = "Python",country = "India"):
    print("\t{} \t{} \t\t{} \t{} \t{}".format(stno,stname,stmarks,course,country))
# main prog
print("\t\tstudent information")
stdet(11,"arun",78)
stdet(12,"vamshi",83,course="java")
stdet(13,"nithi",72)
stdet(14,"raju",88,country="usa")
stdet(15,"sai",75)
stdet(16,"kiran",90)
'''
'''
# prog to find area & perimeter of circle by using default parameters

def area(r,PI = 3.14):
    ac = PI*r**2
    print("area of circle is {}".format(ac))

def peri(PI = 3.14):
    r = float(input("enter radius of cir for peri: "))
    peri = 2*PI*r
    print("perimeter circle is {}".format(peri))
# main prog
r = float(input("enter radius of cir for area: "))
area(r)
peri()
'''
# keyword parameters or arguments
'''
def empdet(eno,ename,dsg,sal,country = "India"):
    print("\t{}\t{}\t{}\t{}\t{}".format(eno,ename,dsg,sal,country))
# main prog
print("\tEmployee Details")
print("\teno\tename\tdsg\tsal\tcountry")
empdet(21,"raju","se",5.6)
empdet(22,"rakesh",sal = 6.0,dsg = "tr")
empdet(sal = 6.2,ename = "kiran",dsg = "hr",eno = 23)
empdet(24,"nith",dsg = "sm",sal = 5.4,country="canada")
'''
# variable length parameters or arguments

def dis(x):
    print(x)
dis(28)
def dis(x,y):
    print(x,y)      # for this prog we are writing each time function definition and function calling each time
dis(28,69)
def dis(x,y,z):
    print(x,y,z)
dis(28,69,86)
def dis(x,y,z):
    print(x,y,z)
dis("python","java","sql")

'''
def dis(*x):      # here '*x' is variable length parameter --<class,tuple>
    for val in x:
        print(x,type(x))
        print("{}".format(val))
# main prog
dis(10)
dis(10,20)
dis(10,20,30)
dis(10,20,30,40)
dis(10,20,30,40,50)
'''
'''
def sum(name,*marks,standard = 10):
    s = 0
    print("{} {}".format(name,standard))
    for maks in marks:
        print("{}".format(maks))
        s = s+maks
    else:
        print("sum = {}".format(s))
        print()
# main prog
sum("rohit",77,48,38,97,69,86)
sum("jadeja",85,90,95,99,71,100)
sum("axar",73,79,51,57,99,100)
'''
# keyword variable length parameters or arguments

'''
def det(**x):
    print(x,type(x))
# main prog
det(name = "leo")
det(sno = 11,sname = "robert")
det(eno = 21,ename = "michael",dsg = "dancer")
det(rno = 31,rname = "myke",dsg = "boxer",inc = 100000)
'''
'''
def det(**x):
    for k,v in x.items():
        print("\t{}\t{}".format(k,v))
# main prog
det(name = "leo")
det(sno = 11,sname = "robert")
det(eno = 21,ename = "michael",dsg = "dancer")
det(rno = 31,rname = "myke",dsg = "boxer",inc = 100000)
'''
'''
# prog to find total marks secured by diff students and different class students and different subjects
def studet(sname,sclass,**mrks):
    print("stu name   : {}".format(sname))
    print("stu class : {}".format(sclass))
    print("\tsubject\tmarks")
    totalmarks = 0
    for sub,marks in mrks.items():
        print("\t{}\t{}".format(sub,marks))
        totalmarks = totalmarks+marks
    else:
        print("Total marks = {}".format(totalmarks))
# main prog
studet("arjun","inter",eng = 87,maths = 70,phy = 73,che = 90,tel = 58)
studet("mitchell","b.tech",cs = 75,maths = 49,eng = 81)
studet("ravindra","degree",tel = 45,eng = 73,maths = 90,phy = 63)
studet("blesson","b.pharmacy",micro = 99)
studet("israel","bba")
'''