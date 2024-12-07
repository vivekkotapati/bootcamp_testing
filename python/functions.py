'''def my_fun():            # defining fun
    print("hello")
my_fun()                 # calling fun

def my_fun(a,b):            # defining fun with parameters
    print("hello",a,b)
my_fun(1,2)                 # calling fun with arguments

def my_function(fname):
  print(fname + " details")

my_function("Emil")
my_function("address")
my_function("phno")

def my_function(child3, child2, child1):  #You can also send arguments with the key = value syntax. 
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def my_function(country = "Norway"):  # The following example shows how to use a default parameter value.
                                      # If we call the function without argument, it uses the default value:
    print("I am from " + country)

my_function("Sweden")
my_function("India")             
my_function()
my_function("Brazil")

'''
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
# variable length ARG
def sum(*n):
    total = 0
    for i in n:
        total += i
    print("sum is:",total)
sum(10,20,30)
sum()
sum(10,20)
# combination of var length arg with other args then for other args we should provide value
def f1(*s,n1):
    for i in s:
        print(i)
    print(n1)

f1(10,'a',20,'b',n1=11)

# **Kwargs

def name(**Kwargs):
    for k,v in Kwargs.items():
        print(k,'=',v)
name(n1=1,n2=2,n3=3)
name(rlno=22,n='vivek',marks=350,subject='python')


def example_function(a, b, *args, **kwargs):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")

example_function(1, 2, 3, 4, key1="value1", key2="value2")
