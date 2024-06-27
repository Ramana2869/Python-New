# local and global variables

'''
lang = "PYTHON PROG"    # global variable
def learncrs1():
    crs1 = "DL"          # local variable
    print("To implement '{}' we learn '{}'".format(crs1,lang))
    #print(crs2,crs3)    # not possible to access
#lang = "PYTHON PROG"    # global variable
def learncrs2():         
    crs2 = "ML"          # local variable
    print("To implement '{}' we learn '{}'".format(crs2,lang))
    #print(crs1,crs3)    # not possible to access
#lang = "PYTHON PROG"    # global variable
def learncrs3():
    crs3 = "NL"          # local variable
    print("To implement '{}' we learn '{}'".format(crs3,lang))
    #print(crs1,crs2)    # not possible to access
#lang = "PYTHON PROG"    # global variable

# main prog
#lang = "PYTHON PROG"     # global variable 
learncrs1()
learncrs2()
learncrs3()
#lang = "PYTHON PROG"      # it will give nameerror name 'lang' is not defined 
'''

# global keyword programs
'''
# prog 1
a = 2869

def update():
    global a
    a = a+1

# main prog
print("before update value is {}".format(a))
update()
print("after update value is {}".format(a))
'''

# prog 2
a = 2869
lang = "PYTHON"

def update1():
    global a,lang
    a = a+2869
    lang = lang +" "+ "PROGRAMMING"

def update2():
    global a,lang
    a = a*3
    lang = lang +" "+ "LANGUAGE"

# main prog()
print("before update1 value is {}".format(a))
print("before update1 value is {}".format(lang))
update1()
print("after update1 value is {}".format(a))
print("after update1 value is {}".format(lang))
update2()
print("after update2 value is {}".format(a))
print("after update2 value is {}".format(lang))
