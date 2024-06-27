# filter() function

# filter from list positive & negative values by using normal function
'''
def positive(n):
    if n>0:
        return True
    else:
        return False

def negative(n):
    if n<0:
        return True
    else:
        return False
    
# main prog
lst = [9,28,-32,69,-45,-14,96,89,-82,29,-26]
filtobj = filter(positive,lst)
print("type of filtobj variable = ",type(filtobj))
pslst = list(filtobj)     # here we can convert into tuple and set    # here we converting filter object into collection object type
print("original lst is {}".format(lst))
print("pslst is {}".format(pslst))
filtobj = filter(negative,lst)
nslst = list(filtobj)     # here we can convert into tuple and set
print("negative list is {}".format(nslst))
'''
# filter from list positive & negative values by using lambda function
'''
positive = lambda n : n > 0
negative = lambda n : n < 0

# main prog# main prog
lst = [9,28,-32,69,-45,-14,96,89,-82,29,-26]
filtobj = filter(positive,lst)
print("type of filtobj variable = ",type(filtobj))
pslst = list(filtobj)     # here we can convert into tuple and set    # here we converting filter object into collection object type
print("original lst is {}".format(lst))
print("pslst is {}".format(pslst))
filtobj = filter(negative,lst)
nslst = list(filtobj)     # here we can convert into tuple and set
print("negative list is {}".format(nslst))
'''
# filter from list positive & negative values by using lambda function
'''
lst = [9,28,-32,69,-45,-14,96,89,-82,29,-26]
filtobj = filter(lambda n : n > 0,lst)     # here we can convert into tuple and set    # here we converting filter object into collection object type
pslst = tuple(filtobj)     
print("original lst is {}".format(lst))
print("pslst is {}".format(pslst))
filtobj = filter(lambda n : n< 0,lst)
nslst = set(filtobj)     # here we can convert into tuple and set
print("negative list is {}".format(nslst))
'''

# dynamically entering values into list and filtering +ve and -ve values

lst = []
n = int(input("enter how many no's u want: "))

for i in range(1,n+1):
    val = float(input())
    lst.append(val)
else:
    print("original lst is {}".format(lst))
    pslst = list(filter(lambda n : n > 0,lst))    
    nslst = list(filter(lambda n : n< 0,lst))
    print("original lst is {}".format(lst))
    print("pslst is {}".format(pslst))
    print("negative list is {}".format(nslst))